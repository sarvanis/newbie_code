import os
print " Welcome to Rock Paper Scissors game \n"
print "Valid inputs \n rock \npaper\n scissor\n" 
print "enter choice of player 1\n"
player1= str(raw_input())
os.system('cls' if os.name == 'nt' else 'clear')
print "enter choice of player 2\n"
player2= str(raw_input())

if( player1=='rock'):
 
	if(player2=='rock'):
		print "tie between players \n play again"
	elif(player2=='scissor'):
		print " player 1 won the game"
	else:
		print " player2 won the game"

elif(player1=='paper'):
	if(player2=='paper'):
		print "tie between players \n play again"
	elif(player2=='rock'):
		print "player 1 won the game"
	else:
		print "player 2 won the game"
elif(player1=='scissor'):
	if(player2=='scissor'):
		print"tie between players"
	elif(player2=='rock'):
		print "player2 won the game"
	else:
		print "player1 won the game"
else:
	print"enter a valid input"
