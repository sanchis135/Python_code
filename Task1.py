# Task 1: Write a Python script to check if a number is even or odd.

def odd_even(variable):
    if (variable % 2 == 0):
        print ('Number is odd')
    else:
        print('Number is even')

num = int(input('Enter a number: '))

odd_even(num)