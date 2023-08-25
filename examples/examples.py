
example1 = {
    'text': "An introduction to AI-assisted audio content creation.",
    'table_script': """
| Audio Type   | Layout     | ID | Character | Action | Volume | Description                                                      | Length |
|--------------|------------|----|-----------|--------|--------|------------------------------------------------------------------|--------|
| music        | background | 1  | N/A       | begin  | -35    | Inspirational technology-themed music                            | Auto   |
| speech       | foreground | N/A| Narrator  | N/A    | -15    | Welcome to the future of audio content creation.                 | Auto   |
| sound_effect | foreground | N/A| N/A       | N/A    | -35    | Digital startup sound                                            | 2      |
| speech       | foreground | N/A| Narrator  | N/A    | -15    | With evolving technology, we are introducing AI-assisted tools for pristine audio production. | Auto |
| sound_effect | foreground | N/A| N/A       | N/A    | -35    | Keyboard typing noise                                            | 3      |
| speech       | foreground | N/A| Narrator  | N/A    | -15    | Imagine crafting audio content with the power of AI at your fingertips. | Auto |
| sound_effect | background | 2  | N/A       | begin  | -35    | Ambiance of a busy control room                                   | Auto   |
| speech       | foreground | N/A| Narrator  | N/A    | -15    | Enhanced quality, efficient production and limitless creativity, all under one roof. | Auto |
| sound_effect | background | 2  | N/A       | end    | N/A    | N/A                                                              | Auto   |
| speech       | foreground | N/A| Narrator  | N/A    | -15    | Unleash your potential with AI-assisted audio content creation.  | Auto   |
| music        | background | 1  | N/A       | end    | N/A    | N/A                                                              | Auto   |

""",
    'table_voice': """
| Character   | Voice     |
|-------------|-----------|
| Narrator    | News_Male_En |

""",
    'wav_file': 'examples/1.mp4',
}

example2 = {
    'text': "A couple dating in a cafe.",
    'table_script': """
| Audio Type   | Layout     | ID | Character | Action | Volume | Description                                   | Length |
|--------------|------------|----|-----------|--------|--------|-----------------------------------------------|--------|
| sound_effect | background | 1  | N/A       | begin  | -35    | Soft chattering in a cafe                     | Auto   |
| sound_effect | background | 2  | N/A       | begin  | -38    | Coffee brewing noises                         | Auto   |
| music        | background | 3  | N/A       | begin  | -35    | Soft jazz playing in the background           | Auto   |
| speech       | foreground | N/A| Man       | N/A    | -15    | It’s really nice to finally get out and relax a little, isn’t it? | Auto |
| speech       | foreground | N/A| Woman     | N/A    | -15    | I know, right? We should do this more often.  | Auto   |
| sound_effect | background | 2  | N/A       | end    | N/A    | N/A                                           | Auto   |
| speech       | foreground | N/A| Man       | N/A    | -15    | Here’s your coffee, just as you like it.      | Auto   |
| speech       | foreground | N/A| Woman     | N/A    | -15    | Thank you, it smells wonderful.               | Auto   |
| music        | background | 3  | N/A       | end    | N/A    | N/A                                           | Auto   |
| sound_effect | background | 1  | N/A       | end    | N/A    | N/A                                           | Auto   |

""",
    'table_voice': """
| Character   | Voice     |
|-------------|-----------|
| Man         | Male1_En    |
| Woman       | Female1_En   |

""",
    'wav_file': 'examples/2.mp4',
}


example3 = {
    'text': "A child is participating in a farting contest.",
    'table_script': """
| Audio Type   | Layout     | ID | Character | Action | Volume | Description                                          | Length |
|--------------|------------|----|-----------|--------|--------|------------------------------------------------------|--------|
| sound_effect | background | 1  | N/A       | begin  | -35    | Outdoor park ambiance, people chattering             | Auto   |
| music        | background | 2  | N/A       | begin  | -35    | Light comedy theme music, quirky                     | Auto   |
| speech       | foreground | N/A| Host      | N/A    | -15    | Welcome to the annual Fart Competition.              | Auto   |
| speech       | foreground | N/A| Host      | N/A    | -15    | Now, let’s welcome our youngest participant.         | Auto   |
| sound_effect | foreground | N/A| N/A       | N/A    | -35    | Clapping sound                                       | 2      |
| speech       | foreground | N/A| Child     | N/A    | -15    | Hi, I’m excited to be here.                          | Auto   |
| sound_effect | foreground | N/A| N/A       | N/A    | -35    | Short, cartoonish duration of a fart sound           | 4      |
| sound_effect | foreground | N/A| N/A       | N/A    | -35    | Audience laughing and applauding                     | 2      |
| speech       | foreground | N/A| Host      | N/A    | -15    | Wow, that was impressive! Let’s give another round of applause! | Auto |
| sound_effect | foreground | N/A| N/A       | N/A    | -35    | Audience clapping and cheering                       | 3      |
| music        | background | 2  | N/A       | end    | N/A    | N/A                                                  | Auto   |
| sound_effect | background | 1  | N/A       | end    | N/A    | N/A                                                  | Auto   |
""",
    'table_voice': """
| Character   | Voice     |
|-------------|-----------|
| Host        | Male1_En     |
| Child       | Child_En     |

""",
    'wav_file': 'examples/3.mp4',
}



examples = [example1, example2, example3]