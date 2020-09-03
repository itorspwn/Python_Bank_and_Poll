import os 
import csv

#Set file path 
bank_csv = os.path.join('Resources', 'budget_data.csv')


#Def data lists
dates = []
revenue = []
delt_change = []

#Assign accumulators
total_months = 0
net_revenue = 0


#Read in csv path
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #read header row
    header = next(csvreader)

    #read row after header
    next_row = next(csvreader)
    #assign variable to revenue column 
    amount = int(next_row[1])
    #add month 
    total_months += 1
    #add revenue to net 
    net_revenue += amount

    #loop through file and append months and revenue to lists 
    for rows in csvreader: 

        #add to month total
        total_months = total_months + 1
        #add revenue to net 
        net_revenue = net_revenue + int(rows[1])

        #add month and revenue to lists
        dates.append(rows[0])
        revenue.append(int(rows[1]))

        #find change in profit and add change to list
        difference = int(rows[1]) - amount
        delt_change.append(difference)
        amount = int(rows[1])



#average of changes in profit/losses over the entire period
avg_change = sum(delt_change)/len(delt_change)
#print(avg_change)

#greatest increase in profits (date and amount) over the entire period
g_increase = max(revenue)
increase_index = revenue.index(g_increase)
max_month = dates[increase_index]
#print(max_month)

#greatest decrease in losses (date and amount) over the entire period 
g_decrease = min(revenue)
decrease_index = revenue.index(g_decrease)
min_month = dates[decrease_index]
#print(min_month)


#----------------------------------------------------------------------------
#print financial summary table 

print(f'Financial Analysis\n-------------------------\nTotal Months: {total_months}\nTotal: ${net_revenue}\nAverage Change: ${avg_change}\nGreatest Increase in Profits: {max_month} (${g_increase})\nGreatest Decrease in Profits: {min_month} (${g_decrease})')

   
#----------------------------------------------------------------------------
#export text file with results 

analysis = open("financial_analysis.txt", "w")

print(f'Financial Analysis\n-------------------------\nTotal Months: {total_months}\nTotal: ${net_revenue}\nAverage Change: ${avg_change}\nGreatest Increase in Profits: {max_month} (${g_increase})\nGreatest Decrease in Profits: {min_month} (${g_decrease})', file = analysis)


analysis.close()



