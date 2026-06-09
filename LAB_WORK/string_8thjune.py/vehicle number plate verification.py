'''
4. Vehicle Number Plate Verification 
Problem Statement 
A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid.  
Sample Output 
Vehicle Number: MH12AB4589 
State Code: MH 
District Code: 12 
Series: AB 
Vehicle Number: 4589 
 
Total Letters: 4 
Total Digits: 6 
 
Vehicle Number Status: Valid 
'''
print("---- VEHICLE NUMBER PLATE VERIFICATION ----")

plate = "MH12AB4589"

# Extract details
state_code = plate[:2]
district_code = plate[2:4]
series = plate[4:6]
vehicle_number = plate[6:]

# Count letters and digits
letters = 0
digits = 0

for ch in plate:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

# Verify number plate format
if (plate[:2].isalpha() and
    plate[2:4].isdigit() and
    plate[4:6].isalpha() and
    plate[6:].isdigit() and
    len(plate) == 10):
    status = "Valid"
else:
    status = "Invalid"

# Display output
print("Vehicle Number:", plate)
print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)

print("\nTotal Letters:", letters)
print("Total Digits:", digits)

print("\nVehicle Number Status:", status)