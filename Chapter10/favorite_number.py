from pathlib import Path
import json


while True:
    favorite_number = input('What is your favorite number? ')

    try:
        favorite_number = int(favorite_number)
    except ValueError:
        print('You should only insert numbers!')
    else:
        break

path = Path('favorite_number.json')
contents = json.dumps(favorite_number)
path.write_text(contents)