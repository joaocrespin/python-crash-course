guests = ['frankenstein', 'dracula', 'linus tech tips']

for guest in guests:
    print(f'Hello, {guest.title()}, you are invited to my party!')

popped = guests.pop(1)

print(f'\nOh no, {popped.title()} can\'t make it!\n')

guests.insert(1, 'eric matthes')

for guest in guests:
    print(f'Hello, {guest.title()}, you are invited to my party!')

print('\nWait, I found a bigger table!\n')

guests.insert(0, 'barack obama')
guests.insert(2, 'irene')
guests.append('george')

for guest in guests:
    print(f'Hello, {guest.title()}, you are invited to my party!')

print('\nWAIT! I can only invite two people...\n')

for i in range(4):
    removed_guest = guests.pop()
    print(f'Sorry {removed_guest.title()}, you can\'t come anymore...')

for guest in guests:
    print(f'Hello, {guest.title()}, you are invited to my party!')

del guests[1]
del guests[0]

print(f'\n{guests}')