#Modules
import os
import csv

#Set up file path and names
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
resultspath = os.path.join('.', 'Resources', 'results.txt')

#Define lists used
candidate_list = []
candidate_votes_list = []

#Open file
with open(csvpath,"r") as csvfile:

    #Set up file reader with , delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read header and save in variable
    election_header = next(csvreader)

    #Read each row in file
    for row in csvreader: 
        #Check if Candidate has already been added to the list
        if row[2] in candidate_list:
            #Candidate is in list, increment the vote count
            candidate_votes_list[candidate_list.index(row[2])] += 1
        else:
            #Candidate is not in the list, add to the candidate list and begin the vote count at 1
            candidate_list.append(row[2])
            candidate_votes_list.append(1)

#Get the sum of votes for all candidates
total_votes = sum(candidate_votes_list)

#Set index for loop to 0
candidate_index=0

#Print Election Results to console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#Calculate percentage and display the Candidate, Percentage and Numbr of Votes
for candidate in candidate_list:
    print(f"{candidate}: {candidate_votes_list[candidate_index] / total_votes *100:.3f}% ({candidate_votes_list[candidate_index]})")
    candidate_index += 1
print("-------------------------")
#Identify the Winner by finding max number of votes and using the index to get the name
print(f"Winner: {candidate_list[candidate_votes_list.index(max(candidate_votes_list))]}")
print("-------------------------")

#Repeat above to write to a text file
candidate_index=0
#Open output file
with open(resultspath,"w") as results_file:
    results_file.write("Election Results\n")
    results_file.write("-------------------------\n")
    results_file.write(f"Total Votes: {total_votes}\n")
    results_file.write("-------------------------\n")
    for candidate in candidate_list:
        results_file.write(f"{candidate}: {candidate_votes_list[candidate_index] / total_votes *100:.3f}% ({candidate_votes_list[candidate_index]})\n")
        candidate_index += 1
    results_file.write("-------------------------\n")
    results_file.write(f"Winner: {candidate_list[candidate_votes_list.index(max(candidate_votes_list))]}\n")
    results_file.write("-------------------------\n")
    results_file.close()
