'''
3. Chat Message Analytics 
Problem Statement 
A chat application stores a message: 
Python is awesome and Python is easy to learn 
Tasks 
Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants.  
Sample Output 
Message: 
Python is awesome and Python is easy to learn 
 
Total Characters: 45 
Total Words: 8 
 
Longest Word: awesome 
Shortest Word: is 
 
Occurrences of Python: 2 
 
Words Longer Than 4 Characters: 
['Python', 'awesome', 'Python', 'learn'] 
 
Vowels: 16 
Consonants: 22
'''
# Chat Message Analytics

# Store the message in a string variable
message = "Python is awesome and Python is easy to learn"

# Display the original message
print("Message:")
print(message)

# 1. Count total characters (including spaces)
print("\nTotal Characters:", len(message))

# Convert message into a list of words
words = message.split()

# 2. Count total words
print("Total Words:", len(words))

# 3. Find the longest word
longest_word = max(words, key=len)
print("\nLongest Word:", longest_word)

# 4. Find the shortest word
shortest_word = min(words, key=len)
print("Shortest Word:", shortest_word)

# 5. Count how many times "Python" appears
python_count = words.count("Python")
print("\nOccurrences of Python:", python_count)

# 6. Create a list of words having more than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

print("\nWords Longer Than 4 Characters:")
print(long_words)

# 7. Display all words starting with a vowel
print("\nWords Starting With a Vowel:")

for word in words:
    if word[0].lower() in "aeiou":
        print(word)

# 8. Count vowels and consonants
vowels = 0
consonants = 0

for ch in message.lower():

    # Check if character is a letter
    if ch.isalpha():

        # Count vowels
        if ch in "aeiou":
            vowels += 1

        # Count consonants
        else:
            consonants += 1

print("\nVowels:", vowels)
print("Consonants:", consonants)
