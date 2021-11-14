#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

import csv
import os

# Assign a variable to load a file from A path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.

# Create a filename variable to save a file to a path to
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)