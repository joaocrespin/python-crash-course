from multiple_modules_user import Users

class Admin(Users):
    '''A simple attempt to represent an admin'''
    
    def __init__(self, first_name, last_name, age, favorite_color, privileges):
        super().__init__(first_name, last_name, age, favorite_color)
        self.privileges = Privileges(privileges)


class Privileges:
    '''A simple attempt to represent the privileges for an admin'''

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        '''Display the admin privileges'''
        print('\nList of privileges:')
        for privilege in self.privileges:
            print(f'\t{privilege}')
