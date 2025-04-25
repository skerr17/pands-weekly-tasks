# bank.py
# Week 2's Weekly Task
# This program prompts the user and read in two money amounts (in cents).
# Adds the two amounts 
# Prints out the answer in a human readable format with a euro sign and a decimal point between the euro and cent of the amount
# Author: Stephen Kerr

# Added context prompt for the user so they know what the program is doing
print("This program will prompt you for two amounts of money in cents,"
        " add them together and present the Euro value to you.")

while True: 
    try:
        # Prompt the user for the first amount in cents
        first_amount_cents = int(input("Please enter the first amount (in cents): "))
        break  # Exit the loop if input is valid move to the next amount
    except ValueError: # If the user enters a non-integer value, print an error message and prompt again
        print("Invalid input. Please enter a valid integer for the amount in cents.")

while True: 
    try:
        # Prompt the user for the second amount in cents
        second_amount_cents = int(input("Please enter the second amount (in cents): "))
        break  # Exit the loop if input is valid move to the next amount
    except ValueError: # If the user enters a non-integer value, print an error message and prompt again
        print("Invalid input. Please enter a valid integer for the amount in cents.")


# caclcuate the total amount in euros
total_amount_euros = (first_amount_cents + second_amount_cents) / 100

# Final Print of the total amount in euros
print(f"The total amount is €{total_amount_euros:0.2f}") # Seen the way to show 2 decimals on w3bschool.com
