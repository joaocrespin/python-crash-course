print('Choose your pizza toppings! (say quit to stop)')

while True:
    topping = input('Topping: ')
    if topping == 'quit':
       break
    else:
        print(f'Adding {topping} to the pizza.')