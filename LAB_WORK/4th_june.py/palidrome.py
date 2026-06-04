#9. Palindrome and Reverse Number Checker 
#Accept a number from the user. 
#Display
# Whether it is a Palindrome  
# Whether it is a Reverse Number.
number = input("Enter a number: ")  
# Check for Palindrome
if number == number[::-1]:      
    print(f"{number} is a Palindrome.")
else:
    print(f"{number} is not a Palindrome.")
# Check for Reverse Number
reverse_number = number[::-1]
if number == reverse_number:
    print(f"{number} is a Reverse Number.")
else:
    print(f"{number} is not a Reverse Number.")

    