import shutil
import json5
import traceback

import gradio as gr
from tabulate import tabulate

import utils
import pipeline
from pipeline import generate_json_file, generate_audio
from voice_presets import load_voice_presets_metadata, add_session_voice_preset, \
    remove_session_voice_preset
from share_btn import community_icon_html, loading_icon_html, share_js



VOICE_PRESETS_HEADERS = ['ID', 'Description']
DELETE_FILE_WHEN_DO_CLEAR = False
DEBUG = False


def convert_json_to_md(audio_script_response):
    audio_json_data = json5.loads(audio_script_response)
    table = [[node.get(field, 'N/A') for field in ["audio_type", "layout", "id", "character", "action", 'vol']] +
             [node.get("desc", "N/A") if node.get("audio_type") != "speech" else node.get("text", "N/A")] +
             [node.get("len", "Auto") if "len" in node else "Auto"]
             for i, node in enumerate(audio_json_data)]

    headers = ["Audio Type", "Layout", "ID", "Character", "Action", 'Volume', "Description", "Length" ]

    # Tabulate
    table_txt = tabulate(table, headers, tablefmt="github")
    return table_txt


def convert_char_voice_map_to_md(char_voice_map):
    table =[[character, char_voice_map[character]["id"]] for character in char_voice_map]
    headers = ["Character", "Voice"]
    # Tabulate
    table_txt = tabulate(table, headers, tablefmt="github")
    return table_txt


def get_or_create_session_from_state(ui_state):
    if 'session_id' not in ui_state:
        ui_state['session_id'] = pipeline.init_session()
    return ui_state['session_id']


def generate_script_fn(instruction, _state: gr.State):
    try:
        session_id = get_or_create_session_from_state(_state)
        api_key = utils.get_api_key()
        json_script = generate_json_file(session_id, instruction, api_key)
        table_text = convert_json_to_md(json_script)
    except Exception as e:
        gr.Warning(str(e))
        print(f"Generating script error: {str(e)}")
        traceback.print_exc()
        return [
            None,
            _state,
            gr.Button.update(interactive=False),
            gr.Button.update(interactive=True),
            gr.Button.update(interactive=True),
            gr.Button.update(interactive=True),
        ]

    _state = {
        **_state,
        'session_id': session_id,
        'json_script': json_script
    }
    return [
        table_text, 
        _state,
        gr.Button.update(interactive=True),
        gr.Button.update(interactive=True),
        gr.Button.update(interactive=True),
        gr.Button.update(interactive=True),
    ]


def generate_audio_fn(state):
    btn_state = gr.Button.update(interactive=True)
    try:
        api_key = utils.get_api_key()
        audio_path, char_voice_map = generate_audio(**state, api_key=api_key)
        table_text = convert_char_voice_map_to_md(char_voice_map)
        # TODO: output char_voice_map to a table
        return [
            table_text,
            gr.make_waveform(str(audio_path)),
            btn_state,
            btn_state,
            btn_state,
            btn_state,
        ]
    except Exception as e:
        print(f"Generation audio error: {str(e)}")
        traceback.print_exc()
        gr.Warning(str(e))

    return [
        None,
        None,
        btn_state,
        btn_state,
        btn_state,
        btn_state,
    ]


def clear_fn(state):
    if DELETE_FILE_WHEN_DO_CLEAR:
        shutil.rmtree('output', ignore_errors=True)
    state = {'session_id': pipeline.init_session()}
    return [gr.Markdown.update(value=''),
            gr.Textbox.update(value=''), 
            gr.Video.update(value=None),
            gr.Markdown.update(value=''), 
            gr.Button.update(interactive=False), 
            gr.Button.update(interactive=False),
            state, gr.Dataframe.update(visible=False), 
            gr.Button.update(visible=False),
            gr.Textbox.update(value=''), 
            gr.Textbox.update(value=''), 
            gr.File.update(value=None)]


def textbox_listener(textbox_input):
    if len(textbox_input) > 0:
        return gr.Button.update(interactive=True)
    else:
        return gr.Button.update(interactive=False)


def get_voice_preset_to_list(state: gr.State):
    if state.__class__ == gr.State:
        state = state.value
    if 'session_id' in state:
        path = utils.get_session_voice_preset_path(state['session_id'])
    else:
        path = ''
    voice_presets = load_voice_presets_metadata(
        path,
        safe_if_metadata_not_exist=True
    )
    dataframe = []
    for key in voice_presets.keys():
        row = [key, voice_presets[key]['desc']]
        dataframe.append(row)
    return dataframe


def df_on_select(evt: gr.SelectData):
    print(f"You selected {evt.value} at {evt.index} from {evt.target}")
    return {'selected_voice_preset': evt.index}


def del_voice_preset(selected_voice_presets, ui_state, dataframe):
    gr_visible = gr.Dataframe.update(visible=True)
    btn_visible = gr.Button.update(visible=True)
    current_presets = get_voice_preset_to_list(ui_state)
    if selected_voice_presets['selected_voice_preset'] is None or \
            selected_voice_presets['selected_voice_preset'][0] > len(current_presets) - 1:
        gr.Warning('None row is selected')
        return [current_presets, gr_visible, btn_visible, selected_voice_presets]
    # Do the real file deletion
    index = selected_voice_presets['selected_voice_preset'][0]
    vp_id = dataframe['ID'][index]
    remove_session_voice_preset(vp_id, ui_state['session_id'])
    current_presets = get_voice_preset_to_list(ui_state)
    gr.Dataframe.update(value=current_presets)
    if len(current_presets) == 0:
        gr_visible = gr.Dataframe.update(visible=False)
        btn_visible = gr.Button.update(visible=False)
    selected_voice_presets['selected_voice_preset'] = None
    return [current_presets, gr_visible, btn_visible, selected_voice_presets]


def get_system_voice_presets():
    system_presets = load_voice_presets_metadata(utils.get_system_voice_preset_path())
    data = []
    for k, v in system_presets.items():
        data.append([k, v['desc']])
    # headers = ['id', 'description']
    # table_txt = tabulate(data, headers, tablefmt="github")
    return data


def set_openai_key(key, _state):
    _state['api_key'] = key
    return key


def add_voice_preset(vp_id, vp_desc, file, ui_state, added_voice_preset):
    if vp_id is None or vp_desc is None or file is None or vp_id.strip() == '' or vp_desc.strip() == '':
        gr.Warning('please complete all three fields')
    else:
        count: int = added_voice_preset['count']
        # check if greater than 3
        session_id = get_or_create_session_from_state(ui_state)
        file_path = file.name
        print(f'session {session_id}, id {id}, desc {vp_desc}, file {file_path}')
        # Do adding ...
        try:
            add_session_voice_preset(vp_id, vp_desc, file_path, session_id)
            added_voice_preset['count'] = count + 1
        except Exception as exception:
            print(exception)
            traceback.print_exc()
            gr.Warning(str(exception))

    # After added
    dataframe = get_voice_preset_to_list(ui_state)
    df_visible = gr.Dataframe.update(visible=True)
    del_visible = gr.Button.update(visible=True)
    if len(dataframe) == 0:
        df_visible = gr.Dataframe.update(visible=False)
        del_visible = gr.Button.update(visible=False)
    return [gr.Textbox.update(value=''), gr.Textbox.update(value=''), gr.File.update(value=None),
            ui_state, added_voice_preset, dataframe, gr.Button.update(interactive=True),
            df_visible, del_visible]


css = """
        a {
            color: inherit;
            text-decoration: underline;
        }
        .gradio-container {
            font-family: 'IBM Plex Sans', sans-serif;
        }
        .gr-button {
            color: white;
            border-color: #000000;
            background: #000000;
        }
        input[type='range'] {
            accent-color: #000000;
        }
        .dark input[type='range'] {
            accent-color: #dfdfdf;
        }
        .container {
            max-width: 730px;
            margin: auto;
            padding-top: 1.5rem;
        }
        #gallery {
            min-height: 22rem;
            margin-bottom: 15px;
            margin-left: auto;
            margin-right: auto;
            border-bottom-right-radius: .5rem !important;
            border-bottom-left-radius: .5rem !important;
        }
        #gallery>div>.h-full {
            min-height: 20rem;
        }
        .details:hover {
            text-decoration: underline;
        }
        .gr-button {
            white-space: nowrap;
        }
        .gr-button:focus {
            border-color: rgb(147 197 253 / var(--tw-border-opacity));
            outline: none;
            box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
            --tw-border-opacity: 1;
            --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
            --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(3px var(--tw-ring-offset-width)) var(--tw-ring-color);
            --tw-ring-color: rgb(191 219 254 / var(--tw-ring-opacity));
            --tw-ring-opacity: .5;
        }
        #advanced-btn {
            font-size: .7rem !important;
            line-height: 19px;
            margin-top: 12px;
            margin-bottom: 12px;
            padding: 2px 8px;
            border-radius: 14px !important;
        }
        #advanced-options {
            margin-bottom: 20px;
        }
        .footer {
            margin-bottom: 45px;
            margin-top: 35px;
            text-align: center;
            border-bottom: 1px solid #e5e5e5;
        }
        .footer>p {
            font-size: .8rem;
            display: inline-block;
            padding: 0 10px;
            transform: translateY(10px);
            background: white;
        }
        .dark .footer {
            border-color: #303030;
        }
        .dark .footer>p {
            background: #0b0f19;
        }
        .acknowledgments h4{
            margin: 1.25em 0 .25em 0;
            font-weight: bold;
            font-size: 115%;
        }
        #container-advanced-btns{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
        }
        .animate-spin {
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            from {
                transform: rotate(0deg);
            }
            to {
                transform: rotate(360deg);
            }
        }
        #share-btn-container {
            display: flex; padding-left: 0.5rem !important; padding-right: 0.5rem !important; background-color: #000000; justify-content: center; align-items: center; border-radius: 9999px !important; width: 13rem;
            margin-top: 10px;
            margin-left: auto;
        }
        #share-btn {
            all: initial; color: #ffffff;font-weight: 600; cursor:pointer; font-family: 'IBM Plex Sans', sans-serif; margin-left: 0.5rem !important; padding-top: 0.25rem !important; padding-bottom: 0.25rem !important;right:0;
        }
        #share-btn * {
            all: unset;
        }
        #share-btn-container div:nth-child(-n+2){
            width: auto !important;
            min-height: 0px !important;
        }
        #share-btn-container .wrap {
            display: none !important;
        }
        .gr-form{
            flex: 1 1 50%; border-top-right-radius: 0; border-bottom-right-radius: 0;
        }
        #prompt-container{
            gap: 0;
        }
        #generated_id{
            min-height: 700px
        }
        #setting_id{
          margin-bottom: 12px;
          text-align: center;
          font-weight: 900;
        }
"""

with gr.Blocks(css=css) as interface:

    gr.HTML(
            """
                <div style="text-align: center; max-width: 700px; margin: 0 auto;">
                <div
                    style="
                    display: inline-flex;
                    align-items: center;
                    gap: 0.8rem;
                    font-size: 1.75rem;
                    "
                >
                    <h1 style="font-weight: 900; margin-bottom: 7px; line-height: normal;">
                    WavJourney: Compositional Audio Creation with LLMs
                    </h1>
                </div>
                <p style="margin-bottom: 10px; margin-top: 10px; font-size: 94%">
                    <a href="https://arxiv.org/abs/2307.14335">[Paper]</a> <a href="https://audio-agi.github.io/WavJourney_demopage/">[Demo Page]</a> <a href="https://github.com/Audio-AGI/WavJourney">[GitHub]</a> <a href="https://discord.com/invite/5Hqu9NmA8V">[Join Discord]</a>
                </p>
                </div>
            """
        )

    gr.HTML(
        """
        <p>For faster inference without waiting in queue, you may duplicate the space and upgrade to GPU (VRAM>16G) in settings.
        <br>
        <a href="https://huggingface.co/spaces/Audio-AGI/WavJourney?duplicate=true">
        <img style="margin-top: 0em; margin-bottom: 0em" src="https://bit.ly/3gLdBN6" alt="Duplicate Space"></a>
        <p/>
    """
    )

    gr.HTML(
        """
        <p>Begin with a text prompt, and let WavJourney transform it into captivating audio content. Experience engaging audio storylines, personalized voices, lifelike speech, emotionally resonant musical compositions, and immersive sound effects!
        <p/>
    """
    )

    gr.HTML(
        """
        <p>WavJourney Pipeline:<p/>
        <ul>
        <li>Stage 0: (optional) add your customized voice preset for more personalized audio creation experience.</li>
        <li>Stage 1: generate the audio script based on the input text instruction (the default language is English, but you can actually type in your own language).</li>
        <li>Stage 2: Select the suitable voice in the multilingual voice preset for the each character in the audio script & generate audio.</li>
        </ul>


    """
    )



    system_voice_presets = get_system_voice_presets()
    # State
    ui_state = gr.State({})
    selected_voice_presets = gr.State(value={'selected_voice_preset': None})
    added_voice_preset_state = gr.State(value={'added_file': None, 'count': 0})
    # UI Component
    # gr.Markdown(
    # """
    # How can I access GPT-4? <a href="https://platform.openai.com/account/api-keys">[Ref1]</a><a href="https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4">[Ref2]</a>
    # """
    # )
    # key_text_input = gr.Textbox(label='Please Enter OPENAI Key for accessing GPT-4 API', lines=1, placeholder="OPENAI Key here.",
    #                         value=utils.get_key())
    text_input_value = '' if DEBUG is False else "an audio introduction to quantum mechanics"
    
    text_input = gr.Textbox(
        label='Input Text Instruction', 
        lines=2, 
        placeholder="Input instruction here (e.g., An introduction to AI-assisted audio content creation).",
        value=text_input_value,
        elem_id="prompt-in",)

    gr.Markdown(
    """
    Clicking 'Generate Script' button, the generated audio script will be displayed below.
    """
    )
    audio_script_markdown = gr.Markdown(label='Audio Script')
    generate_script_btn = gr.Button(value='Generate Script', interactive=False)
    
    gr.Markdown(
    """
    Clicking 'Generate Audio' button, the voice mapping results & generated audio will be displayed below.
    """
    )
    char_voice_map_markdown = gr.Markdown(label='Character-to-voice Map')

    audio_output = gr.Video(elem_id="output-video")

    generate_audio_btn = gr.Button(value='Generate Audio', interactive=False)
    
    # share to community
    with gr.Group(elem_id="share-btn-container", visible=False):
        community_icon = gr.HTML(community_icon_html)
        loading_icon = gr.HTML(loading_icon_html)
        share_button = gr.Button(value="Share to community", elem_id="share-btn")

    gr.HTML(
        """
        <p>Share your generations with the community by clicking the share icon at the bottom right the generated audio!<p/>
        <p>
        Useful tips for prompting WavJourney:
        <p/>
        <ul> 
        <li>You can use vague or specific descriptions, or a combination of them. For example: "male speech about pizze" or "a man is saying: I love pizza!"</li>
        <li> You can control the length of audio script by simply adding the restriction. For example: "generate an audio script around 10-15 lines (max length has been set to 30)"</li>
        <li> You can specify the language of the speaker. For example: "a boy is playing with a girl, boy's speech is in Chinese while girl's speech in Japanese"</li>
        <li> Explore more prompting techniques by yourself! 🤗</li>
        </ul>

    """
    )

    # add examples
    from examples.examples import examples as WJExamples
    def example_fn(idx, _text_input):
        print('from example', idx, _text_input)
        example = WJExamples[int(idx)-1]
        print(example['table_script'], example['table_voice'], gr.make_waveform(example['wav_file']))
        return example['table_script'], example['table_voice'], gr.make_waveform(example['wav_file'])

    _idx_input = gr.Textbox(label='Example No.')
    _idx_input.visible=False
    gr.Examples(
            [[idx+1, x['text']] for idx, x in enumerate(WJExamples)],
            fn=example_fn,
            inputs=[_idx_input, text_input],
            outputs=[audio_script_markdown, char_voice_map_markdown, audio_output],
            cache_examples=True,
        )

    # System Voice Presets
    gr.Markdown(label='System Voice Presets', value='# System Voice Presets')
    with gr.Accordion("Click to check system speakers", open=False):
        gr.Markdown('Supported Language: English, Chinese, French, German, Hindi, Italian, Japanese, Korean, Russian, Spanish, Polish, Portuguese')

        system_markdown_voice_presets = gr.Dataframe(label='System Voice Presets', headers=VOICE_PRESETS_HEADERS,
                                                    value=system_voice_presets)
    # User Voice Preset Related
    gr.Markdown('# (Optional) Speaker Customization ')
    with gr.Accordion("Click to add speakers", open=False):
        gr.Markdown(label='User Voice Presets', value='## User Voice Presets')
        get_voice_preset_to_list(ui_state)
        voice_presets_df = gr.Dataframe(headers=VOICE_PRESETS_HEADERS, col_count=len(VOICE_PRESETS_HEADERS),
                                    value=get_voice_preset_to_list(ui_state), interactive=False, visible=False)
    # voice_presets_ds = gr.Dataset(components=[gr.Dataframe(visible=True)], samples=get_voice_preset_to_list(ui_state))
        del_voice_btn = gr.Button(value='Delete Selected Voice Preset', visible=False)
        gr.Markdown(label='Add Voice Preset', value='## Add Voice Preset')
        gr.Markdown(
        """
        
        What makes for good voice prompt? See detailed instructions <a href="https://github.com/gitmylo/bark-voice-cloning-HuBERT-quantizer">here</a>. 
        """
        )
        vp_text_id = gr.Textbox(label='Id', lines=1, placeholder="Input voice preset id here.")
        vp_text_desc = gr.Textbox(label='Desc', lines=1, placeholder="Input description here.")
        vp_file = gr.File(label='Wav File', type='file', file_types=['.wav'],
                        interactive=True)
        vp_submit = gr.Button(label='Upload Voice Preset', value="Upload Voice Preset")
    
    # clear btn, will re-new a session
    clear_btn = gr.ClearButton(value='Clear All')

    # disclaimer
    gr.Markdown(
        """
    # Disclaimer
    We are not responsible for audio generated using semantics created by WavJourney. Just don't use it for illegal purposes.
    """
    )

    # events
    # key_text_input.change(fn=set_openai_key, inputs=[key_text_input, ui_state], outputs=[key_text_input])
    text_input.change(fn=textbox_listener, inputs=[text_input], outputs=[generate_script_btn])
    generate_audio_btn.click(
        fn=generate_audio_fn,
        inputs=[ui_state],
        outputs=[
            char_voice_map_markdown,
            audio_output,
            generate_audio_btn,
            generate_script_btn,
            clear_btn,
            vp_submit,
        ],
        api_name='audio_journey',
    )
    generate_audio_btn.click(
        fn=lambda: [
            gr.Button.update(interactive=False),
            gr.Button.update(interactive=False),
            gr.Button.update(interactive=False),
            gr.Button.update(interactive=False),
        ],
        outputs=[
            generate_audio_btn,
            generate_script_btn,
            clear_btn,
            vp_submit,
        ]
    )
    clear_btn.click(fn=clear_fn, inputs=ui_state,
                    outputs=[char_voice_map_markdown, text_input, audio_output, audio_script_markdown, generate_audio_btn, generate_script_btn,
                             ui_state, voice_presets_df, del_voice_btn,
                             vp_text_id, vp_text_desc, vp_file])
    generate_script_btn.click(
        fn=generate_script_fn, inputs=[text_input, ui_state],
        outputs=[
            audio_script_markdown,
            ui_state,
            generate_audio_btn,
            generate_script_btn,
            clear_btn,
            vp_submit,
        ]
    )
    generate_script_btn.click(
        fn=lambda: [
            gr.Button.update(interactive=False),
            gr.Button.update(interactive=False),
            gr.Button.update(interactive=False),
            gr.Button.update(interactive=False),
        ],
        outputs=[
            generate_audio_btn,
            generate_script_btn,
            clear_btn,
            vp_submit,
        ]
    )
    voice_presets_df.select(df_on_select, outputs=[selected_voice_presets])
    voice_presets_df.update(lambda x: print(x))
    del_voice_btn.click(del_voice_preset, inputs=[selected_voice_presets, ui_state, voice_presets_df],
                        outputs=[voice_presets_df, voice_presets_df, del_voice_btn, selected_voice_presets])
    # user voice preset upload
    vp_submit.click(add_voice_preset, inputs=[vp_text_id, vp_text_desc, vp_file, ui_state, added_voice_preset_state],
                    outputs=[vp_text_id, vp_text_desc, vp_file, ui_state, added_voice_preset_state, voice_presets_df,
                             vp_submit,
                             voice_presets_df, del_voice_btn])
    vp_submit.click(lambda _: gr.Button.update(interactive=False), inputs=[vp_submit])
    
    # share to HF community
    share_button.click(None, [], [], _js=share_js)

    # debug only
    # print_state_btn = gr.Button(value='Print State')
    # print_state_btn.click(fn=lambda state, state2: print(state, state2), inputs=[ui_state, selected_voice_presets])
interface.queue(concurrency_count=10, max_size=20)
interface.launch()
