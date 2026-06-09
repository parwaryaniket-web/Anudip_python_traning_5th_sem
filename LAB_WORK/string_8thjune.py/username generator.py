'''
7. Username Generator System 
Problem Statement 
A student enters: 
Rahul Sharma 
Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics.  
Sample Output 
Original Name: Rahul Sharma 
 
Generated Username: 
rahulsharma2026 
 
Username Length: 15 
 
Vowels: 5 
Consonants: 10 
 
Status: Username Generated Successfully
'''
# Username Generator System

name = input("Enter your name: ")

# Remove spaces and convert to lowercase
username = name.replace(" ", "").lower()

# Append current year
username = username + "2026"

# Keep only first 12 characters if length exceeds 12
if len(username) > 12:
    username = username[:12]

# Count vowels and consonants
vowels = 0
consonants = 0

for ch in username:
    if ch.isalpha():  # Check only letters
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Display results
print("\nOriginal Name:", name)
print("Generated Username:", username)
print("Username Length:", len(username))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Status: Username Generated Successfully")
