'''
4. Cricket Tournament Analytics System 
Problem Statement 
Store statistics of at least 30 cricket players. 
Example Structure 
players = { 
    "Virat": { 
        "runs": 645, 
        "matches": 12, 
        "wickets": 0 
    } 
} 
Requirements 
1. Display all player statistics.  
2. Find highest run scorer.  
3. Find lowest run scorer.  
4. Calculate average runs.  
5. Find player with maximum wickets.  
6. Find all-rounders (runs > 300 and wickets > 5).  
7. Display players scoring above average.  
8. Create categories:  
o Star Performer  
o Good Performer  
o Average Performer  
o Poor Performer  
9. Generate team statistics.  
10. Display top 5 batsmen.  
11. Display top 5 bowlers.  
12. Create a separate dictionary for award winners.  
Challenge 
Generate a tournament report.
'''
# Cricket Tournament Analytics System

# Dictionary storing player statistics
players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 520, "matches": 12, "wickets": 1},
    "Hardik": {"runs": 350, "matches": 12, "wickets": 8},
    "Jadeja": {"runs": 310, "matches": 12, "wickets": 12},
    "Bumrah": {"runs": 50, "matches": 12, "wickets": 18}
}

# Add more players up to 30 in the same format

# --------------------------------------------------
# 1. Display All Player Statistics
# --------------------------------------------------
print("ALL PLAYER STATISTICS")

for player, details in players.items():
    print(player, details)

# --------------------------------------------------
# 2. Find Highest Run Scorer
# --------------------------------------------------
highest_runs = 0
highest_player = ""

for player, details in players.items():
    if details["runs"] > highest_runs:
        highest_runs = details["runs"]
        highest_player = player

print("\nHighest Run Scorer =", highest_player)

# --------------------------------------------------
# 3. Find Lowest Run Scorer
# --------------------------------------------------
lowest_runs = 99999
lowest_player = ""

for player, details in players.items():
    if details["runs"] < lowest_runs:
        lowest_runs = details["runs"]
        lowest_player = player

print("Lowest Run Scorer =", lowest_player)

# --------------------------------------------------
# 4. Calculate Average Runs
# --------------------------------------------------
total_runs = 0

for details in players.values():
    total_runs = total_runs + details["runs"]

average_runs = total_runs / len(players)

print("Average Runs =", average_runs)

# --------------------------------------------------
# 5. Find Player with Maximum Wickets
# --------------------------------------------------
max_wickets = 0
best_bowler = ""

for player, details in players.items():
    if details["wickets"] > max_wickets:
        max_wickets = details["wickets"]
        best_bowler = player

print("Maximum Wickets =", best_bowler)

# --------------------------------------------------
# 6. Find All-Rounders
# Runs > 300 and Wickets > 5
# --------------------------------------------------
print("\nALL-ROUNDERS")

for player, details in players.items():
    if details["runs"] > 300 and details["wickets"] > 5:
        print(player)

# --------------------------------------------------
# 7. Display Players Scoring Above Average
# --------------------------------------------------
print("\nPLAYERS ABOVE AVERAGE RUNS")

for player, details in players.items():
    if details["runs"] > average_runs:
        print(player)

# --------------------------------------------------
# 8. Create Performance Categories
# --------------------------------------------------
print("\nPERFORMANCE CATEGORY")

for player, details in players.items():

    if details["runs"] > 500:
        print(player, "- Star Performer")

    elif details["runs"] > 300:
        print(player, "- Good Performer")

    elif details["runs"] > 100:
        print(player, "- Average Performer")

    else:
        print(player, "- Poor Performer")

# --------------------------------------------------
# 9. Generate Team Statistics
# --------------------------------------------------
total_wickets = 0

for details in players.values():
    total_wickets = total_wickets + details["wickets"]

print("\nTEAM STATISTICS")
print("Total Players =", len(players))
print("Total Runs =", total_runs)
print("Total Wickets =", total_wickets)

# --------------------------------------------------
# 10. Display Top 5 Batsmen
# --------------------------------------------------
print("\nTOP 5 BATSMEN")

sorted_batsmen = sorted(players.items(),
                        key=lambda x: x[1]["runs"],
                        reverse=True)

for player, details in sorted_batsmen[:5]:
    print(player, details["runs"])

# --------------------------------------------------
# 11. Display Top 5 Bowlers
# --------------------------------------------------
print("\nTOP 5 BOWLERS")

sorted_bowlers = sorted(players.items(),
                        key=lambda x: x[1]["wickets"],
                        reverse=True)

for player, details in sorted_bowlers[:5]:
    print(player, details["wickets"])

# --------------------------------------------------
# 12. Create Award Winners Dictionary
# --------------------------------------------------
award_winners = {
    "Best Batsman": highest_player,
    "Best Bowler": best_bowler
}

print("\nAWARD WINNERS")
print(award_winners)

# --------------------------------------------------
# Challenge : Tournament Report
# --------------------------------------------------
print("\n===== TOURNAMENT REPORT =====")

print("Total Players =", len(players))
print("Total Runs Scored =", total_runs)
print("Total Wickets Taken =", total_wickets)
print("Average Runs =", average_runs)
print("Highest Run Scorer =", highest_player)
print("Best Bowler =", best_bowler)

print("\nAward Winners")
print(award_winners)