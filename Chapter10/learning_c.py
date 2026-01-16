from pathlib import Path

path = Path('C:/Users/Cliente/Desktop/python-crash-course/Chapter10/learning_python.txt')
contents = path.read_text()

contents = contents.replace('Python', 'C')

for line in contents.splitlines():
    print(line)