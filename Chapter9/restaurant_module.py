class Restaurant:
    '''Simple model of a restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Describes the type of restaurant and its name'''
        print(f'This is an {self.cuisine_type.title()} food restaurant named {self.restaurant_name.title()}.')

    def open_restaurant(self):
        '''Simulates the opening of the restaurant'''
        print('The restaurant is now open!')