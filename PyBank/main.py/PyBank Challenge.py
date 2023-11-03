# PyBank Challenge

#Let's import the necessary modules to read and utilize csv files

import os
import csv

#Set up some introductory Print Statements and empty lists we can append later
print("Financial Analysis")
print("---------------------------")
total_months = []
net_total = []
monthly_flux =[]


#Set up a filepath that references the budget_data.csv
#Open and read budget_data.csv

csvpath = os.path.join("..","Resources","budget_data.csv")
with open(csvpath,encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)

#Write a script that analyzes/calculates the following:  
#Total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        total_months.append(row[0])
        net_total.append(int(row[1]))
    print(f"Total Months: {len(total_months)}")
    print(f"Total: $ {sum(net_total)}")
        
#The changes in "Profit/Losses" over the entire period,
#and then averages those changes
    for x in range(len(total_months)):
        if net_total[x] > 0 and net_total[x]+1 > 0 and net_total[x]+1 > net_total[x]:

    
    for x in range(len(total_months)):
        if int(row[1]) > 0 and int(row[1]+1) > 0 and int(row[1]+1) > int(row[1]):
            change = int(row[1]+1) - int(row[1])
            monthly_flux.append(change)
        elif int(row[1]) > 0 and int(row[1]+1) > 0 and int(row[1]+1) < int(row[1]):
            change = int(row[1]) - int(row[1]+1)
            monthly_flux.append(change)
        elif int(row[1]) < 0 and int(row[1]+1) > 0:
            change = int(row[1]+1) + int(row[1])
            monthly_flux.append(change)
        elif int(row[1]) < 0 and int(row[1]+1) < 0 and int(row[1]) > int(row[1]+1):


#The greatest increase in profits (date and amount) over entire period

#The greatest decrease in profits (date and amount) over the entire period

#Print all calculated values, adjusting value types and utilizing methods where needed
            
#Analysis must be printed to terminal AND exported to a txt file