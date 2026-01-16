from random import choice

characters = [22, 45, 33, 54, 'F', 'W', 'Y', 'K', 12, 'L', 99, 98, 56, 77, 10]

my_ticket = [22, 45, 'W', 77]

won = False
count = 0

while not won:
    ticket = []
    while len(ticket) < 4:
        character = choice(characters)
        if character not in ticket:
            ticket.append(character)
    
    if my_ticket == ticket:
        won = True
    else:
        count +=1 
        

print(f"The loop had to run {count} times to give me a winning ticket.")