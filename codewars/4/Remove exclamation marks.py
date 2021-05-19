def remove_exclamation_marks(s):
    return s.replace('!', '')

remove_exclamation_marks("Hello World!")# "Hello World"
remove_exclamation_marks("Hello World!!!")# "Hello World"
remove_exclamation_marks("Hi! Hello!")# "Hi Hello"
remove_exclamation_marks("")# ""
remove_exclamation_marks("Oh, no!!!")# "Oh, no"