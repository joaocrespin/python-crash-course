
first_num = input('Insert the first number: ')
second_num = input('Insert the second number: ')

try:
    first_num = int(first_num)
    second_num = int(second_num)
except ValueError:
    print('Please, only insert numbers.')
else:
    print(first_num + second_num)