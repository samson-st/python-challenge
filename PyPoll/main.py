# create a script that analyzes votes and calculates the following:
# * The total number of votes cast
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.



#import modules
import os

#module for reading CSV files
import csv


election_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')

#total rows
vote_total = 0

votes_per_candidate = {}

#open up election_data
with open(election_data_csv, newline='') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #read each row of data after the header
    for row in csvreader:
        vote_total += 1
        if row[2] not in votes_per_candidate:
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1   
        
        

#output to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_total))
print("-------------------------")

for candidate, votes in votes_per_candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/vote_total) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votes_per_candidate, key=votes_per_candidate.get)

print(f"Winner: {winner}")

#output to text file

f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(vote_total))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in votes_per_candidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/vote_total) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
