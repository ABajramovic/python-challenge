#PyPoll
import os 
import csv

csvpath = "C:/Users/bajraax/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

# Declare  Variables 
county = []
candidate = []
unique_candidates = []
row_count=0
winning_number_of_votes = 0 
voter_id = []

with open(csvpath, newline='') as csvfile:
csvreader = csv.reader(csvfile, delimiter=',') 
csv_header = next(csvreader)


# Loop through the rows of *.csv 
for row in csvreader:

# Complete a list of candidates who received votes
    candidate.append(row[2])
    current_candidate = row[2]
    row_count = row_count+1
    voter_id.append(row[0])
    county.append(row[1])


# Combine and create a list of candidates who received votes
    if unique_candidates.count(current_candidate) == 0:
        unique_candidates.append(current_candidate)
    print(f"	") 
    print(f"Election Results")
    print(f"	") 
    print(f"Total Votes : {row_count}")
    string = "Total Votes : "+ str(row_count)
    print(f"	") 
    f.write('Election Results\n')
    f.write("	") 
    f.write(string + '\n')
    f.write('	\n')

for person in unique_candidates:
    number_of_votes = candidate.count(person)

    if number_of_votes > winning_number_of_votes:	 	 
        winner = person	 	 
        winning_number_of_votes = number_of_votes	 	 
    percent_of_votes = number_of_votes / row_count *100	 	 
    percent_of_votes = round(percent_of_votes,4)	 	 
	 	 	 
    print(f"{person} : {percent_of_votes}% ({number_of_votes})	")	 	 
    string = str(person) + "	:	" + "	" + str(percent_of_votes) + "%"	+ "	" + "(" + str(number_of_votes) + ")"
    f.write(string+"\n")	 	 

print(f"------------------------")	 	 
 	 	 
f.write('	\n')	 	 
print(f"Winner :	{winner}")	 	 
string = "Winner	:	" +str(winner)	 	 
f.write(string+"\n")	 	 
f.write('	\n')	 	 
f.close	 	 
	 	 	 
