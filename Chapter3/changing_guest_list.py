guests = ['frankenstein', 'dracula', 'linus tech tips']

for guest in guests:
    print(f'Hello, {guest.title()}, you are invited to my party!')

popped = guests.pop(1)

print(f'Oh no, {popped.title()} can\'t make it!')

guests.insert(1, 'eric matthes')

for guest in guests:
    print(f'Hello, {guest.title()}, you are invited to my party!')
