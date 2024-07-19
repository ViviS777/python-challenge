# name:...
# date:2024-7-13
# file:PyBank
# encoding=utf-8

# Import modules os and csv
import os
import csv
# File path.
PyBankdata = os.path.join("Resources", "budget_data.csv")
# Get data.
with open(PyBankdata, mode='r', encoding='utf-8') as file:
    data = csv.DictReader(file)
    # Initial var    
    Total_months = 0
    Total = 0
    Profit_Losses = []
    Changes = []
    dates=[]
    # Get target data.
    previous_profit_loss=0
    for row in data:
        # Get Total months.
        if row['Date']:            
            Total_months += 1
            dates.append(row['Date'])           
        Profit_Loss = row['Profit/Losses']
        Profit_Losses.append(Profit_Loss)
        # Get Total profits.
        if Profit_Loss:           
            Total += float(Profit_Loss)
        # Get total monthly change.
        if row['Date'] is not None:            
            change = float(Profit_Loss)- float(previous_profit_loss)           
            Changes.append(change)
        previous_profit_loss = Profit_Loss
    # Get average monthly change.    
    average_change = (sum(Changes)-Changes[0]) / (Total_months - 1)
    # Find the max, min change and the corresponding dates
    Max_increase_Change = max(Changes)
    Min_decrease_Change = min(Changes)
    greatest_increase_index = Changes.index(Max_increase_Change)
    greatest_increase_date = dates[greatest_increase_index ]
    greatest_decrease_index = Changes.index(Min_decrease_Change)
    greatest_decrease_date = dates[greatest_decrease_index ]  
### Output 
with open('Financial Analysis.txt', 'w') as text:
    text.write(f"\nFinancial Analysis\n")
    text.write("\n---------------------------\n")
    text.write(f"\nTotal months: {Total_months}\n")
    text.write(f"\nTotal: ${Total:.0f}\n")
    text.write(f"\naverage_change: ${average_change:.2f}\n")
    text.write(f"\nGreatest Increase in Profits: {greatest_increase_date} (${Max_increase_Change:.0f})\n")
    text.write(f"\nGreatest Decrease in Profits: {greatest_decrease_date} (${Min_decrease_Change:.0f})\n")








    
