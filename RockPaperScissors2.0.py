

# This program selects a random number from 1 through 3
# Each number represents Rock, paper and Scissors respectively
# The user enters their choice and the computers choice is displayed
# The winner is determined based on the rules below
# rock smashes scissors, scissors cuts paper, and paper covers rock.
# If the choices are the same, then the game repeats.


# Import the random library
from random import randint

print('Welcome to the rock paper scissors game.')
# Declare the variable for a tie 
Draw =True
# Create a while loop to test the condition
while Draw==True:
    print('')
    print('Press 1 for Rock')
    print('Press 2 for Paper')
    print('Press 3 for Scissors')
    player=int(input('What is your choice? '))
    

    # Give the computer it's selection of numbers
    ComputerInput=randint(1,3)
    print(computer)
    if computer==1:
	computer_choice='Rock'
    elif computer==2:
	computer_choice='Paper'
    elif computer==3:
	computer_choice='Scissors'

    if (player=='Rock') and (computer_choice=='Rock'):
        Draw=False
        print('Computer wins because paper covers rock')
    if (player=='Scissors') and (computer_choice=='Rock'):
        Draw=False
        print('Computer wins because rock smashes scissors')
    if (player=='Paper') and (computer_choice=='Scissors'):
        Draw=False
        print('Computer wins because scissors cuts paper')
    if (computer_choice=='Rock') and (player=='Paper'):
        Draw=False
        print('Player wins because paper covers rock')
    if (computer_choice=='Scissors') and (player=='Rock'):
        Draw=False
        print('Player wins because rock smashes scissors')
    if (computer_choice=='Paper') and (player=='Scissors'):
        Draw=False
        print('Player wins because scissors cuts paper')
    if (player==computer_choice:
        Draw= True
        print('Its a tie')
