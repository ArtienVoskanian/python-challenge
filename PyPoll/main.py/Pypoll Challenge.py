#Pypoll Challenge
#Import necessary modules

import os
import csv

#Set up some empty lists/variables we will use later

ballot_id = []
candidates = []
unique_candidates = []
ccs_count = 0
dd_count = 0
rad_count = 0

#Set up a path that references the csv file which contains the data we want to analyze
#Open it and read the reference file
#Skip the header

csvpath = os.path.join("..","Resources","election_data.csv")
with open(csvpath,encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)

#The dataset includes "Voter ID", "County", and "Candidate". 
#First lets take the colums with relevant information to the project and append them to our empty lists

    for row in csvreader:
        ballot_id.append(row[0])
        candidates.append(row[2])

#Now lets loop through the data and find the candidates involved in the election, appending each candidate only once into our unique_candidates list        
#Also, lets store each candidate in a seperate variable for future use   
    for candidate in candidates:
        if candidate  not in unique_candidates:
            unique_candidates.append(candidate)
    
    candidate1 = unique_candidates[0]
    candidate2 = unique_candidates[1]
    candidate3 = unique_candidates[2]
            
#We can calculate how many votes each candidate received by looping through our list and checking each rows value
#Each row adds 1 vote to the relevant candidates count. Adding up all three counts will give us the total votes in the election

    for x in range(len(candidates)):
        if candidates[x] == unique_candidates[0]:
            ccs_count = ccs_count + 1
        elif candidates[x] == unique_candidates[1]:
            dd_count = dd_count + 1
        elif candidates[x] == unique_candidates[2]:
            rad_count = rad_count + 1

    total_votes = int(ccs_count) + int(dd_count) + int(rad_count)

#With the total number of votes, as well as each candidates votes both calculated, we can find what percentage of the vote each candidate won
   
    ccs_percentage = round(ccs_count/total_votes * 100,3)
    dd_percentage = round(dd_count/total_votes * 100,3)
    rad_percentage = round(rad_count/total_votes * 100,3)

#Finally lets declare the winner based on popular vote

    if int(ccs_count) > int(dd_count) and int(ccs_count) > int(rad_count):
        winner = "Charles Casper Stockham"
    elif int(dd_count) > int(rad_count) and int(dd_count) > int(ccs_count):
        winner = "Diana DeGette"
    elif int(rad_count) > int(ccs_count) and int(rad_count) > int(dd_count):
        winner = "Raymon Anthony Doane"

#All thats left is to print the results in the terminal, as well as exporting them to a txt file

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")

    print("----------------------------")
    print(f"{candidate1}: {ccs_percentage}% ({ccs_count})")
    print(f"{candidate2}: {dd_percentage}% ({dd_count})")
    print(f"{candidate3}: {rad_percentage}% ({rad_count})")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

output_path = os.path.join("..","Analysis","PyPoll Challenge Txt File")
with open(output_path,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"{candidate1}: {ccs_percentage}% ({ccs_count})"])
    csvwriter.writerow([f"{candidate2}: {dd_percentage}% ({dd_count})"])
    csvwriter.writerow([f"{candidate3}: {rad_percentage}% ({rad_count})"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["----------------------------"])    
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote