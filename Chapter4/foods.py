foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = foods[:]

foods.append('bell pepper')

friend_foods.append('eggs')

print('My favorite foods are:')
for food in foods:
    print(food)

print('My friend\'s favorite foods are:')
for food in friend_foods:
    print(food)

