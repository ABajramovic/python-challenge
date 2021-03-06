# PyBank
import os
import csv

# Read data from the Resources folder
file_to_load = "C:/Users/bajraax/Desktop/python-challenge/PyBank/Resources/budget_data.csv

with open(file_to_load) as csvfile:
csvreader = csv.reader(csvfile, delimiter=",") csv_header = next(csvfile)
print(f"csv Header: {csv_header}")

# Declare Variables 
Delta = []
Greatest_Increase_Date = "" 
Greatest_Decrease_Date = ""
Months = []
Plus_Minus = [

# Loop through the rows of *.csv 
for row in csvreader:
Months.append(row[0])
Plus_Minus.append(int(row[1]))

#Output
print(f"	") 
print(f"Financial Analysis for Pybank")
print(f"	") 
print(f"Total Months: ", len(Months)) 
print(f"Total P&L: $", sum(Plus_Minus))


for i in range(1, len(Plus_Minus)):
# Find average change between months
Delta.append(Plus_Minus[i] - Plus_Minus[i-1])

# Find average of values
Average_Change = sum(Delta) / len(Delta)

# Greatest increase in profits (date and amount) over the entire period
Greatest_Increase = max(Delta)
Greatest_Increase_Date = str(Months[Delta.index(max(Delta))])

#Greatest decrease in losses (date and amount) over the entire period
Greatest_Decrease = min(Delta)
Greatest_Decrease_Date = str(Months[Delta.index(min(Delta))])

#Print Statements
print(f"Average Change: $", round(Average_Change,2))
print(f"Greatest Increase: ", Greatest_Increase_Date, "($", Greatest_Increase,")")
print(f"Greatest Decrease: ", Greatest_Decrease_Date, "($", Greatest_Decrease,")")


#Print the analysis to the terminal and export a text file 
writefile.writelines('	\n') 
writefile.writelines('Financial Analysis for Pybank\n')
writefile.writelines('	\n')
writefile.writelines('Total Months: ' + str(len(Months)) + '\n') writefile.writelines('Total P&L: $' + str(sum(Plus_Minus)) + '\n') writefile.writelines('Average Change: $' + str(round(Average_Change,2)) + '\n') writefile.writelines('Greatest Increase: ' + Greatest_Increase_Date + ' ($' +
str(Greatest_Increase) + ')'+ '\n')
writefile.writelines('Greatest Decrease: ' + Greatest_Decrease_Date + ' ($' + str(Greatest_Decrease) + ')')
