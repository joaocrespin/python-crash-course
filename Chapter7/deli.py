sandwich_orders = [] 

print('\nInsert you sandwich orders, say stop to quit.')
while True:
    sandwich = input('Order: ')
    
    if sandwich == 'stop':
        print()
        break

    sandwich_orders.append(sandwich)

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich} sandwich!')
    finished_sandwiches.append(current_sandwich)

for finished_sandwich in finished_sandwiches:
    print(f'{finished_sandwich} sandwich is finished.')