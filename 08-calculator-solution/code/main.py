print('**********__MY FIRST CALCULATOR__**********')
print('Please enter the first number:')

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

print('Please select the operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division')

operation = int(input('Enter the operation number: '))

match operation:
    case 1:
        print(f'The result is: {num1 + num2}')
    case 2:
        print(f'The result is: {num1 - num2}')
    case 3:
        print(f'The result is: {num1 * num2}')
    case 4:
        print(f'The result is: {num1 / num2}')
    case _:
        print('Invalid operation number')
