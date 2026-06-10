'''
5. City Population & Development Dashboard 
Problem Statement 
The government wants to analyze city data. 
Store details of at least 30 cities. 
Example Structure 
cities = { 
    "Delhi": { 
        "population": 32000000, 
        "area": 1484, 
        "literacy": 89 
    } 
} 
Requirements 
1. Display all city details.  
2. Find the most populated city.  
3. Find the least populated city.  
4. Calculate average population.  
5. Display cities with literacy rate above 90%.  
6. Display cities with literacy below average.  
7. Calculate population density.  
8. Find city with highest density.  
9. Categorize cities:  
o Small  
o Medium  
o Large  
10. Create a development-priority list.  
11. Generate separate dictionaries for:  
o High Literacy Cities  
o Low Literacy Cities  
12. Generate a national summary report.  
Challenge 
Rank all cities based on population density.
'''
# City Population & Development Dashboard

# Dictionary storing city details
cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 92},
    "Chennai": {"population": 11000000, "area": 426, "literacy": 91},
    "Kolkata": {"population": 15000000, "area": 205, "literacy": 88},
    "Bangalore": {"population": 13000000, "area": 709, "literacy": 90}
}

# Add more cities up to 30 in the same format

# --------------------------------------------------
# 1. Display All City Details
# --------------------------------------------------
print("ALL CITY DETAILS")

for city, details in cities.items():
    print(city, details)

# --------------------------------------------------
# 2. Find Most Populated City
# --------------------------------------------------
max_pop = 0
max_city = ""

for city, details in cities.items():
    if details["population"] > max_pop:
        max_pop = details["population"]
        max_city = city

print("\nMost Populated City =", max_city)

# --------------------------------------------------
# 3. Find Least Populated City
# --------------------------------------------------
min_pop = 999999999
min_city = ""

for city, details in cities.items():
    if details["population"] < min_pop:
        min_pop = details["population"]
        min_city = city

print("Least Populated City =", min_city)

# --------------------------------------------------
# 4. Calculate Average Population
# --------------------------------------------------
total_population = 0

for details in cities.values():
    total_population += details["population"]

avg_population = total_population / len(cities)

print("Average Population =", avg_population)

# --------------------------------------------------
# 5. Cities with Literacy Above 90%
# --------------------------------------------------
print("\nCities with Literacy Above 90%")

for city, details in cities.items():
    if details["literacy"] > 90:
        print(city)

# --------------------------------------------------
# 6. Cities with Literacy Below Average
# --------------------------------------------------
total_literacy = 0

for details in cities.values():
    total_literacy += details["literacy"]

avg_literacy = total_literacy / len(cities)

print("\nCities with Literacy Below Average")

for city, details in cities.items():
    if details["literacy"] < avg_literacy:
        print(city)

# --------------------------------------------------
# 7. Calculate Population Density
# Density = Population / Area
# --------------------------------------------------
print("\nPopulation Density")

for city, details in cities.items():
    density = details["population"] / details["area"]
    print(city, "=", round(density, 2))

# --------------------------------------------------
# 8. Find City with Highest Density
# --------------------------------------------------
highest_density = 0
dense_city = ""

for city, details in cities.items():
    density = details["population"] / details["area"]

    if density > highest_density:
        highest_density = density
        dense_city = city

print("\nHighest Density City =", dense_city)

# --------------------------------------------------
# 9. Categorize Cities
# --------------------------------------------------
print("\nCITY CATEGORIES")

for city, details in cities.items():

    if details["population"] > 20000000:
        print(city, "- Large City")

    elif details["population"] > 10000000:
        print(city, "- Medium City")

    else:
        print(city, "- Small City")

# --------------------------------------------------
# 10. Development Priority List
# Literacy below 90
# --------------------------------------------------
print("\nDevelopment Priority Cities")

for city, details in cities.items():
    if details["literacy"] < 90:
        print(city)

# --------------------------------------------------
# 11. High Literacy and Low Literacy Dictionaries
# --------------------------------------------------
high_literacy = {}
low_literacy = {}

for city, details in cities.items():

    if details["literacy"] >= 90:
        high_literacy[city] = details

    else:
        low_literacy[city] = details

print("\nHigh Literacy Cities")
print(high_literacy)

print("\nLow Literacy Cities")
print(low_literacy)

# --------------------------------------------------
# 12. National Summary Report
# --------------------------------------------------
print("\n===== NATIONAL SUMMARY REPORT =====")

print("Total Cities =", len(cities))
print("Total Population =", total_population)
print("Average Population =", avg_population)
print("Average Literacy =", avg_literacy)
print("Most Populated City =", max_city)
print("Least Populated City =", min_city)
print("Highest Density City =", dense_city)

# --------------------------------------------------
# Challenge : Rank Cities by Population Density
# --------------------------------------------------
print("\nCITY DENSITY RANKING")

density_list = []

for city, details in cities.items():
    density = details["population"] / details["area"]
    density_list.append((density, city))

density_list.sort(reverse=True)

for rank, item in enumerate(density_list, start=1):
    print(rank, "-", item[1], "-", round(item[0], 2))