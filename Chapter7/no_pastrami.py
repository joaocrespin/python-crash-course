sandwich_orders = ['tuna', 'ice cream', 'pastrami', 'chiken', 'ground beef', 'pastrami', 'tomato', 'beans', 'pastrami', 'cheese'] 

print('\nSorry, the Deli has runb out of PASTRAMI.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich} sandwich!')
    finished_sandwiches.append(current_sandwich)

print()

for finished_sandwich in finished_sandwiches:
    print(f'{finished_sandwich.title()} sandwich is finished.')