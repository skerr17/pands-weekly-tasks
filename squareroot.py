# squareroot.py
# Week 6's weekly task 
# This program takes a positive floating-point number as input 
# and outputs an approximation of its square root
# The program uses Newton's method to approximate the square root of a number
# Author: Stephen Kerr

while True:
    try:    
        # prompt the user for a number
        number = float(input('Please Enter a Positive Number: '))

        if number <= 0:
            print("The number must be greater than zero. Try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid positive number.")


tolerance = 0.00001 # number of decimal places to approximate to be accurate to 5 decimal places

# calculate the approximate square root of the number
# using Newton's method
def newton_method(number, tolerance):
    # Assuming the sqrt of number as number only
    x = number
    # count the number of iterations 
    count = 0
    # loop until the difference between the square of x and number is less than 0.00001
    while True:
        count += 1
        # calculate the square root of the number
        root = 0.5 * (x + number / x)
        # check if the difference between the square of x and number is less than 0.00001
        if abs(root - x) < tolerance:
            break
        # update the value of x
        x = root
    return root, count

# call the newton_method function
root, count = newton_method(number, tolerance)

# print the approximate square root of the number 
print(f'The Approximate Square Root of {number} = {root:.5f}' 
      f'(to 5 Decimal Places).' 
      f'\nIt took {count} iterations to reach this value.')


# reference: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# reference: https://en.wikipedia.org/wiki/Newton%27s_method
# reference: https://www.youtube.com/watch?v=2158QbsunA8
# reference: https://www.w3schools.com/python/python_strings_format.asp