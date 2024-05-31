print("pypoll")


import os
import csv
from pathlib import Path 

# Assign file location with the pathlib library
csv_file_path = Path("Resources", "election_data.csv")

# Declare Variables 
total_votes = 0 
candidate_options = []
candidate_votes = {}
vote_percentage = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open csv in default read mode with context manager
with open(csv_file_path, encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable called total_votes
        total_votes +=1

        candidate_name = row[2]


        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print a the summary of the analysis
output_file = Path("Election_Results_Summary.txt")
with open(output_file,"w") as analysis:
# Print the summary table
    election_results = (
        f"Election Results\n"
        f"----------------------------\n"
        f"Voter Output: {total_votes}\n"
        f"----------------------------\n"
    )
    analysis.write(election_results)
    

    print(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/ float(total_votes) *100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage 

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        analysis.write(voter_output)
        print(voter_output)
    winning_summary = (
        f"Winner : {winning_candidate}\n"
        f"Winner percentage: {winning_percentage:.3f}%\n"
    )
    print(winning_summary)

# write the analysis
    analysis.write(winning_summary)
    
