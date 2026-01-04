pet_0 = {
    'name': 'pancinha',
    'type': 'dog',
    'owner': 'crespin',
}

pet_1 = {
    'name': 'nug',
    'type': 'dog',
    'owner': 'joão guilherme',
}

pet_2 = {
    'name': 'doug',
    'type': 'ferret',
    'owner': 'luis',
}

pet_3 = {
    'name': 'crystal',
    'type': 'cat',
    'owner': 'guilherme',
}

pet_4 = {
    'name': 'olhudo',
    'type': 'bird',
    'owner': 'matheus',
}

pets = (pet_0,pet_1,pet_2,pet_3,pet_4)

for pet in pets:
    print(f"{pet['name'].capitalize()} is a {pet['type']} owned by {pet['owner'].title()}.")