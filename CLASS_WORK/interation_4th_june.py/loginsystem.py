#login system 
#Write a program that keeps asking the user to enter the password until the correct password is provided. 
correct_password = "password123"  # Set the correct password
while True:         
    user_password = input("Enter the password: ")
    if user_password == correct_password:
        print("Password is correct!")
        break
    else:
        print("Incorrect password. Please try again.")  
# python -u "CLASS_WORK\loginsystem.py"
