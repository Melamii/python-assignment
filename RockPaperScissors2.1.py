# Chiemela Amaefule
# Python(10657), Mon,Wed, 11.00, Central
# Chapter: 5
# Exercise: 21
# Due date: 10/27/2019

# This program selects a random number from 1 through 3
# Each number represents Rock, paper and Scissors respectively
# The user enters their choice and the computers choice is displayed
# The winner is determined based on the rules below
# rock smashes scissors, scissors cuts paper, and paper covers rock.
# If the choices are the same, then the game repeats.

# Import the random library
import random

print("Welcome to the Rock Paper Scissors Game.")

# Create the test variable
Draw = False

# Create the a while loop to declare all the options
# Give the player the options they have to enter
while Draw == False:
    print("")
    print("Press 1 for Rock.")
    print("Press 2 for Paper.")
    print("Press 3 for Scissors.")

    PlayerInput = int(input("What is your move?"))
    ComputerInput = random.randrange(1,3)

    # Create all the possible option for the player and the computer as well as the result

    if (PlayerInput == 1) and (ComputerInput == 1):
        Draw = False
        print("It's a draw, you both chose Rock")

    if (PlayerInput == 2) and (ComputerInput == 1):
        Draw == True
        print("You win because the computer played Rock.")

    if (PlayerInput == 3) and (ComputerInput == 1):
        Draw == True
        print("You lose because the computer played Rock.")
        
    if (PlayerInput == 1) and (ComputerInput == 2):
        Draw = True
        print("You lose because the computer played Paper.")
        
    if (PlayerInput == 2) and (ComputerInput == 2):
        Draw == False
        print("It's a draw because the computer played Paper.")

    if (PlayerInput == 3) and (ComputerInput == 2):
        Draw == True
        print("You win because the computer played Paper.")
        
    if (PlayerInput == 1) and (ComputerInput == 3):
        Draw = True
        print("You because the computer played Scissors.")
        
    if (PlayerInput == 2) and (ComputerInput == 3):
        Draw == True
        print("You lose because the computer played Scissors!")

    if (PlayerInput == 3) and (ComputerInput == 3):
        Draw == False
        print("It's a draw because the computer played Scissors!")