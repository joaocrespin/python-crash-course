from pathlib import Path

def read_file(path):
    '''Read the lines in a file'''
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f'{path}:')
        for line in contents.splitlines():
            print(line)

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    path = Path(filename)
    read_file(path)