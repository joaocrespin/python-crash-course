print('Insert your age to discover the price of your ticket, say "-1" to stop.')

active = True
while active:
    age = int(input('Age: '))
    if age == -1:
        active = False
    elif age < 3:
        print('Your ticket is free!')
    elif age >= 3 and age <= 12:
        print('Your ticket costs 10$.')
    elif age > 12:
        print('Your ticket costs 12$')
    else:
        print('Error: something went wrong...')
    