#Armstrong
#Accept a number from the user and check whether it is an Armstrong Number. 
number = int(input("Enter a number: "))# Get the number from the user
num_str = str(number)# Convert the number to a string to easily iterate through its digits
num_digits = len(num_str)# Get the number of digits in the number
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)# Calculate the sum of each digit raised to the power of the number of digits
if sum_of_powers == number:# Check if the calculated sum is equal to the original number
    print(f"{number} is an Armstrong number.")# If they are equal, it is an Armstrong number
else:# If they are not equal, it is not an Armstrong number
    print(f"{number} is not an Armstrong number.")  # You can run this program and input any number to check if it is an Armstrong number or not.
    