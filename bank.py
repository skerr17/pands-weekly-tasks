# bank.py
# This program prompts the user and read in two money amounts (in cents).
# Adds the two amounts 
# Prints out the answer in ahuman readable format with a euro sign and a decimal point between the euro and cent of the amount
# author: Stephen Kerr

# Added context prompt for the user so they know what the program is doing
print("This program will prompt you for two amounts of money in cents add them together and present the Euro value to you.")
amount1 = int(input("Please enter the first amount (in cents): "))
amount2 = int(input("Please enter the second amount (in cents): "))
print("The total amount is €{:0.2f}".format((amount1 + amount2) / 100)) # Seen the way to show 2 decimals on w3bschool.com
