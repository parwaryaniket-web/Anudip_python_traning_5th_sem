#8. ATM Simulation System 
#Initial Balance = ₹10,000 
#Display a menu repeatedly: 
#1. Check Balance 
#2. Deposit 
#3. Withdraw 
#4. Exit 
balance = 10000  # Initial balance
while True:  # Start an infinite loop
    print("\nATM Menu:")# Display the menu options
    print("1. Check Balance")# Display option to check balance
    print("2. Deposit")# Display option to deposit money
    print("3. Withdraw")# Display option to withdraw money
    print("4. Exit")# Display option to exit the program
    
    choice = input("Enter your choice (1-4): ")  # Get user's choice
    
    if choice == '1':  # Check Balance
        print(f"Your current balance is: ₹{balance}")# Display the current balance to the user
    
    elif choice == '2': # Deposit
        amount = float(input("Enter the amount to deposit: "))# Get the amount to deposit from the user
        if amount > 0:# Check if the amount is positive
            balance += amount# Add the deposited amount to the balance
            print(f"₹{amount} deposited successfully. New balance: ₹{balance}")# Display the new balance after deposit
        else:# If the amount is not positive, display an error message
            print("Invalid amount. Please enter a positive number.")# Display an error message for invalid deposit amount
    
    elif choice == '3':  # Withdraw
        amount = float(input("Enter the amount to withdraw: "))# Get the amount to withdraw from the user
        if amount > balance:# Check if the withdrawal amount is greater than the current balance
            print("Insufficient funds. Please try again.")# Display an error message for insufficient funds
        elif amount <= 0:# Check if the withdrawal amount is positive
            print("Invalid amount. Please enter a positive number.")# Display an error message for invalid withdrawal amount
        else:# If the withdrawal amount is valid and sufficient, proceed with the withdrawal
            balance -= amount# Subtract the withdrawn amount from the balance
            print(f"₹{amount} withdrawn successfully. New balance: ₹{balance}")# Display the new balance after withdrawal
    
    elif choice == '4':  # Exit
        print("Thank you for using the ATM. Goodbye!")
        break  # Exit the loop
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")# Display an error message for invalid menu choice
        
