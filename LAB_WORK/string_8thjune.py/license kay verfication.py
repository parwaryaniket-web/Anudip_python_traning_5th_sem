'''
9. License Key Verification System 
Problem Statement 
A software license key is entered: 
ABCD-EFGH-IJKL-MNOP 
Tasks 
Write a program to: 
1. Verify there are exactly 4 groups.  
2. Verify each group contains exactly 4 characters.  
3. Count total letters.  
4. Count vowels.  
5. Remove hyphens and display the merged key.  
6. Create a list containing all groups.  
7. Display whether the key format is valid.  
Sample Output 
License Key: 
ABCD-EFGH-IJKL-MNOP 
 
Groups: 
['ABCD', 'EFGH', 'IJKL', 'MNOP'] 
 
Number of Groups: 4 
 
Total Letters: 16 
Total Vowels: 4 
 
Merged Key: 
ABCDEFGHIJKLMNOP 
 
License Key Status: Valid
'''
# License Key Verification System

# Input license key
license_key = "ABCD-EFGH-IJKL-MNOP"

# Display original key
print("License Key:")
print(license_key)

# Split the key into groups using '-'
groups = license_key.split("-")

# Display groups
print("\nGroups:")
print(groups)

# Count number of groups
num_groups = len(groups)
print("\nNumber of Groups:", num_groups)

# Remove hyphens and join all groups
merged_key = "".join(groups)

# Count total letters
total_letters = len(merged_key)

# Count vowels
vowels = "AEIOUaeiou"
vowel_count = 0

for ch in merged_key:
    if ch in vowels:
        vowel_count += 1

# Check validity
valid = True

# Condition 1: Exactly 4 groups
if num_groups != 4:
    valid = False

# Condition 2: Every group must have 4 characters
for group in groups:
    if len(group) != 4:
        valid = False

# Display results
print("\nTotal Letters:", total_letters)
print("Total Vowels:", vowel_count)

print("\nMerged Key:")
print(merged_key)

# Display status
if valid:
    print("\nLicense Key Status: Valid")
else:
    print("\nLicense Key Status: Invalid")