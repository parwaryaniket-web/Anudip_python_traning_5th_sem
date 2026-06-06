#. Consecutive Number Detector 
#Problem Statement 
#Given a list: 
#numbers = [4, 5, 6, 10, 11, 15, 16, 17] 
#Write a program to find all pairs of consecutive numbers.
print("-----CONSECUTIVE NUMBER DETECTOR-----")
numbers = [4, 5, 6, 10, 11, 15, 16, 17]  # List of numbers
consecutive_pairs = []  # Initialize an empty list to store pairs of consecutive numbers    # Loop through the list of numbers and check for consecutive pair
for i in range(len(numbers) - 1):  # Loop through the list of numbers
    if numbers[i] + 1 == numbers[i + 1]:  # Check if the current number and the next number are consecutive
        consecutive_pairs.append((numbers[i], numbers[i + 1]))  # If they are consecutive, add the pair to the list
print("Pairs of consecutive numbers:", consecutive_pairs)  # Print the pairs of consecutive numbers




    