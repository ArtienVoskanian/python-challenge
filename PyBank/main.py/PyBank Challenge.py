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
greatest_increase = 0
greatest_decrease = 0


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
#Make a new list that stores the calculated data of the increase or decrease in profits from each month 
#Round function is used to round the averaged value to 2 decimal places only

    for x in range(len(total_months)-1):
        change = int(net_total[x+1]) - int(net_total[x])
        monthly_flux.append(change)
    average = round(sum(monthly_flux)/len(monthly_flux),2)
    print(f"Average: ${average}")
    
        
#Greatest increase in profits during the time period. Must print out the date of when that was, as well as the value itself
#Greatest decrease in profits. Print out the date of when that was and the value.
#Can calculate these two at the same time since we are looking at the same list for both
#Must add a + 1 to the indexes for the total_months list so it matches the monthly_flux index since its indexes are shifted up 1
#This relative shift is due to how we calculated the values stored in the monthly_flux list above 

    for x in range(len(monthly_flux)-1):
        if monthly_flux[x] > monthly_flux[x+1] and monthly_flux[x] > greatest_increase:
            greatest_increase = monthly_flux[x]
            greatest_increase_date = total_months[x+1]
        elif monthly_flux[x] < monthly_flux[x+1] and monthly_flux[x+1] > greatest_increase:
            greatest_increase = monthly_flux[x+1]
            greatest_increase_date = total_months[x+2]
        elif monthly_flux[x] < monthly_flux[x+1] and monthly_flux[x] < greatest_decrease:
            greatest_decrease = monthly_flux[x]
            greatest_decrease_date = monthly_flux[x+1]
        elif monthly_flux[x] > monthly_flux[x+1] and monthly_flux[x+1] < greatest_decrease:
            greatest_decrease = monthly_flux[x+1]
            greatest_decrease_date = total_months[x+2]  
    print(f"Greatest Increase: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease: {greatest_decrease_date} (${greatest_decrease})")
            
           
#Analysis must be printed to terminal AND exported to a txt file