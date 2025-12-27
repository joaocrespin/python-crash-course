guests = ['frankenstein', 'dracula', 'linus tech tips']

for guest in guests:
    print(f'Hello, {guest.title()}, you are invited to my party!')

popped = guests.pop(1)

print(f'Oh no, {popped.title()} can\'t make it!')

guests.insert(1, 'eric matthes')

for guest in guests:
    print(f'Hello, {guest.title()}, you are invited to my party!')

print('Wait, I found a bigger table!')

guests.insert(0, 'barack obama')
guests.insert(2, 'irene')
guests.append('george')

for guest in guests:
    print(f'Hello, {guest.title()}, you are invited to my party!')