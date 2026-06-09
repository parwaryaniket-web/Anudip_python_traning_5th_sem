'''
2. Password Strength Analyzer 
Problem Statement 
A user enters a password. 
Python@2026! 
Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately.  
Sample Output 
Password: Python@2026! 
 
Uppercase Letters: 1 
Lowercase Letters: 5 
Digits: 4 
Special Characters: 2 
 
Digits Found: ['2', '0', '2', '6'] 
Special Characters Found: ['@', '!'] 
 
Password Strength: Strong 
'''
# Password Strength Analyzer

# User password
password = "Python@2026!"

# Counters
uppercase = 0
lowercase = 0
digits = 0
special = 0

# Lists to store digits and special characters
digit_list = []
special_list = []

# Check each character in the password
for ch in password:

    # Count uppercase letters
    if ch.isupper():
        uppercase += 1

    # Count lowercase letters
    elif ch.islower():
        lowercase += 1

    # Count digits
    elif ch.isdigit():
        digits += 1
        digit_list.append(ch)   # Store digit separately

    # Count special characters
    else:
        special += 1
        special_list.append(ch) # Store special character separately

# Check password strength
if (len(password) >= 8 and
    uppercase >= 1 and
    lowercase >= 1 and
    digits >= 1 and
    special >= 1):
    strength = "Strong"

elif len(password) >= 6:
    strength = "Medium"

else:
    strength = "Weak"

# Display results
print("Password:", password)

print("\nUppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Digits:", digits)
print("Special Characters:", special)

print("\nDigits Found:", digit_list)
print("Special Characters Found:", special_list)

print("\nPassword Strength:", strength)