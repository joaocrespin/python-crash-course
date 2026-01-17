from pathlib import Path

file = Path('guest.txt')

name = input("What's your name?\n")

file.write_text(name)