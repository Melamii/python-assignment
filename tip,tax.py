Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Ask the customer for the price of their meal
>>>  meal_price=float(input('How much was your meal? '))
# Calculate the percent of tip to be paid
>>> TIP_PERCENT=18/100
>>> tip=float(meal_price*TIP_PERCENT)
>>> print(tip)
#Calculate trhe percent of the tax
>>> TAX_PERCENT=7/100
>>> tax=float(TAX_PERCENT*meal_price)
>>> print(tax)
#Sum the tax, tip, and the meal price to get the total paid by the customer
>>> total_paid=meal_price+tax+tip
>>> print(total_paid)

How much was your meal? 30
tip=5.3999999999999995
tax=2.1
total_paid=37.5
