#Analyze financial records of a company

#Your task is to create a Python script that analyzes the records to calculate each of the following:


#Import the buget data
import os
import csv
budgetcsv = os.path.join("Resources","budget_data.csv")

with open(budgetcsv) as csvfile:
    # Read the header row first, then save the dataset in csvreader
    csv_header = next(csvfile)     
    csvreader = csv.reader(csvfile, delimiter = ',')
    # Initialize variables   
    Months = 0
    Sum_Profit = 0
    change = 0
    prevprofit = 0
    GProfit = 0
    GLoss = 0
    GProfit_Date = ""
    GLoss_Date = ""

    # Scan dataset by each row, and calculate some metrics
    for row in csvreader:
        # Calculate the net total amount of "Profit/Losses" over the entire period
        Sum_Profit += int(row[1])
        # Calculate the total number of months included in the dataset
        Months += 1
        # Store the first "Profit/Loss" value, next find the change in "Profit/Loss" from month-to-month, keep iterating for entire dataset
        if Months == 1:
            prevprofit = int(row[1])
            continue
        # For each row if the value in the Profit/Loss is positive, record the date as "GProfit_Date" and the profit as "GProfit". 
        # For each row if the value in the Profit/Loss is negative, record the date as "GLoss_Date" and the loss in "GLoss".
        # Compare "Profit/Loss" to the "GProfit", update "GProfit" if the new value is larger than the previous value.
        # Compare "Profit/Loss" to the "GLoss", update "GLoss" if the new value is smaller than the previous value.

        delta = int(row[1]) - prevprofit
        if delta > 0 and delta > GProfit:
            GProfit = delta
            GProfit_Date = row[0]
        if delta < 0 and delta < GLoss:
            GLoss = delta
            GLoss_Date = row[0]
                      
        change +=  delta
        prevprofit = int(row[1])
         
    avg_change = change/(Months-1)
    # print("Financial Analysis")
    # print("----------------------------------------")
    # print("Total Months: ", Months)
    # print("Net Total Profit/Loss: ", "${:.0f}".format(Sum_Profit))
    # print("Average Change in Profit/Loss: ", "${:.2f}".format(avg_change))
    # print("Greatest Increase in Profits: ", GProfit_Date, "(", "${:.0f}".format(GProfit), ")")
    # print("Greatest Decrease in Profits: ", GLoss_Date, "(", "${:.0f}".format(GLoss), ")")
    
    line1 = "Financial Analysis \n"
    line2 = "---------------------------------------- \n"
    line3 = "Total Months: {}\n". format(Months)
    line4 = "Net Total Profit/Loss: ${:.0f}\n".format(Sum_Profit)
    line5 = "Average Change in Profit/Loss: ${:.2f}\n".format(avg_change)
    line6 = "Greatest Increase in Profits: {} (${:.0f})\n".format(GProfit_Date,GProfit)
    line7 = "Greatest Decrease in Profits: {} (${:.0f}\n".format(GLoss_Date,GLoss)
    
    print(line1 + line2 + line3 + line4 + line5 + line6 + line7)

# Write data to a text file
with open("analysis/Output.txt", "w") as text_file:
    text_file.writelines([line1, line2, line3, line4, line5, line6, line7])
    


