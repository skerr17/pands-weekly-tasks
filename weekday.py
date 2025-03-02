# This program outputs whether or not today is a weekday. 
# Author: Stephen Kerr

# import datetime module
import datetime

# workout what day of the week it is 
current_date = datetime.datetime.now()

# Use the striftime() method from the dateimte to format the day of the week
current_day_of_the_week = current_date.strftime("%A")

# create the weekday days of the week to check against if today is weekday or not
weekdays_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Print out the formated date
print(f'Today is {current_date.strftime("%x")}\nWhich is a ...')

# work out if this day of the week is a weekday or weekend and print
if current_day_of_the_week in weekdays_list:
    # check if the day is a weekday
    print(f'{current_day_of_the_week}, sorry to say this but today is a weekday.')
else:
    # must be a weekend
    print(f'{current_day_of_the_week} is a weekend day. Lets celebrate!!')


