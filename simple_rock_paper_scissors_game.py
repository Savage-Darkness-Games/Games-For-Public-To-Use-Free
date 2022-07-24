from random import randint

# define variables
player_score = 0
computer_score = 0
bgame_running = "True"
sgame_continue = "y"
sgame_exit = "n"
other_choice = 0
choice = 0
player_score == int(player_score)
computer_score == int(computer_score)
#start game loop
print(f"Welcome to a simple Rock, Paper, Scissors game. As we are just starting, the score is Player: {player_score} versus Computer: {computer_score}")
while bgame_running == "True":
	player_score = int(player_score)
	computer_score == int(computer_score)
	other_choice = randint(1, 3)
	other_choice = int(other_choice)
	choice = input(f"Please pick between: rock: 1, paper: 2, or scissors: 3? - Must be an integer: ")
	choice = int(choice)
	if choice == other_choice:
		print(f"Player and Computer chose the same thing: Draw!")
		player_score = int(player_score)
		computer_score = int(computer_score)
		print(f"Score is currently Player: {player_score} Computer: {computer_score}.")
	elif choice == 1: # rock
		if other_choice == 2: # paper
			print(f"Computer Wins!")
			computer_score = computer_score + 1
			player_score = int(player_score)
			computer_score = int(computer_score)
			print(f"Score is currently Player: {player_score} Computer: {computer_score}.")
		elif other_choice == 3: # scissors
			print(f"Player Wins!")
			player_score = player_score + 1
			player_score = int(player_score)
			computer_score = int(computer_score)
			print(f"Score is currently Player: {player_score} Computer: {computer_score} .")
	elif choice == 2: # paper
		if other_choice == 3: # scissors
			print(f"Computer Wins!")
			computer_score = computer_score + 1
			player_score = int(player_score)
			computer_score = int(computer_score)
			print(f"Score is currently Player: {player_score} Computer: {computer_score} .")
		elif other_choice == 1: # rock
			print(f"Player Wins!")
			player_score = player_score + 1
			player_score = int(player_score)
			computer_score = int(computer_score)
			print(f"Score is currently Player: {player_score} Computer: {computer_score} .")
	elif choice == 3: # scissors
		if other_choice == 2: # rock
			print(f"Computer Wins!")
			computer_score = computer_score + 1
			player_score = int(player_score)
			computer_score = int(computer_score)
			print(f"Score is currently Player: {player_score} Computer: {computer_score} .")
		elif other_choice == 1: #paper
			print(f"Player_Wins")
			player_score = player_score + 1
			player_score = int(player_score)
			computer_score = int(computer_score)
			print(f"Score is currently Player: {player_score} Computer: {computer_score} .")
	else:
		print(f"You picked an incorrect format, computer wins by default!")
		computer_score = computer_score + 1
		player_score = int(player_score)
		computer_score = int(computer_score)
		print(f"Score is currently Player: {player_score} Computer: {computer_score} .")
	scommand = input(f"Do you want to play again, (y/n)? ")
	scommand = str(scommand)
	if scommand.lower() == sgame_continue:
		bgame_running = "True"
	elif scommand.lower() == sgame_exit:
		bgame_running = "False"
	else:
		print(f"Incorrect answer, exiting due you your stupidity!")
		bgame_running = "False"
