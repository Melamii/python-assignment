# Chiemela Amaefule
# Python(10657), Mon, Wed, 11.00am, Central
# Chapter 5
# Assignment name: Building a Menu Driven Program using Modules and Functions
# Due date: 11/10/19

# This program allows the user to choose various
# geometry calculations from a menu. this program
# imports the grahics_and_geometry module
import graphics_and_geometry


# Constants for the menu choices
SQUARE_DRAW_CHOICE=1
CIRCLE_DRAW_CHOICE=2
LINE_DRAW_CHOICE=3
CIRCLE_AREA_CHOICE=4
CIRCLE_CIRCUMFERENCE_CHOICE=5
RECTANGLE_AREA_CHOICE=6
RECTANGLE_PERIMETER_CHOICE=7
QUIT_CHOICE=8

# The main function
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice
    choice=0

    while choice != QUIT_CHOICE:
        # Display the menu
        display_menu()

        # Get the user's choice.
        choice= int(input('Enter your choice: '))

        # Perform the selected action
        if choice == SQUARE_DRAW_CHOICE:
            x= int(input("Enter the square's x coordinate: "))
            y=int(input("Enter the square's y coordinate: "))
            width=float(input("Enter the square's width: "))
            color=input('What color would you like the square to be? ')
            print('This is what your square looks like', square_draw(x,y,width,color))
        elif choice == CIRCLE_DRAW_CHOICE:
            x= int(input("Enter the circle's x coordinate: "))
            y=int(input("Enter the circle's y coordinate: "))
            radius=float(input("Enter the circle's radius: "))
            color=input('What color would you like the circle to be? ')
            print('This is what your circle looks like', circle_draw(x,y, radius, color))
        elif choice == LINE_DRAW_CHOICE:
            startX= int(input("Enter the line's initial x coordinate: "))
            startY=int(input("Enter the line's initial y coordinate: "))
            endX= int(input("Enter the line's final x coordinate: "))
            endY=int(input("Enter the line's final y coordinate: "))
            color=input('What color would you like the line to be? ')
            print('This is your line', line_draw(startX, startY, endX, endY, color))
        elif choice == CIRCLE_AREA_CHOICE:
            radius=float(input("Enter the circle's radius: "))
            print('The area of the circle is', circle_area(radius))
        elif choice== CIRCLE_CIRCUMFERENCE_CHOICE:
            radius=float(input("Enter the circle's radius: "))
            print('The circumference of your circle is', circle_circumference(radius))
        elif choice==RECTANGLE_AREA_CHOICE:
            width=float(input("Enter the width of the rectangle: "))
            length=float(input("Enter the length of the rectangle: "))
            print('The area of your rectangle is', rectangle_area(width, length))
        elif choice== RECTANGLE_PERIMETER_CHOICE:
            width=float(input("Enter the width of the rectangle: "))
            length=float(input("Enter the length of the rectangle: "))
            print('The perimeter of your rectangle is', rectangle_perimeter(width, length))
        elif choice== QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
# The display menu function displays the menu
def display_menu():
    print('MENU')
    print('1) Draw a square')
    print('2) Draw a circle')
    print('3) Draw a line')
    print('4) Area of a circle')
    print('5) Circumference of a circle')
    print('6) Area of a rectangle')
    print('7) Perimeter of a rectangle')
    print('8) Quit')

# Call the main function
main()
