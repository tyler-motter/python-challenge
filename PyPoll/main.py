#import dependecies
import os
import csv

#setting the file
csvpath = os.path.join("Resources", "election_data.csv")

#declaring variables
int_votes = 0
winner_votes = 0
candidates = []
candidate_names = []
percent_votes = []
number_votes = []

#opening the file, setting delimiter, and skipping headers
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #for loop adding each vote each loop, identifying unique names
    #else is adding votes for unique candidates
    for row in csvreader:
        int_votes += 1
        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            number_votes.append(1)
        else:
            candidate_list = candidate_names.index(row[2])
            number_votes[candidate_list] += 1

    #calculating percentage of votes
    for i in range(len(number_votes)):
        percent_votes.append(number_votes[i] / int_votes)
    
    #calculate winner
    for i in range(len(number_votes)):
        if number_votes[i] > winner_votes:
            winner_vote = number_votes[i]
            winner = candidate_names[i]
    
    #creating text file
    results = os.path.join("Resources", "results.txt")
    with open(results, 'w') as textfile:
        textfile.write(f"Election Results \n"
                       f"-----------------\n"
                       f"Total Votes: {int_votes} \n"
                       f"------------------\n")
        
        for i in range(len(candidate_names)):
            textfile.write(f"{candidate_names[i]}: {(percent_votes[i] * 100)} {(number_votes[i])}\n")
        textfile.write(f"-----------------\n"
                       f"Winner: {winner} \n"
                       f"------------------\n")
    #printing text file
    with open(results, 'r') as analysis:
        result_display = analysis.read()
        print(result_display)