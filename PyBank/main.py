#Modules
import os
import csv
import sys

#Set up input file path and name
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#Define lists used
month_list = []
profit_loss_list = []
pl_diff_list=[]

#Set initial previous profit/loss to 0
pl_diff = 0

#Open input file
with open(csvpath,"r") as csvfile:

    #Set up file reader with , delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read header and save in variable
    pl_header = next(csvreader)

    #Read each row in file
    for row in csvreader:
        #Append Month to the list
        month_list.append(row[0])

        #Append Profit/Loss to the list
        profit_loss_list.append(int(row[1]))

        #Calculate the difference and append to the list
        pl_diff_list.append(int(row[1]) - pl_diff)

        #Set the previous profit/loss to current row
        pl_diff = int(row[1])

#Remove first value from the profit/loss difference list as there is no difference for the first month
pl_diff_list.pop(0)

#Function to write output, parameter is file or terminal
def write_output(output_mode):
    if output_mode=="file":
        orig_stdout = sys.stdout
        analysispath = os.path.join('.', 'Resources', 'analysis.txt')
        analysis_file = open(analysispath,"w")
        sys.stdout = analysis_file

    print("Financial Analysis")
    print("----------------------------")

    #Total Months length of the month list
    print(f"Total Months: {len(month_list)}")

    #Total sum of the profit/loss list
    print(f"Total: ${sum(profit_loss_list)}")

    #Average is sum/len of the profit/loss list
    print(f"Average  Change: ${round(sum(pl_diff_list) / len(pl_diff_list),2)}")

    #Greatest Increase is max of profit/loss difference list, month uses index of the max value + 1 to account for the first month being removed
    print(f"Greatest Increase in Profits: {month_list[pl_diff_list.index(max(pl_diff_list))+1]} (${max(pl_diff_list)})")

    #Greatest Decrease is min of profit/loss difference list, month uses index of the min value + 1 to account for the first month being removed
    print(f"Greatest Decrease in Profits: {month_list[pl_diff_list.index(min(pl_diff_list))+1]} (${min(pl_diff_list)})")

    #Close the file and reset the stdout to the terminal
    if output_mode=="file":
        analysis_file.close()
        sys.stdout = orig_stdout

#Call function to write the file and again for the terminal
write_output("file")
write_output("terminal")
