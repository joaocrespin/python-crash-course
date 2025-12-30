pizzas = ['Calabrese', 'Bahian', 'Margherita']

friend_pizzas = pizzas[:]

pizzas.append('Napolitan')

friend_pizzas.insert(0, 'Portuguese')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('My friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)