#create a Python script that analyzes the records to calculate each of the following values:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period

from audioop import avg
from locale import currency
import os
import csv

#path made 
csvpath=os.path.join("Resources", "budget_data.csv")

total_months=[]
net_totals=[]
profit_change=[]

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)

    csvheader=next(csvreader)

#locating number of months
    for row in csvreader:
        total_months.append(row[0])
        net_totals.append(int(row[1]))

for i in range(len(net_totals) -1):
    profit_change.append(net_totals[i+1] - net_totals[i])


max_increase_month_index = profit_change.index(max(profit_change)) +1
max_decrease_month_index = profit_change.index(min(profit_change)) +1



print('\n')
print("Financial Analysis")
print("-"*30)
print(f"Total Months: {len(total_months)}")
print('\n')
print(f"Net Totals: ${sum(net_totals)}")
print('\n')
print(f"Average Change: ${round(sum(profit_change) / len(profit_change),2)}")
print('\n')
print(f"Greatest Increase in Profits: {total_months[max_increase_month_index]} (${max(profit_change)})")
print('\n')
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month_index]} (${min(profit_change)})")
print('\n')

#Output Files
output_files = os.path.join("Analysis", "Financial Analysis.txt")

with open(output_files, "w") as file:

    file.write("Financial Analysis")
    file.write('\n')
    file.write("-"*30)
    file.write('\n')
    file.write(f"Total Months: {len(total_months)}")
    file.write('\n')
    file.write(f"Net Totals: ${sum(net_totals)}")
    file.write('\n')
    file.write(f"Average Change: ${round(sum(profit_change) / len(profit_change),2)}")
    file.write('\n')
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month_index]} (${max(profit_change)})")
    file.write('\n')
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month_index]} (${min(profit_change)})")
    file.write('\n')