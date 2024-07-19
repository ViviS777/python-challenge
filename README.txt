# PyPoll

## Description
This Python script analyzes the vote data from a local election. It reads the election data from a CSV file located in the "Resources" directory, processes the data, and outputs the election results to a text file named "Election results.txt".

The script performs the following tasks:

1. Imports the necessary modules (os and csv).
2. Retrieves the file path for the "election_data.csv" file located in the "Resources" directory.
3. Reads the election data from the CSV file using the csv.DictReader() function.
4. Initializes variables to keep track of the total number of votes and the number of votes for each candidate.
5. Iterates through the election data, counting the total number of votes and the votes for each candidate.
6. Calculates the percentage of votes for each candidate.
7. Determines the winner of the election based on the highest number of votes.
8. Writes the election results to the "Election results.txt" file, including the total number of votes, the percentage and number of votes for each candidate, and the name of the winner.

## Usage
1. Ensure that the "election_data.csv" file is located in the "Resources" directory.
2. Run the Python script.
3. The "Election results.txt" file will be created in the same directory as the Python script, containing the election results.

## Output
The script will generate the following output in the "Election results.txt" file:


# PyBank

## Description
This Python script analyzes the financial records of a company. It reads the financial data from a CSV file located in the "Resources" directory, processes the data, and outputs the financial analysis to a text file named "Financial Analysis.txt".

The script performs the following tasks:

1. Imports the necessary modules (os and csv).
2. Retrieves the file path for the "budget_data.csv" file located in the "Resources" directory.
3. Reads the financial data from the CSV file using the csv.DictReader() function.
4. Initializes variables to keep track of the total number of months, the total profit/losses, the changes in profit/losses, and the corresponding dates.
5. Iterates through the financial data, calculating the total number of months, the total profit/losses, and the changes in profit/losses between consecutive months.
6. Calculates the average change in profit/losses.
7. Determines the greatest increase and decrease in profits, including the corresponding dates.
8. Writes the financial analysis to the "Financial Analysis.txt" file, including the total number of months, the total profit/losses, the average change in profit/losses, the greatest increase in profits, and the greatest decrease in profits.

## Usage
1. Ensure that the "budget_data.csv" file is located in the "Resources" directory.
2. Run the Python script.
3. The "Financial Analysis.txt" file will be created in the same directory as the Python script, containing the financial analysis.

## Output
The script will generate the following output in the "Financial Analysis.txt" file: