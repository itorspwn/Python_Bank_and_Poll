import os 
import csv

#Set file path 
election_csv = os.path.join('Resources', 'election_data.csv')


#Def data lists
voter_id = []
county = []
candidate = []


#Read in csv path
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #read header row
    header = next(csvreader)
    #read row after header
    next_row = next(csvreader)
    
    #loop through file and append voter id, county, and candidate to lists 
    for rows in csvreader:
        
        #add items to lists
        voter_id.append(int(rows[0]))
        county.append(rows[1])
        candidate.append(rows[2])
    

#total votes
total_vote = len(voter_id)


#Def individual candidate lists
khan = []
correy = []
li = []
o_tooley = []


    #loop through list of candidate and add to individial candidate lists 
for i in candidate:
    if i == "Khan":
            khan.append(candidate)
    elif i == "Correy":
            correy.append(candidate)
    elif i == "Li":
            li.append(candidate)
    else:
            o_tooley.append(candidate)

#total vote for each candidate
total_khan = len(khan)
total_correy = len(correy)
total_li = len(li)
total_o_tooley = len(o_tooley)

#The percentage of votes each candidate won
khan_p = total_khan / len(candidate) * 100
correy_p = total_correy / len(candidate) * 100
li_p = total_li / len(candidate) * 100
li_p_round = round(li_p)
li_p_round = float(li_p_round)
o_tooley_p = total_o_tooley / len(candidate) * 100

#Total number of votes for each candidate
khan_total = len(khan)
correy_total = len(correy)
li_total = len(li)
o_tooley_total = len(o_tooley)

#Set "winner" to candidate with greatest tally of votes
if len(khan) > len(correy) and len(khan) > len(li) and len(khan) > len(o_tooley):
    winner = "Khan"
elif len(correy) > len(khan) and len(correy) > len(li) and len(correy) > len(o_tooley):
    winner = "Correy"
elif len(li) > len(khan) and len(li) > len(correy) and len(li) > len(o_tooley):
    winner = "Li"
else:
    winner = "O'Tooley "



#----------------------------------------------------------------------------
#print election results table 

print(f"Election Results\n-------------------------\nTotal Votes: {total_vote}\n-------------------------\nKhan: {khan_p}% ({total_khan})\nCorrey: {correy_p}% ({total_correy})\nLi: {li_p_round}% ({total_li})\nO'Tooley: {o_tooley_p}% ({total_o_tooley})\n-------------------------\nWinner: {winner}\n-------------------------")

   
#----------------------------------------------------------------------------
#export text file with election results 

analysis_path = os.path.join("Analysis", "Election_Results.txt")
analysis = open(analysis_path, "w")

print(f"Election Results\n-------------------------\nTotal Votes: {total_vote}\n-------------------------\nKhan: {khan_p}% ({total_khan})\nCorrey: {correy_p}% ({total_correy})\nLi: {li_p_round}% ({total_li})\nO'Tooley: {o_tooley_p}% ({total_o_tooley})\n-------------------------\nWinner: {winner}\n-------------------------",  file = analysis)


analysis.close()