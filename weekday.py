# weekday.py
# This program outputs whether or not today is a weekday,
# or a weekend day. Using the datetime module to get the current date and time.
# Author: Stephen Kerr

# import datetime module
import datetime

# workout what day of the week it is 
current_date = datetime.datetime.now()

# Use the striftime() method from the datetime to format the day of the week
current_day = current_date.strftime("%A")

# create the weekday days of the week to check against if today is weekday or not
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Print out the formatted date
print(f'Today is {current_date.strftime("%x")}\nWhich is a ...')

# work out if this day of the week is a weekday or weekend and print
if current_day in weekdays:
    # check if the day is a weekday
    print(f'{current_day}, sorry to say this but today is a weekday.')
else:
    # must be a weekend
    print(f'{current_day} is a weekend day. Lets celebrate!!')


# References: 
# Found out how to use the datatime module from W3Bschools - Here https://www.w3schools.com/python/python_datetime.asp
# Found this article on how to check if an element exists in a list - Here - https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/