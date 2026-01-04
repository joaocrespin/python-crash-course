cities = {
    'shenzhen': {'country':'china', 'population':13_000_000, 'fact':'It was a '
        'small fishing village until 1979 and is now a global technology and '
        'finance hub, often referred to as "China\'s Silicon Valley".'},
    'bergen': {'country':'norway', 'population':295_000, 'fact':'Known as the '
        '"Gateway to the Fjords," the city is surrounded by seven mountains and '
        'is one of the rainiest cities in Europe.'},
    'windhoek': {'country':'namibia', 'population': 500_000, 'fact':'It is the '
        'highest capital city in Southern Africa, sitting at an elevation of '
        '1,650 meters (5,413 feet) above sea level.'},
}

for city, information in cities.items():
    print(f'\n{city.capitalize()}:')
    print(f'Localized in {information['country'].capitalize()},' 
         f' It has a population of approximately {information['population']}' 
         f' people.\nA fun fact about the city is: {information['fact']}')