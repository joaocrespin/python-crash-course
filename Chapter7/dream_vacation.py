print('\nIf you could visit one place in the world, where would you go?\n')

poll_answers = {}

active = True
while active:
    name = input('What is your name?\n')
    place = input('Where would you go?\n')
    poll_answers[name] = place

    repeat = input('Is there anyone else who would like to answer the poll (yes/no)?  ')
    if repeat == 'no':
        active = False

print('\nPoll Results:')
for name, place in poll_answers.items():
    print(f'{name.title()} would like to visit {place.title()}!')

