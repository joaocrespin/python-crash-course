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

class IceCreamStand(Restaurant):
    '''A simple attempt to represent a ice cream stand'''

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'strawberry', 'pineapple', 
                        'condensed milk', 'coconut']
    
    def list_flavors(self):
        '''Shows the available ice cream flavors '''
        print('\nAvailable flavors:')
        for flavor in self.flavors:
            print(flavor.title())


little_chico = IceCreamStand('Little Chico', 'Cold')
little_chico.describe_restaurant()
little_chico.list_flavors()