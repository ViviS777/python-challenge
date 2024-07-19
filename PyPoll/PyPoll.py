#name:...
#date:2024-7-13
#file:PyPoll
#encoding=utf-8

# Import modules os and csv
import os
import csv
# Get the target directory path.
PyPolldata= os.path.join("Resources","election_data.csv")
# Get data.
with open(PyPolldata, mode='r', encoding='utf-8') as file:
    data = csv.DictReader(file)  
    # Initial var    
    Total_votes=0
    candidates={}
    # Get target data.
    for row in data:
        # Count votes.
        if row['Ballot ID']:
            Total_votes += 1
        # Count candidates.    
        candidate = row['Candidate']        
        if candidate in candidates:  
            candidates[candidate] += 1  
        else:  
            candidates[candidate] = 1
    # Find the winner.
    max_key, max_value = max(candidates.items(), key=lambda x: x[1])
### Output 
with open('Election results.txt', 'w') as text:
    text.write("\nElection Results\n")
    text.write("\n---------------------------\n")
    text.write(f"\nTotal votes: "+str(Total_votes)+"\n")
    text.write("\n---------------------------\n")
    # Get the candidate list and votes.
    for candidate, count in candidates.items():
        a=count/Total_votes
        text.write(f"\n{candidate}: {float(a)*100:.3f}% ({count})\n")
    text.write("\n---------------------------\n")
    text.write(f"\nWinner:{max_key}\n")
    text.write("\n---------------------------\n")
