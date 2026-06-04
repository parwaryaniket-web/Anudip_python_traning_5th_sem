#4. Number Guessing Game 
#Generate a secret number between 1 and 50. 
#Allow the user to keep guessing until the correct number is found. 


import random


secret_number = random.randint(1, 50)
guess = None

while guess != secret_number:
    guess = int(input("Guess the number (between 1 and 50): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number: {secret_number}")          
