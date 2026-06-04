#Write a program that accepts marks from the user and continues asking for marks until the entered score is 40 or more. 
#Display a congratulatory message once the student passes the assessment. 
while True:  # Start an infinite loop
    marks = int(input("Enter the marks: "))  # Get marks from the user and convert it to an integer
    if marks >= 40:  # Check if the marks are 40 or more
        print("Congratulations! You passed the assessment!")
        break  # Exit the loop if the student passes
    else:
        print("Marks are less than 40. Please try again.")  # Prompt the user to try again if the marks are less than 40        
# python -u "CLASS_WORK\onlineexam.py"  
    