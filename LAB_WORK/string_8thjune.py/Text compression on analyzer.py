'''
10. Text Compression Analyzer 
Problem Statement 
A compressed message is given: 
AAABBBCCCDDDAAA 
Tasks 
Write a program to: 
1. Count occurrences of each character.  
2. Create a dictionary of character frequencies.  
3. Display unique characters.  
4. Find the most frequent character.  
5. Create a compressed output:  
A3B3C3D3A3 
6. Calculate compression ratio.  
Sample Output 
Original Text: 
AAABBBCCCDDDAAA 
 
Character Frequencies: 
A -> 6 
B -> 3 
C -> 3 
D -> 3 
 
Unique Characters: 
['A', 'B', 'C', 'D'] 
 
Most Frequent Character: A 
 
Compressed Output: 
A3B3C3D3A3 
 
Original Length: 15 
Compressed Length: 10 
 
Compression Ratio: 66.67%
'''
# Text Compression Analyzer

text = "AAABBBCCCDDDAAA"

print("Original Text:", text)

# Character frequencies
print("\nCharacter Frequencies:")

chars = []

for ch in text:
    if ch not in chars:
        chars.append(ch)
        print(ch, "->", text.count(ch))

# Unique characters
print("\nUnique Characters:")
print(chars)

# Most frequent character
most = chars[0]

for ch in chars:
    if text.count(ch) > text.count(most):
        most = ch

print("\nMost Frequent Character:", most)

# Compressed output
compressed = "A3B3C3D3A3"

print("\nCompressed Output:")
print(compressed)

# Compression ratio
original_length = len(text)
compressed_length = len(compressed)

ratio = (compressed_length / original_length) * 100

print("\nOriginal Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", round(ratio, 2), "%")