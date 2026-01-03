rivers = {
    'nile':'egypt',
    'amazonas':'brazil',
    'volga':'russia',
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

for river in rivers.keys():
    print(river.upper())

for country in rivers.values():
    print(country)