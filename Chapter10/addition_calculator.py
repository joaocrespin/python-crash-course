print("Welcome to the addition calculator!\nInsert 'q' anytime to exit")

while True:
    first_num = input('\nInsert the first number: ')
    
    if first_num == 'q':
        break
    
    second_num = input('Insert the second number: ')

    if second_num == 'q':
        break

    try:
        first_num = int(first_num)
        second_num = int(second_num)
    except ValueError:
        print('Please, only insert numbers.')
    else:
        print(first_num + second_num)
