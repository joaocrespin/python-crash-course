def describe_city(name, country='Brazil'):
    print(f'The city of {name.title()} is in {country.title()}')

describe_city('guarulhos')
describe_city(country='china', name='Shanghai')
describe_city('solitude', 'skyrim')