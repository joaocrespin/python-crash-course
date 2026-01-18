from pathlib import Path
import json


def get_stored_data(path):
    """Get stored user data if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    return username

def get_new_age():
    """Prompt for a new age."""
    while True:
        age = input('What is your age? ')
        try:
            age = int(age)
        except ValueError:
            print('You should only insert numbers!')
        else:
            return age
        
def get_new_color():
    """Prompt for a new favorite color."""
    color = input('What is your favorite color? ')
    return color

def save_user_data(path, username, age, color):
    """Saave the collected user data in a JSON file."""
    user = {
            'username':username,
            'age': age,
            'color': color,
           }
    contents = json.dumps(user)
    path.write_text(contents)

def get_new_data(path):
    """Prompt the user for their data."""
    username = get_new_username()
    age = get_new_age()
    color = get_new_color()
    save_user_data(path, username, age, color)
    print(f"We'll remember you when you come back, {username}!")

def greet_user():
    """Greet the user by name and show their stored data."""
    path = Path('user.json')
    user = get_stored_data(path)
    if user:
        check_name = input(f'Is your username "{user['username']}"? (yes/no)\n')

        if check_name == 'yes':
            print(f"Welcome back, {user['username']}!")
            print(f"You are {user['age']} years old and your favorite color is " 
                f"{user['color']}.")
        elif check_name == 'no':
            get_new_data(path)
        else:
            print('Invalid input!')

    else:
        get_new_data(path)

greet_user()