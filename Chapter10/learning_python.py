from pathlib import Path

path = Path('C:/Users/Cliente/Desktop/python-crash-course/Chapter10/learning_python.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)