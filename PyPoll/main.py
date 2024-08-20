#import modules
import os
import csv

# Variables
votes = 0 
candidates = {} 

# setting path
csvpath = os.path.join("C:/Users/kiley/OneDrive/Desktop/Module Challenges/Module 3 Challenge/python-challenge/PyPoll/Resources/election_data.csv")

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

# Exporting results to a text file
output_dir = os.path.join("C:\\Users\\kiley\\OneDrive\\Desktop\\Module Challenges\\Module 3 Challenge\\python-challenge\\PyPoll\\analysis")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, "analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("----------------------------\n")
    txtfile.write("Total Votes: " + str(votes) + "\n")
    txtfile.write("----------------------------\n")
    for candidate, vote_count in candidates.items():
        vote_percentage = (vote_count / votes) * 100
        txtfile.write(f"{candidate}: {vote_percentage:.3f}%   ({vote_count})\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Winner: {winner}\n")