#Write a program that repeatedly asks the user to enter a PIN until the correct PIN is entered. 
correct_pin = "1234"  # Set the correct PIN
while True:             
    user_pin = input("Enter the PIN: ")
    if user_pin == correct_pin:
        print("PIN is correct!")
        break
    else:
        print("Incorrect PIN. Please try again.")   
# python -u "LAB_WORK\pin_Verification.py"                              