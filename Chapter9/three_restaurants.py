class Restaurant:
    '''Simple model of a restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Describes the type of restaurant and its name'''
        print(f'\nThis is an {self.cuisine_type.title()} food restaurant named {self.restaurant_name.title()}.')

    def open_restaurant(self):
        '''Simulates the opening of the restaurant'''
        print('The restaurant is now open!')

restaurant_one = Restaurant('Coconut Bamboo', 'brazilian')
restaurant_two = Restaurant('Mango Cane', 'jamaican')
restaurant_three = Restaurant('Potato Wire', 'american')

restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
