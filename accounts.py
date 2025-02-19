# accounts.py
# Week 3's Weekly Task
# This program reads a Bank Account Number and for security reason only displays the last 4 digits
# replacing the digital before the last 4 with X characters
# Author: Stephen Kerr
'''
# Assumptions:
 1. For the extra requirement is that the bank account number must be more than 4 digits long. (minimum 4 digits)
 2. The bank account number character lenght limit is 20.  (Maximum 20 digits)
 3. The user will enter a valid bank account number between the 4 digit min and 20 didgit max.
 4. The bank account number will be a string.
'''
# prompt the user for their bank account number
bank_account_number = str(input("Please enter your bank account number: "))


# configure the output to display the last 4 digits of the account number
# and replace the rest with X characters
bank_account_number_lenght = len(bank_account_number)

# check if the account number is less than 4 digits and no more than 20 digits
if bank_account_number_lenght < 4:
    print("The bank account number must be at least 4 digits long")

elif bank_account_number_lenght >= 20:
    # check the account number is not more than 20 digits
    print("The bank account number must be less than 20 digits long")

else:
    # get the last 4 digits of the account number
    last_4_digits = bank_account_number[-4:]

    # calculate the number of x characters to be displayed
    x_characters = bank_account_number_lenght - 4

    # print the account number in the new format
    print(f"The last 4 digits of your bank account number are: {x_characters * 'X'}{last_4_digits}")