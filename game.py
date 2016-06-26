from random import randint
def start():
	print("Hello and welcome to this guessing game! \nStart guessing, it's a number between 1 and 1000...")
	correct_number = randint(1,5) #correct_number=100
	number=input() # number='200'
	count=1

	while number != correct_number: # n=0,correct=100
		if number == 'quit':
			print('**** The game was interrupted')
			return None
		elif type(number) is not int:
			print('Stupid, only number is allowed')
			number = input()
			count = count + 1
		elif number > correct_number and number < 1000:
			print('Guess is too high!')
			number = input() #32
			count = count + 1

		elif number < correct_number:
			print('Guess is too low!')
			number = input() #0
			count = count + 1
		elif number < 1 or number > 1000:
			print("Stupid guess! I won't count that...")
			number = input() #100
			count = count + 1

		

	print '**** CORRECT!\nYou guessed the correct number in', count, 'guesses'
	print('Please enter your name:') 
	input()
	print('Do you want to play again?(y/n)')
	answer = input()
	if answer == 'n':
		print('**** The game is over')
	elif answer == 'y':
		start()


	


