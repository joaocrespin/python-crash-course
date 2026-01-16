from random import choice

characters = [22, 45, 33, 54, 'F', 'W', 'Y', 'K', 12, 'L', 99, 98, 56, 77, 10]

ticket = []
while len(ticket) < 4:
    character = choice(characters)
    if character not in ticket:
        ticket.append(character)

print(f"Any ticket matching {ticket} won a prize!")