#Write a program that repeatedly asks the user to guess the number and displays a success message when the correct number is entered
correct_number = 7  # Set the correct number
while True:  # Start an infinite loop
    user_guess = int(input("Guess the number: "))  # Get user's guess and convert it to an integer
    if user_guess == correct_number:  # Check if the guess is correct
        print("Congratulations! You guessed the correct number!")
        break  # Exit the loop if the guess is correct
    else:
        print("Wrong guess. Please try again.")  # Prompt the user to try again if the guess is incorrect   
# python -u "CLASS_WORK\gussthegame.py" 