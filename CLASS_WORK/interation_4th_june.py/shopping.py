#Write a program that continuously accepts item prices and calculates the total bill amount. The program should stop accepting prices when the user enters 0. 
total_bill = 0.0  # Initialize total bill amount
while True:  # Start an infinite loop
    price = float(input("Enter the price of the item (or 0 to stop): "))  # Get item price from user
    if price == 0:  # Check if the user wants to stop entering prices
        break  # Exit the loop if 0 is entered
    total_bill += price  # Add the item price to the total bill 
print("Total bill amount: $", total_bill)  # Display the total bill amount

