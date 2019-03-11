#PyPoll
import os 
import csv

csvpath = "PyPoll/election_data.csv"

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    csv_header = next(csvreader)

# Declare  Variables 
county = []
candidates = []
unique_candidates = []
row_count=0
winning_number_of_votes = 0 
voter_id = []


# Loop through the rows of *.csv 
    for row in csvreader:
        candidate = row[2]

        total_votes += 1

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

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
	 	 	 
