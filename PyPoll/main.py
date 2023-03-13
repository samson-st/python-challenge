# create a script that analyzes votes and calculates the following:
# * The total number of votes cast
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.



#import modules
#https://docs.python.org/3/library/collections.html
import os
import csv
import collections
from collections import Counter

#input file for data analysis
election_data = os.path.join("Resources/", "election_data.csv")
#output file
text_path = os.path.join("analysis", "results.txt")

#declare variables
chosen_candidates = []
votes_per_candidate = []

# Open and read csv
with open(election_data, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    #read through rows
    for row in csv_reader:

        chosen_candidates.append(row[2])

    sorted_candidates = sorted(chosen_candidates)
    arrange_candidates = sorted_candidates

    #count votes per candidate
    candidate_count = Counter (arrange_candidates)
    


