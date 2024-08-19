#import modules
import os
import csv

# Variables
votes = 0  # To count the total votes
candidates = {}  # To store vote counts per candidate

# Setting path for the csv file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Loop for total votes
    for row in csvreader:
        votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# Printing the results
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(votes))
print("----------------------------")

for candidate, vote_count in candidates.items():
    vote_percentage = (vote_count / votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}%   ({vote_count})")
    
print("----------------------------") 

# Determining the winner
winner = max(candidates, key=candidates.get)

# Print winner
print(f"Winner: {winner}")
