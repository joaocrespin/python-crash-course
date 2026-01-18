from pathlib import Path
import json

def get_favorite_number():
    '''Prompt the user for their favorite number'''
    while True:
        favorite_number = input('What is your favorite number? ')
        try:
            favorite_number = int(favorite_number)
        except ValueError:
            print('You should only insert numbers!')
        else:
            return favorite_number

def save_favorite_number(path, favorite_number):
    '''Save the user's favorite number into a JSON file'''
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print("Favorite number saved successfully!")

def read_favorite_number(path):
    '''Read the user's favorite number from a JSON file'''
    contents = path.read_text()
    favorite_number = json.loads(contents)
    return favorite_number

def favorite_number():
    '''Tell the user's favorite number or ask for it'''
    path = Path('favorite_number.json')

    if path.exists():
        favorite_number = read_favorite_number(path)
        print(f"I remember your favorite number, it's {favorite_number}!")
    else:
        favorite_number = get_favorite_number()
        save_favorite_number(path, favorite_number)

favorite_number()