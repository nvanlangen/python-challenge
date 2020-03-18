#Modules
import os
import csv
import sys

#Set up input file path and name
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

#Define lists used
candidate_list = []
candidate_votes_list = []

#Open file
with open(csvpath,"r") as csvfile:

    #Set up file reader with comma delimiter
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

#Function to write output, parameter is file or terminal
def write_results(output_mode):
    if output_mode=="file":
        #Write output to a file
        orig_stdout = sys.stdout
        resultspath = os.path.join('.', 'Resources', 'results.txt')
        results_file = open(resultspath,"w")
        sys.stdout = results_file
        
    #Get the sum of votes for all candidates
    total_votes = sum(candidate_votes_list)

    #Set index for loop to 0
    candidate_index=0

    #Print Election Results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    #Calculate percentage and display the Candidate, Percentage and Number of Votes
    for candidate in candidate_list:
        print(f"{candidate}: {candidate_votes_list[candidate_index] / total_votes *100:.3f}% ({candidate_votes_list[candidate_index]})")
        candidate_index += 1
    print("-------------------------")
    #Identify the Winner by finding max number of votes and using the index to get the name
    print(f"Winner: {candidate_list[candidate_votes_list.index(max(candidate_votes_list))]}")
    print("-------------------------")

    #Close the file and reset the stdout to the terminal
    if output_mode=="file":
        results_file.close()
        sys.stdout = orig_stdout

#Call function to write the file and again for the terminal
write_results("file")
write_results("terminal")
