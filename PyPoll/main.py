#Analyze polling data for a recent election to find the winner

#Import the poll data
import os
import csv
pollcsv = os.path.join("Resources","election_data.csv")

with open(pollcsv) as csvfile:
    #Read the header row first, then save the dataset in csvreader
    csv_header = next(csvfile)     
    csvreader = csv.reader(csvfile, delimiter = ',')
    # Initialize variables   
    tot_votes = 0
    candidates = dict()
    names = []   
    
    for row in csvreader:
        # Calculate the total number of votes 
        tot_votes += 1
        # Get unique candidate names, store as keys in candidates dictionary
        # Also add votes per candidate and store as values in the candidates dictionary
        if row[2] not in names:
            names.append(row[2])
            candidates[row[2]] = list()
            candidates[row[2]].append(1) 
        else:
            candidates[row[2]][0] += 1
      
    # Print results
    line1 = "Election Results \n"
    line2 = "---------------------------------------- \n"
    line3 = "Total Votes: {}\n". format(tot_votes)
    line4 = "---------------------------------------- \n" 
    print(line1+line2+line3+line4) 

    # Store the percentage of votes each candidate won in the dictionary
    winner_percentage = 0
    winner = 0
    candidate_lines = []
    for key,value in candidates.items():  
        # The percentage of votes each candidate won
        percentage = (value[0]/tot_votes) * 100
        candidates[key].append(percentage)
        # Find the winning candidate
        if percentage > winner_percentage:
            winner_percentage = percentage
            winner = key
        candidate_lines.append("{}: {:.3f}% ({})".format(key,candidates[key][1],candidates[key][0]))
    
    # Print results 
    for i in candidate_lines:  
        print(i)       
    line5="---------------------------------------- \n"
    line6="Winner: {}\n".format(winner)
    line7="---------------------------------------- \n"
    print(line5+line6+line7) 

# Write data to a text file
with open("analysis/PollResults.txt", "w") as text_file:
    text_file.write(line1+line2+line3+line4)
    for i in candidate_lines:
        text_file.write(i)
        text_file.write("\n")   
    text_file.write(line5+line6+line7)

