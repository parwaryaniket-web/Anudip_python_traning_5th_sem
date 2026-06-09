'''
5. Product Review Analyzer 
Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.  
 
Sample Output 
Total Words: 8 
 
Word Frequencies: 
This -> 1 
product -> 1 
is -> 1 
excellent -> 3 
and -> 1 
very -> 1 
useful -> 1 
 
Most Frequent Word: excellent 
 
Words Appearing Once: 
['This', 'product', 'is', 'and', 'very', 'useful'] 
 
Unique Words: 
['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']
'''
# Product Review Analyzer

# Store the review in a string
review = "This product is excellent excellent excellent and very useful"

# Convert review into a list of words
words = review.split()

# 1. Count total words
print("Total Words:", len(words))

# 2. Create a dictionary for word frequencies
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord Frequencies:")
for word, count in freq.items():
    print(word, "->", count)

# 3. Find the most frequently used word
most_word = ""
max_count = 0

for word, count in freq.items():
    if count > max_count:
        max_count = count
        most_word = word

print("\nMost Frequent Word:", most_word)

# 4. Find words appearing only once
once_words = []

for word, count in freq.items():
    if count == 1:
        once_words.append(word)

print("\nWords Appearing Once:")
print(once_words)

# 5. Count words having more than 5 characters
count_long = 0

for word in words:
    if len(word) > 5:
        count_long += 1

print("\nWords More Than 5 Characters:", count_long)

# 6. Display words in reverse order
print("\nWords in Reverse Order:")
for word in words[::-1]:
    print(word, end=" ")

# 7. Create a list of unique words
unique_words = list(freq.keys())

print("\n\nUnique Words:")
print(unique_words)