'''
 Employee Performance Dashboard 
Problem Statement 
Employee performance scores are stored as: 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Create separate lists:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60)  
Sample Output 
Employees Scoring Above 80: 
EMP101 
EMP104 
EMP105 
EMP107 
 
Top Performer: EMP105 (97) 
 
Employees Needing Improvement: 3 
 
Average Score: 71.3 
 
Excellent: 
['EMP101', 'EMP105'] 
 
Good: 
['EMP102', 'EMP104', 'EMP107'] 
 
Average: 
['EMP108', 'EMP110'] 
 
Poor: 
['EMP103', 'EMP106', 'EMP109']
'''
# Employee Performance Dashboard

# Dictionary storing employee IDs and their scores
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():  # Get employee ID and score
    if score > 80:  # Check if score is greater than 80
        print(emp)

# 2. Count employees needing improvement (score less than 60)
improvement_count = 0  # Counter starts from 0

for score in performance.values():  # Loop through all scores
    if score < 60:  # Check if score is below 60
        improvement_count += 1  # Increase counter by 1

print("\nEmployees Needing Improvement:", improvement_count)

# 3. Find the top performer
top_emp = ""      # Store employee ID
top_score = 0     # Store highest score

for emp, score in performance.items():  # Loop through dictionary
    if score > top_score:  # If current score is highest
        top_score = score  # Update highest score
        top_emp = emp      # Update employee ID

print("\nTop Performer:", top_emp, "(", top_score, ")", sep="")

# 4. Calculate average performance score
total_score = sum(performance.values())  # Add all scores
total_employees = len(performance)       # Count employees
average = total_score / total_employees  # Average formula

print("\nAverage Score:", round(average, 1))

# 5. Create separate lists
excellent = []  # Score >= 90
good = []       # Score 75 to 89
average_list = []  # Score 60 to 74
poor = []       # Score below 60

for emp, score in performance.items():  # Loop through employees

    if score >= 90:
        excellent.append(emp)

    elif score >= 75:
        good.append(emp)

    elif score >= 60:
        average_list.append(emp)

    else:
        poor.append(emp)

# Display all categories
print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average_list)

print("\nPoor:")
print(poor)