# This program asks the user for a number and determines if its in the range 1 through 7
# Each number the represents a day of the week.
# If the number is outside the range an error message is displayed.
# Ask the user for a number
>>>Day_number=int(input("Please enter a number: "))
>>> # Set a range
>>> if Day_number==1:
	print('The day is Monday.')
    elif Day_number==2:
        print('The day is Tuesday.')
    elif Day_number==3:
        print('The day is Wednesday.')
    elif Day_number==4:
        print('The day is Thursday.')
    elif Day_number==5:
        print('The day is Friday.')
    elif Day_number==6:
        print('The day is Saturday.')
    elif Day_number==7:
        print('The day is Sunday.')
    else:
        print(str(Day_number) + 'does not correspond with a day') 
