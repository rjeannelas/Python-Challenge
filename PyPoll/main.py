# import poll
import os
import csv

# Reference variables
votes = []
county = []
candidates = []
Charles_Casper_Stockham = []
Diana_DeGette = []
Raymon_Anthony_Doane = []
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

# open file location and read csv
election_data=os.path.join('Resources','election_data.csv')
print(os.path.abspath(election_data))

C:\Users\rjean\Downloads\Resources\election_data.csv

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    # Iterate each row of data after header
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

Header: ['Ballot ID', 'County', 'Candidate']

# Count the Voter ID's for total
total_votes = (len(votes))
print(total_votes)

739422

# Count the votes by canidate name
for candidate in candidates:
    if candidate == "Charles Casper Stockham":
        Charles_Casper_Stockham.append(candidates)
        Charles_Casper_Stockham_votes = len(Charles_Casper_Stockham)
    elif candidate == "Diana DeGette":
        Diana_DeGette.append(candidates)
        Diana_DeGette_votes = len(Diana_DeGette)
    else:
        Raymon_Anthony_Doane.append(candidates)
        Raymon_Anthony_Doane_votes = len(Raymon_Anthony_Doane)
        
print(Charles_Casper_Stockham_votes)
print(Diana_DeGette_votes)
print(Raymon_Anthony_Doane_votes)

511278
1637352
69636

# Percentages
Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_votes / total_votes) * 100), 3)
Diana_DeGette_percent = round(((Diana_DeGette_votes / total_votes) * 100), 3)
Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_votes / total_votes) * 100), 3)

print(Charles_Casper_Stockham_percent)
print(Diana_DeGette_percent)
print(Raymon_Anthony_Doane_percent)

69.146
221.437
9.418

# Winner 
if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
    winner = "Charles_Casper_Stockham"
elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent, Raymon_Anthony_Doane_percent):
    winner = "Diana_DeGette"  
else:
    winner = "Raymon_Anthony_Doane"

# Print Statements
print(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

Election Results
-----------------------------------
Total Votes: 739422
-----------------------------------
Charles_Casper_Stockham_percent: 69.146% (511278)
Diana_DeGette: 221.437% (1637352)
Raymon_Anthony_Doane: 9.418% (69636)
-----------------------------------
Winner: Diana_DeGette
-----------------------------------

# Output to a text file
file = open("output.txt","w")
file.write(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

file.close()
