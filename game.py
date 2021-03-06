from random import randint

high_score = dict()
f = open('results.txt','w')
f.write('Current highscore list\n')
f.write('Name    Guesses\n')

def start():
	print("Hello and welcome to this guessing game! \nStart guessing, it's a number between 1 and 1000...")
	
	correct_number = randint(1,1000) 
	number=input() 
	count=1

	while number != correct_number: 
		
		if number == 'quit':
			print('**** The game was interrupted')
			return None
		elif type(number) is not int:
			number = input('Stupid, only number is allowed\n')
		elif number > correct_number and number < 1000:
			number = input('Guess is too high!\n')
		elif number < correct_number:
			number = input('Guess is too low!\n')
		elif number < 1 or number > 1000:
			number = input("Stupid guess! I won't count that...\n") 
		
		count = count + 1
   	
   	print '**** CORRECT!\nYou guessed the correct number in', count, 'guesses'
	name = input('Please enter your name:\n')
	high_score[name] = count
	answer = input('Do you want to play again?(y/n)\n')
	if answer == 'n':
		print('**** The game is over')
		f.close()
	elif answer == 'y':	
		print('Current highscore list:')
		print('Name    Guesses')
		print name, '    ', high_score[name]
		
		for name in high_score:
			f.write(name + '    ' + str(high_score[name]))
			f.write('\n')

		start()


	


