import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
    
        candidate_name = row[2]

        if candidate_name not in candidate_options:
    
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] +=1

        for candidate_name in candidate_votes:

            votes = candidate_votes[candidate_name] 

            vote_percentage = float(votes) / float(total_votes) * 100
        
            if (votes > winning_count) and (vote_percentage > winning_percentage):

                winning_count = votes

                winning_percentage = vote_percentage

                winning_candidate = candidate_name

            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
            print(winning_candidate_summary)    

       

