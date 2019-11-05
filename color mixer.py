Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##Chiemela Amaefule
    ##Python 1 (10657), Mon, 11.00, Central Campus
    ##Chapter: 3
    ##Exercise: 7
    ##Assignment Name: Color Mixing 
    ##Due Date: 10/12/19
>>> # This program asks the user to enter two primary colors
>>> # If the color is not a primary color, an error message will be displayed
>>> # Otherwise it will display the resulting primary color
>>> # Ask the user to enter primary colors
>>> color1=input("Please enter a primary color: ")
Please enter a primary color: yellow
>>> color2=input("Please enter another primary color: ")
Please enter another primary color: blue
>>> # Create conditions to make sure the user enters a primary color
>>> if color1==red and color2==yellow or color1==yellow and color2==red:
>>>     print("The color you get is orange.")
>>> elif color1==red and color2==blue or color1==blue and color2==red:
>>> 	print("The color you get is purple.")
>>> elif color1==yellow and color2==blue or color1==blue and color2==yellow:
>>> 	print("The color you get is green.")
>>> else:
>>> 	print("The color you entered is not a primary color.")
