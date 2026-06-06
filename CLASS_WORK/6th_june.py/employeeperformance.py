#Question 1: Employee Performance Evaluation 
#Problem Statement
#A company stores employee details in a tuple. Each employee record contains: 
#employees = ( 
#05", "Amit", 45)  
#Where: 
#• First value = Employee ID  
#• Second value = Employee Name  
#• Third value = Performance Score 
#Write a Python program to: 
#1. Display details of employees scoring 80 or above.  
#2. Count the number of employees who need improvement (score below 60).  
#3. Find the employee with the highest score.  
#4. Create a list containing the names of all employees scoring above 75.  
#5. Display the performance category for each employee:  
#o 90 and above → Excellent  
#o 75 to 89 → Good  
#o 60 to 74 → Average  
#o Below 60 → Needs Improvement 
print("---- EMPLOYEE PERFORMANCE EVALUATION ----")
employees = ( 
    ("E01", "Anuj", 92), 
    ("E02", "Rahul", 76), 
    ("E03", "Priya", 58), 
    ("E04", "Neha", 88), 
    ("E05", "Amit", 45) 
)
# 1. Employees scoring 80 or above
print("Employees scoring 80 or above:") 
for emp in employees: 
    if emp[2] >= 80: # Check if the performance score is 80 or above
        print(f"ID: {emp[0]}, Name: {emp[1]}, Score: {emp[2]}") # Print the details of the employee
# 2. Count employees who need improvement (score below 60)
improvement_count = 0
for emp in employees: 
    if emp[2] < 60: # Check if the performance score is below 60
        improvement_count += 1 # Increment the counter for employees who need improvement
print("Number of employees who need improvement:", improvement_count) # Print the count of employees who need improvement
# 3. Employee with the highest score
highest_score = -1
top_employee = None
for emp in employees:
    if emp[2] > highest_score: # Check if the current employee's score is higher than the highest score found so far
        highest_score = emp[2] # Update the highest score
        top_employee = emp # Update the top employee with the current employee's details    
print(f"Employee with the highest score: ID: {top_employee[0]}, Name: {top_employee[1]}, Score: {top_employee[2]}") # Print the details of the employee with the highest score
# 4. List of employee names scoring above 75
good_performers = []
for emp in employees:
    if emp[2] > 75: # Check if the performance score is above 75
        good_performers.append(emp[1]) # Add the employee's name to the list of good performers
print("Employees scoring above 75:", good_performers) # Print the list of employee names scoring above 75
# 5. Performance category for each employee
print("Performance category for each employee:")
for emp in employees:
    if emp[2] >= 90: # Check if the performance score is 90 or above
        category = "Excellent"
    elif emp[2] >= 75: # Check if the performance score is between 75 and 89
        category = "Good"
    elif emp[2] >= 60: # Check if the performance score is between 60 and 74
        category = "Average"
    else: # If the performance score is below 60
        category = "Needs Improvement"
    print(f"ID: {emp[0]}, Name: {emp[1]}, Score: {emp[2]}, Category: {category}") # Print the details of each employee along with their performance category

    
