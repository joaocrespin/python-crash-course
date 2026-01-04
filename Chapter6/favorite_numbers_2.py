favorite_numbers = {
    'otavio': [1, 8, 0],
    'joao': [3, 7, 12],
    'guilherme': [7],
    'cristiano': [30, 60, 90],
    'ronaldo': [10, 11]
}

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f'{name.capitalize()}\'s favorite numbers are: {numbers}')
    else:
        print(f'{name.capitalize()}\'s favorite number is: {numbers[0]}')