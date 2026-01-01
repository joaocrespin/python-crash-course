foods = ('cheese', 'string cheese', 'melted cheese', 'cheese pie', 'cheese lasagna')

print("Restaurant's foods: ")
for food in foods:
    print(food.title())

# Trying to modify one of the items
#foods[0] = 'shrimp'

foods = ('cheese', 'string cheese', 'melted cheese', 'shrimp pie', 'shrimp', 'squid ink')

print("Restaurant's revised menu: ")
for food in foods:
    print(food.title())
