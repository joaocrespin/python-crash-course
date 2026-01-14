class Users:
    '''A simple attempt to represent a user'''
    
    def __init__(self, first_name, last_name, age, favorite_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.favorite_color = favorite_color

    def describe_user(self):
        '''Displays the user information'''
        print(f"\nThe user's full name is {self.first_name.title()} " 
                f"{self.last_name.title()}, they are {self.age} years old "
                f"and their favorite color is {self.favorite_color.upper()}.")
        
    def greet_user(self):
        '''Greets the user'''
        print(f"It's nice to meet you, {self.first_name.title()}!")

crespin = Users('joao', 'crespin', 20, 'green')
crespin.describe_user()
crespin.greet_user()

amanda = Users('amanda', 'nunes', 18, 'purple')
amanda.describe_user()
amanda.greet_user()

juan = Users('juan', 'juan', 21, 'black')
juan.describe_user()
juan.greet_user()
