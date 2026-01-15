class Users:
    '''A simple attempt to represent a user'''
    
    def __init__(self, first_name, last_name, age, favorite_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.favorite_color = favorite_color
        self.login_attempts = 0

    def describe_user(self):
        '''Displays the user information'''
        print(f"\nThe user's full name is {self.first_name.title()} " 
                f"{self.last_name.title()}, they are {self.age} years old "
                f"and their favorite color is {self.favorite_color.upper()}.")
        
    def greet_user(self):
        '''Greets the user'''
        print(f"It's nice to meet you, {self.first_name.title()}!")

    def increment_login_attempts(self):
        '''Counts how many times the user has tried to login'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Brings the login attempts counter back to 0'''
        self.login_attempts = 0

class Admin(Users):
    '''A simple attempt to represent an admin'''

    def __init__(self, first_name, last_name, age, favorite_color, privileges):
        super().__init__(first_name, last_name, age, favorite_color)
        self.privileges = privileges

    def show_privileges(self):
        '''Display the admin privileges'''
        print('\nList of privileges:')
        for privilege in self.privileges:
            print(f'\t{privilege}')

admin = Admin('Joao', 'Crespin', 20, 'Green', ['can delete posts', 
                                               'can edit other posts', 
                                               'can erase anything'])

admin.describe_user()
admin.show_privileges()

