#8. ATM Simulation System 
#Initial Balance = ₹10,000 
#Display a menu repeatedly: 
#1. Check Balance 
#2. Deposit 
#3. Withdraw 
#4. Exit 
balance = 10000  # Initial balance
while True:  # Start an infinite loop
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")  # Get user's choice
    
    if choice == '1':  # Check Balance
        print(f"Your current balance is: ₹{balance}")
    
    elif choice == '2':  # Deposit
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{balance}")
        else:
            print("Invalid amount. Please enter a positive number.")
    
    elif choice == '3':  # Withdraw
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds. Please try again.")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully. New balance: ₹{balance}")
    
    elif choice == '4':  # Exit
        print("Thank you for using the ATM. Goodbye!")
        break  # Exit the loop
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        
