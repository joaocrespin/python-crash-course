from pathlib import Path


path = Path('C:/Users/Cliente/Desktop/python-crash-course/Chapter10/pi_digits.txt')

for line in path.read_text().splitlines():
    print(line)