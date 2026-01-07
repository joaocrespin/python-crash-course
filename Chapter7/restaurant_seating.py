table_size = int(input('How many people are in your dinner group? \n'))

if table_size > 8:
    print(f'{table_size} is too much! You\'ll have to wait for a table')
else:
    print('Your table is ready, please come in!')