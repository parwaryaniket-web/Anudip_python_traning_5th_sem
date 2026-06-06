# write a program in which you have 11 players in a team and you have to print the score of each player and total the whole team score.
print("-----TEAM SCORE CALCULATOR-----")
total_players = 11# Number of players in the team
team_score = 0  # Initialize total team score
for i in range(total_players):# Loop through each player
    player_score = float(input(f"Enter the score for player {i+1}: "))  # Get player's score
    team_score += player_score  # Add player's score to total team score
print(f"Total team score: {team_score}")  # Print the total team score
# In this program, we first initialize the total number of players and the team score. We then use a loop to get the score for each player and add it to the team score. Finally, we print the total team score.
# You can run this program and input the scores for each player to see the total team score.
# python -u player.py     