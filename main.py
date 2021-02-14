#import modules
import os
import csv

#defining variables
total_months = 0
total_amount = 0
month_int_change = 0
month_int_count = 0
month_array_change = []
month_array_count = []
most_increase = 0
month_increase = 0
most_decrease = 0
month_decrease = 0

#setting file path and opening file
csvpath = os.path.join('.', 'PyBank' , 'Resources' , 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    
    #determines data by delimiting by commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skips the header by going to next row
    csv_header = next(csvreader)
    row = next(csvreader)
    
    #going to calculate the months, profit amount, and sets row variable
    previous_row = int(row[1])
    total_months += 1
    total_amount += int(row[1])
    Most_increase = int(row[1])
    month_increase = row[0]
    
    #reads each row after the header string
    for row in csvreader:
        
        #Adds months and profits/losses from the data
        total_months += 1
        total_amount += int(row[1])
        
        #calculates profit/loss changes from  month to month
        month_int_change = int(row[1]) - previous_row
        month_array_change.append(month_int_change)
        previous_row = int(row[1])
        month_array_count.append(row[0])
        
        #if statements to determine highest and lowest amount 
        #by override with current row
        if int(row[1]) > most_increase:
            most_increase = int(row[1])
            month_increase = row[0]
            
        if int(row[1]) < most_decrease:
            most_decrease = int(row[1])
            month_decrease = row[0]
            
    #averages total sum of the array with the length (Average)        
    average_change = sum(month_array_change)/ len(month_array_change)
    
    #takes highest value from the array
    high = max(month_array_change)
    low = min(month_array_change)

#printing out the analysis   
financial_analysis = (f'''Financial Analysis
    ------------------
    Total Months: {total_months}
    Total: ${total_amount}
    Average Change: ${average_change:.2f}  
    Greatest Increase in Profits: {month_increase} ${high}
    Greatest Decrease in Profits: {month_decrease} ${low}''')
print(financial_analysis)

#using previous variable to create new output file
outputtxt = open('output.txt', 'w')
outputtxt.write(financial_analysis)
outputtxt.close() 