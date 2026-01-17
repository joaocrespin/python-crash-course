from pathlib import Path

file = Path('guest_book.txt')

names = ''

while True:
    name = input("\nWhat's your name? ('quit' to exit)\n")

    if name == 'quit':
        break
    else:
        names += f'{name}\n'

file.write_text(names)