#consecutive digit number 
#problem statement
#Accept a number and check whether every digit is exactly 1 greater than its previous digit. 
print("-----CONSECUTIVE DIGIT NUMBER CHECKER-----")
number = input("Enter a number: ")  # Accept a number from the user             
is_consecutive = True  # Initialize a flag to check if the digits are consecutive
for i in range(1, len(number)):  # Loop through the digits of the number
    if int(number[i]) != int(number[i - 1]) + 1:  # Check if the current digit is not exactly 1 greater than the previous digit
        is_consecutive = False  # If not, set the flag to False
        break  # Exit the loop since we found a non-consecutive pair
if is_consecutive:  # Check the flag after the loop
    print("The digits are consecutive.")  # If the flag is True, print that the digits are consecutive  
else:    print("The digits are not consecutive.")  # If the flag is False, print that the digits are not consecutive
