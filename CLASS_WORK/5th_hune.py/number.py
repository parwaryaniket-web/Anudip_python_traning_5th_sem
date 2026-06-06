# write a program to creat a list of 20 number given by the user and ask user to input any other number ,remove all the duplicate number by user list 
print("-----NUMBER LIST AND DUPLICATE REMOVER-----")
number_list = []  # Initialize an empty list to store numbers   
# Get 20 numbers from the user and add them to the list
for i in range(20):# Loop to get 20 numbers from the user
    # Get a number from the user and add it to the list
    num = float(input(f"Enter number {i+1}: "))  # Get a number from the user
    # Add the number to the list
    number_list.append(num)  # Add the number to the list
duplicate_num = float(input("Enter another number to check for duplicates: "))  # Get a number to check for duplicates
# Remove all occurrences of the duplicate number from the list
number_list = [num for num in number_list if num != duplicate_num]  # Create a new list excluding the duplicate number
print("List after removing duplicates:", number_list)  # Print the list after removing duplicates
#finding the frequency of the duplicate number in the original list
frequency = number_list.count(duplicate_num)  # Count the frequency of the duplicate number in the original list
print(f"The number {duplicate_num} was removed {frequency} times from the list.")   # Print the frequency of the duplicate number removed from the list               
