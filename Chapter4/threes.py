numbers = [number*3 for number in range(1, 11)]

for number in numbers:
    print(number)

print(f'The first three numbers are {numbers[:3]}')
print(f'The numbers in the middle are {numbers[3:-3]}')
print(f'The last three numbers are {numbers[-3:]}')
