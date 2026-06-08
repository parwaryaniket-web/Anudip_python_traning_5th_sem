'''
3. City Temperature Monitoring System 
Problem Statement 
Daily temperatures of different cities are stored as: 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).  
6. Count cities with temperature between 35°C and 40°C.  
Sample Output 
Cities Above 40°C: 
Delhi 
Jaipur 
Ahmedabad 
 
Hottest City: Ahmedabad (43°C) 
 
Coolest City: Bengaluru (28°C) 
 
Average Temperature: 36.8°C 
 
Pleasant Cities: 
['Mumbai', 'Bengaluru', 'Pune'] 
 
Cities Between 35°C and 40°C: 4
'''
# City Temperature Monitoring System

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Cities above 40°C
print("Cities Above 40°C:")
for city in temperature:
    if temperature[city] > 40:
        print(city)

# 2. Find hottest city
hottest_city = ""
highest_temp = 0

for city in temperature:
    if temperature[city] > highest_temp:
        highest_temp = temperature[city]
        hottest_city = city

print("\nHottest City:", hottest_city, "(", highest_temp, "°C )")

# 3. Find coolest city
coolest_city = ""
lowest_temp = 100

for city in temperature:
    if temperature[city] < lowest_temp:
        lowest_temp = temperature[city]
        coolest_city = city

print("Coolest City:", coolest_city, "(", lowest_temp, "°C )")

# 4. Average temperature
total = 0

for city in temperature:
    total = total + temperature[city]

average = total / len(temperature)

print("Average Temperature:", round(average, 1), "°C")

# 5. Pleasant cities (less than 35°C)
pleasant_cities = []

for city in temperature:
    if temperature[city] < 35:
        pleasant_cities.append(city)

print("Pleasant Cities:", pleasant_cities)

# 6. Count cities between 35°C and 40°C
count = 0

for city in temperature:
    if temperature[city] >= 35 and temperature[city] <= 40:
        count += 1

print("Cities Between 35°C and 40°C:", count)