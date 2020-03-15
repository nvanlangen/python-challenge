#Modules
import os
import csv

#Set up file path and names
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
analysispath = os.path.join('.', 'Resources', 'analysis.txt')

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
    
    #Read header and ignore
    next(csvreader)

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

#Print Results to Console
print("Financial Analysis")
print("----------------------------")

#Total Months length of the profit/loss list
print(f"Total Months: {len(profit_loss_list)}")

#Total sum of the profit/loss list
print(f"Total: ${sum(profit_loss_list)}")

#Average is sum/len of the profit/loss list
print(f"Average  Change: ${round(sum(pl_diff_list) / len(pl_diff_list),2)}")

#Greatest Increase is max of profit/loss difference list, month uses index of the max value + 1 to account for the first month being removed
print(f"Greatest Increase in Profits: {month_list[pl_diff_list.index(max(pl_diff_list))+1]} (${max(pl_diff_list)})")

#Greatest Decrease is min of profit/loss difference list, month uses index of the min value + 1 to account for the first month being removed
print(f"Greatest Decrease in Profits: {month_list[pl_diff_list.index(min(pl_diff_list))+1]} (${min(pl_diff_list)})")

#Open output file, set newline for Windows 
with open(analysispath,"w",newline='') as textfile:

    #Write lines to the file, same as was printed on the console
    textwriter = csv.writer(textfile)
    textwriter.writerow(["Financial Analysis"])
    textwriter.writerow(["----------------------------"])
    textwriter.writerow(["Total Months: " + str(len(profit_loss_list))])
    textwriter.writerow(["Total: $" + str(sum(profit_loss_list))])
    textwriter.writerow(["Average  Change: $" + str(round(sum(pl_diff_list) / len(pl_diff_list),2))])
    textwriter.writerow(["Greatest Increase in Profits: " + month_list[pl_diff_list.index(max(pl_diff_list))+1] + "($" + str(max(pl_diff_list)) + ")"])
    textwriter.writerow(["Greatest Decrease in Profits: " + month_list[pl_diff_list.index(min(pl_diff_list))+1] + "($" + str(min(pl_diff_list)) + ")"])
