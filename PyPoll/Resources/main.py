#Create a Python script that analyzes the votes and calculates each of the following values:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote

import os
import csv

#path made 
csvpath=os.path.join("Resources","election_data.csv")

ballot_id=[]
candidate=[]
charles=0
diana=0
raymon=0

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)

    #header
    csvheader=next(csvreader)

    #column lists
    for row in csvreader:
        ballot_id.append(row[0])
        candidate.append(row[2])

    #number of votes
    for i in range(len(candidate)):
        if candidate[i] == "Charles Casper Stockham":
            charles = charles + 1
        elif candidate [i] == "Diana DeGette":
            diana = diana + 1
        elif candidate[i] == "Raymon Anthony Doane":
            raymon = raymon + 1

    #winner
    if charles>diana and charles>raymon:
        winner = "Charles Casper Stockham"
    elif diana>charles and diana>raymon: 
        winner = "Diana DeGette"
    elif raymon>charles and raymon>diana:
        winner = "Raymon Anthony Doane"    


print('\n')
print("Election Results")
print("-"*30)
print(f"Total Votes: {len(ballot_id)}")
print("-"*30)
print(f"Charles Casper Stockham: {round(((charles/len(ballot_id))*100),3)}% ({charles})")
print(f"Diana Degrette: {round(((diana/len(ballot_id))*100),3)}% ({diana})")
print(f"Raymon Anthony Doane: {round(((raymon/len(ballot_id))*100),3)}% ({raymon})")
print("-"*30)
print(f"Winner: {winner}")
print('\n')

outputpath = os.path.join("Analysis","Poll Analysis.txt")

with open(outputpath,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow('\n')
    csvwriter.writerow("-"*30)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow("-"*30)
    csvwriter.writerow(f"Total Votes: {len(ballot_id)}")
    csvwriter.writerow("-"*30)
    csvwriter.writerow(f"Charles Casper Stockham: {round(((charles/len(ballot_id))*100),3)}% ({charles})")
    csvwriter.writerow('\n')
    csvwriter.writerow(f"Diana Degrette: {round(((diana/len(ballot_id))*100),3)}% ({diana})")
    csvwriter.writerow('\n')
    csvwriter.writerow(f"Raymon Anthony Doane: {round(((raymon/len(ballot_id))*100),3)}% ({raymon})")
    csvwriter.writerow("-"*30)
    csvwriter.writerow(f"Winner: {winner}")











        

