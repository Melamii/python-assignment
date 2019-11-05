from random import randint
player=input('rock(r),paper(p), or scissors(s)?')
print(player, 'vs')
computer=randint(1,3)
print(computer)
if computer==1:
	computer_choice='r'
elif computer==2:
	computer_choice='p'
else:
	computer_choice='s'
#print(computer)
if player=='r' and computer_choice==2:
	print('Computer wins because paper covers rock')
elif player=='s' and computer_choice==1:
	print('Computer wins because rock smashes scissors')
elif player=='p' and computer_choice==3:
	print('Computer wins because scissors cuts paper')
elif computer_choice==1 and player=='p':
	print('Player wins because paper covers rock')
elif computer_choice==3 and player=='r':
	print('Player wins because rock smashes scissors')
elif computer_choice==2 and player=='s':
	print('Player wins because scissors cuts paper')
else:
	if player==computer_choice:
		print('Its a tie')
Play_again=input('would you like to play again?')
if Play_again==y:
	print(player)
else:
	print('Game Over')