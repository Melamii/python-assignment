# Chiemela Amaefule
# Python(10657), Mon, Wed, 11.00, Central
# Chapter: 4
# Exercise: 7
# Due Date: None

# This program calculates the amount of money a person would earn over time if,
# the person earned a penny the first day, 2 pennies the next day, 
# and the salary continued to double each day

# Ask the user for the number of days
NumberOfDays=int(input('How many days of salary do you want to check? (numbers only)'))

# Declare the salary on the first day
Salary=0.01

# Create the table with its headings 
print()
print('Days\tSalary')
print('............')

# Create the loop and display the results
for Days in range(1, NumberOfDays +1):
    Salary*=2
    print(Days,'\t','$', format(Salary,',.2f'))