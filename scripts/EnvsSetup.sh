conda env create -f Envs/WavJourney.yml && \
conda env update -f Envs/Bark.yml && \
conda env update -f Envs/AudioCraft.yml && \
conda run --live-stream -n WavJourney pip install -U git+https://git@github.com/facebookresearch/audiocraft@c5157b5bf14bf83449c17ea1eeb66c19fb4bc7f0#egg=audiocraft && \
conda run --live-stream -n WavJourney pip install -U --no-deps voicefixer==0.1.2 && \
conda run --live-stream -n WavJourney pip install -U --no-deps numpy==1.21 && \
conda run --live-stream -n WavJourney pip install -U --no-deps librosa==0.8.1