#ATM Transaction History 
#Problem Statement 
# customer's transactions are stored as: 
#transactions = [5000, -2000, 3000, -1000, -500, 7000] 
#Positive values represent deposits and negative values represent withdrawals. 
#Write a program to: 
#1. Calculate the current balance.  
#2. Count total deposits and withdrawals.  
#3. Find the largest deposit and largest withdrawal.  
#4. Create separate lists for deposits and withdrawals.  
#Expected Output 
#Current Balance: 11500 
#Deposits: [5000, 3000, 7000] 
#Largest Withdrawal: -2000 
#Largest Deposit: 7000
print("-----ATM TRANSACTION HISTORY ANALYZER-----") 
transactions = [5000, -2000, 3000, -1000, -500, 7000]  # List of transactions
current_balance = sum(transactions)  # Calculate current balance by summing all transactions
total_deposits = sum(t for t in transactions if t > 0)  # Calculate total deposits
total_withdrawals = sum(t for t in transactions if t < 0)  # Calculate total withdrawals
largest_deposit = max((t for t in transactions if t > 0), default=0)  # Find largest deposit
largest_withdrawal = min((t for t in transactions if t < 0), default=0)  # Find largest withdrawal
# Find largest withdrawal
deposits = [t for t in transactions if t > 0]  # Create list of deposits
withdrawals = [t for t in transactions if t < 0]  # Create list of withdrawals  
print(f"Current Balance: ₹{current_balance}")  # Print current balance          
