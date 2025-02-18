# accounts.py
# Week 3's Weekly Task
# This program reads a Bank Account Number and for security reason only displays the last 4 digits
# replacing the digital before the last 4 with X characters
# Author: Stephen Kerr
'''
# Assumptions:
 1. For the extra requirement is that the bank account number must be at least 4 digits long
 2. The bank account number can be any length over 4 digits (no limit)
'''
# prompt the user for their bank account number
bank_account_number = str(input("Please enter your bank account number: "))


# configure the output to display the last 4 digits of the account number
# and replace the rest with X characters
bank_account_number_lenght = len(bank_account_number)

# check if the account number is less than 4 digits
if bank_account_number_lenght < 4:
    print("The bank account number must be at least 4 digits long")
else:
    # get the last 4 digits of the account number
    last_4_digits = bank_account_number[-4:]

    # calculate the number of x characters to be displayed
    x_characters = bank_account_number_lenght - 4

# print the account number in the new format
print(f"The last 4 digits of your bank account number are: {x_characters * 'X'}{last_4_digits}")