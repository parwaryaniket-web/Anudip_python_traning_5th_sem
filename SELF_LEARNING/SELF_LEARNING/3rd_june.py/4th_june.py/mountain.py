#A Mountain Number is a number whose digits first increase and then decrease. 
#For example, 12321 is a Mountain Number because the digits first increase (1 < 2 < 3) and then decrease (3 > 2 > 1).
#Write a program to check if a given number is a Mountain Number or not.        
print("-----MOUNTAIN NUMBER CHECKER-----")
number = input("Enter a number: ")  # Accept a number from the user
is_mountain = False  # Initialize a flag to check if the number is a Mountain Number
increasing = True  # Initialize a flag to track if the digits are currently increasing
for i in range(1, len(number)):  # Loop through the digits of the number
    if increasing:  # If we are in the increasing phase
        if int(number[i]) > int(number[i - 1]):  # Check if the current digit is greater than the previous digit
            continue  # If it is, continue checking the next digits
        elif int(number[i]) < int(number[i - 1]):  # Check if the current digit is less than the previous digit
            increasing = False  # If it is, switch to the decreasing phase
        else:
            break  # If the digits are equal, it's not a Mountain Number, exit the loop
    else:  # If we are in the decreasing phase
        if int(number[i]) < int(number[i - 1]):  # Check if the current digit is less than the previous digit
            continue  # If it is, continue checking the next digits
        else:
            break  # If the digits are not decreasing, exit the loop

if is_mountain:
    print(f"{number} is a Mountain Number.")
else:
    print(f"{number} is not a Mountain Number.") 
    