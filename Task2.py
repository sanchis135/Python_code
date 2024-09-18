# Task 2: draw a piramid with a number de stars in the last row

num = int(input('Enter a number: '))

for num_stars in range(1,num):
    if num_stars%2 == 0 or num_stars == 1:
        print("*"*num_stars)