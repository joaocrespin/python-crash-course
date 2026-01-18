from pathlib import Path

def find_words(path, word):
    '''Count how many times a word appeared in a file'''
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        word_counter = 0
        for line in contents.splitlines():
            word_counter += line.lower().count(word)
        print(f"The word {word.strip()} appears about {word_counter} times in {path}.")

filenames = ['alice.txt', 'jekyll.txt']
word = 'the '

for filename in filenames:
    path = Path(filename)
    find_words(path, word)
