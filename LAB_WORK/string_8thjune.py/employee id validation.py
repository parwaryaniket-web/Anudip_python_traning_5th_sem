'''1. Employee ID Validation and Analysis System 
Problem Statement 
A company generates employee IDs in the following format: 
EMP2026ANUJ458 
Tasks 
Write a program to: 
1. Count the number of uppercase letters.  
2. Count the number of digits.  
3. Extract the joining year.  
4. Extract the employee name.  
5. Check whether the ID follows these rules:  
o Starts with "EMP"  
o Contains exactly 4 digits for the year  
o Ends with exactly 3 digits  
6. Create a list containing all digits present in the ID.  
7. Find the sum of all digits present in the ID.  
8. Display whether the ID is valid or invalid.  
Sample Output 
Employee ID: EMP2026ANUJ458 
 
Uppercase Letters: 7 
Digits: 7 
 
Joining Year: 2026 
Employee Name: ANUJ 
 
Digit List: [2, 0, 2, 6, 4, 5, 8] 
Sum of Digits: 27 
 
ID Status: Valid'''
# Employee ID Validation and Analysis System

emp_id = "EMP2026ANUJ458"

# Print Employee ID
print("Employee ID:", emp_id)

# Count uppercase letters
uppercase_count = 0
for ch in emp_id:
    if ch.isupper():
        uppercase_count += 1

# Count digits
digit_count = 0
for ch in emp_id:
    if ch.isdigit():
        digit_count += 1

# Extract joining year (4 digits after EMP)
joining_year = emp_id[3:7]

# Extract employee name (between year and last 3 digits)
employee_name = emp_id[7:-3]

# Create a list of all digits
digit_list = []
for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

# Find sum of all digits
digit_sum = sum(digit_list)

# Check validity of ID
if (emp_id.startswith("EMP") and
    emp_id[3:7].isdigit() and
    len(emp_id[3:7]) == 4 and
    emp_id[-3:].isdigit() and
    len(emp_id[-3:]) == 3):
    status = "Valid"
else:
    status = "Invalid"

# Display results
print("\nUppercase Letters:", uppercase_count)
print("Digits:", digit_count)

print("\nJoining Year:", joining_year)
print("Employee Name:", employee_name)

print("\nDigit List:", digit_list)
print("Sum of Digits:", digit_sum)

print("\nID Status:", status)