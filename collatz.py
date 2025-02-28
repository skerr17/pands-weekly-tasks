# collatz.py
# Week 4's weekly task 
# This program prompts the user to input any positive interger
# And outputs the successive values of the following calculation.
# at each step the next value by taking the current value and, if it even, divide by two
# but if it is odd, multiply it by three and add one
# the program will end if the current value is one 
# Author: Stephen Kerr


# prompt the user for a number 
starting_positive_integer = int(input('Please Enter a Positive Integer: '))

# Save the initial value inputed by the user 
starting_positive_integer_initial = starting_positive_integer

# initial the list of successive values 
successive_values = []

# in a while loop check if that number is a even or odd number and apply the above rules until it is equal to 1
while starting_positive_integer != 1:
    # check if it is even 
    if (starting_positive_integer % 2) == 0:
        # value is even divide by 2
        starting_positive_integer = starting_positive_integer // 2
    else:
        # value is not even therefore odd multiply by 3 and add 1
        starting_positive_integer = starting_positive_integer * 3 + 1
    # add the value to the list of successive values
    successive_values.append(starting_positive_integer)


# print the successive values
print(f'You Entered {starting_positive_integer_initial},' 
      f'\nWhich took {len(successive_values)} steps to reach 1.' 
      f'\nThe Successive Values where: {successive_values}')
