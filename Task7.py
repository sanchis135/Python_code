# Task 2: Create a simple calculator that can add, subtract, multiply, and divide two numbers.

def add (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

print( 'List of operations:\n' \
      '1. Add\n' \
        '2. Subtract\n' \
            '3. Multiply\n' \
                '4. Divide\n')

operation = int(input('Slect numbre of operation of the list: '))

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

if operation == 1:
    print (num_1, ' + ', num_2, ' = ', add(num_1,num_2))
elif operation == 2:
    print (num_1, ' - ', num_2, ' = ', subtract(num_1,num_2))
elif operation == 3:
    print (num_1, ' * ', num_2, ' = ', multiply(num_1,num_2))
elif operation == 4:
    print (num_1, ' / ', num_2, ' = ', divide(num_1,num_2))
else:
    print ('Error')