class Restaurant:
    '''Simple model of a restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Describes the type of restaurant and its name'''
        print(f'This is an {self.cuisine_type.title()} food restaurant named {self.restaurant_name.title()}.')

    def open_restaurant(self):
        '''Simulates the opening of the restaurant'''
        print('The restaurant is now open!')

    def set_number_served(self, number):
        '''Changes the number of customer served to the desired one'''
        self.number_served = number

    def increment_number_served(self, number):
        '''Increases the amount of customers served'''
        self.number_served += number

restaurant = Restaurant('KFC', 'American')
print(restaurant.number_served)

restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(200)
print(restaurant.number_served)

restaurant.increment_number_served(50)
print(restaurant.number_served)