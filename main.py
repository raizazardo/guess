#importar as bodegas
from art import logo, vs
from game_data import data
import random
from replit import clear


def format_data(account):
	"""format the data into a printable format"""
	account_name = account["name"]
	account_desc = account["description"]
	account_country = account["country"]
	return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer (guess, a_followers, b_followers): 
	"""take the users guess and follower counts and returns if they got it right"""
	if a_followers > b_followers:
		return guess == "a" #when is evaluated, is guess equal to a, then it will return true or false. 
	else: 
		return guess == "b"
#display art
print (logo)
score = 0 
game_should_continue = True
account_b = random.choice(data)
#make the game a loop b

while game_should_continue:
#generate a random account from the game data
#making the account at position b become the position a 
	
	account_a = account_b
	account_b = random.choice(data)
	
	while account_a == account_b:
		account_b = random.choice(data)
	print (f"Compare A: {format_data(account_a)} ")
	print (vs)
	print (f"Against B: {format_data(account_b)} ")
	guess = input ("Which of them have more followers? Type 'a' for the first one and 'b' for the second one: ").lower()
	
	#check if the user is correct
	##get follower count of each account
	a_followers_count = account_a["follower_count"]
	b_followers_count = account_b["follower_count"]
	
	is_correct = check_answer(guess, a_followers_count, b_followers_count)

	#clear the screen between rows
	print(logo)
	clear()
	
	#score keeping
	#give user feedback
	if is_correct:
		score += 1  
		print(f"You're right! Your current score is:  {score}")
		
	else: 
		game_should_continue = False
		print(f"Sorry, that's wrong. Final score: {score}")





