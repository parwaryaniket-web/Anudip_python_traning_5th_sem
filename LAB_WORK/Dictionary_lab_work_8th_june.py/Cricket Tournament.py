'''
. Cricket Tournament Statistics 
Problem Statement 
Runs scored by players in a tournament: 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks 
1. Display players scoring more than 500 runs.  
2. Find the Orange Cap winner.  
3. Find the lowest scorer.  
4. Calculate total runs scored.  
5. Create a list of players scoring below 400.  
6. Count players scoring between 400 and 600 runs.  
Sample Output 
Players Scoring More Than 500 Runs: 
Virat 
Rohit 
Gill 
Pant 
 
Orange Cap Winner: Gill (698) 
 
Lowest Scorer: Hardik (278) 
 
Total Tournament Runs: 4657 
 
Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja'] 
 
Players Between 400 and 600 Runs: 5
'''
# Cricket Tournament Statistics

runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")

for player in runs:
    if runs[player] > 500:
        print(player)

# 2. Find Orange Cap Winner (highest scorer)
orange_cap = ""
highest_runs = 0

for player in runs:
    if runs[player] > highest_runs:
        highest_runs = runs[player]
        orange_cap = player

print("\nOrange Cap Winner:", orange_cap, "(", highest_runs, ")")

# 3. Find Lowest Scorer
lowest_player = ""
lowest_runs = 1000

for player in runs:
    if runs[player] < lowest_runs:
        lowest_runs = runs[player]
        lowest_player = player

print("\nLowest Scorer:", lowest_player, "(", lowest_runs, ")")

# 4. Calculate Total Runs
total_runs = 0

for player in runs:
    total_runs = total_runs + runs[player]

print("\nTotal Tournament Runs:", total_runs)

# 5. Create list of players scoring below 400
below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400:")
print(below_400)

# 6. Count players scoring between 400 and 600
count = 0

for player in runs:
    if runs[player] >= 400 and runs[player] <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs:", count)