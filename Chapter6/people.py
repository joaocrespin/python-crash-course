person_0 = {
    'first_name': 'Gaius',
    'last_name': 'Maro',
    'age': 40,
    'city': 'solitude',
}

person_1 = {
    'first_name': 'Lord',
    'last_name': 'Vivec',
    'age': 4_000,
    'city': 'vivec city',
}

person_2 = {
    'first_name': 'Serjo',
    'last_name': 'Mora',
    'age': 21,
    'city': 'resdayn',
}

people = (person_0, person_1, person_2)


for person in people:
        print(f'\nI have a friend named {person["first_name"].capitalize()}' \
            f' {person["last_name"].capitalize()}, He is {person["age"]}'\
            f' years old and lives in {person["city"].title()}.')