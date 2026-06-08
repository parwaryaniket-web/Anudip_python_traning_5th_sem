'''
5. Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) is stored as: 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate total units consumed.  
5. Create lists:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).  
Sample Output 
Houses Consuming More Than 400 Units: 
House103 
House106 
House110 
 
Highest Consumption: 
House110 (600 units) 
 
Lowest Consumption: 
House109 (145 units) 
 
Total Units Consumed: 3220 
 
Low Consumption: 
['House102', 'House105', 'House109'] 
 
Medium Consumption: 
['House101', 'House104', 'House107', 'House108'] 
 
High Consumption: 
['House103', 'House106', 'House110'] 
 
Eligible for Energy-Saving Campaign: 5
'''
# Smart Electricity Billing System

units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")

for house in units:
    if units[house] > 400:
        print(house)

# 2. Find highest-consuming house
highest_house = ""
highest_units = 0

for house in units:
    if units[house] > highest_units:
        highest_units = units[house]
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, "(", highest_units, "units )")

# 3. Find lowest-consuming house
lowest_house = ""
lowest_units = 1000

for house in units:
    if units[house] < lowest_units:
        lowest_units = units[house]
        lowest_house = house

print("\nLowest Consumption:")
print(lowest_house, "(", lowest_units, "units )")

# 4. Calculate total units consumed
total_units = 0

for house in units:
    total_units = total_units + units[house]

print("\nTotal Units Consumed:", total_units)

# 5. Create lists for consumption categories

# Empty lists
low_consumption = []
medium_consumption = []
high_consumption = []

for house in units:

    # Less than 200 units
    if units[house] < 200:
        low_consumption.append(house)

    # Between 200 and 400 units
    elif units[house] <= 400:
        medium_consumption.append(house)

    # Greater than 400 units
    else:
        high_consumption.append(house)

print("\nLow Consumption:")
print(low_consumption)

print("\nMedium Consumption:")
print(medium_consumption)

print("\nHigh Consumption:")
print(high_consumption)

# 6. Count houses consuming more than 300 units
count = 0

for house in units:
    if units[house] > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)