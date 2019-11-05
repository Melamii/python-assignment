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
print(computer)
if player=='r' and computer=='p':
	print('Computer wins because paper covers rock')
elif player=='s' and computer=='r':
	print('Computer wins because rock smashes scissors')
elif player=='p' and computer=='s':
	print('Computer wins because scissors cuts paper')
elif computer=='r' and player=='p':
	print('Player wins because paper covers rock')
elif computer=='s' and player=='r':
	print('Player wins because rock smashes scissors')
elif computer=='p' and player=='s':
	print('Player wins because scissors cuts paper')
else:
	if player==computer:
		print('Its a tie')
Play_again=input('would you like to play again?')
if Play_again==y:
	print(player)
else:
	print('Game Over')