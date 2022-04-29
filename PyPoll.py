## Anthony Doane was winner (wrong) have to re-start at 3.5.4

#The data we need to retreive
## 1. - the total number of votes cast
## 2. - a complpete list of candidates who received votes
## 3. - the percentage of votes each candidate won
## 4. - the total number of votes each candidate won
## 5. - the winner of the election based on popular vote

#open CSV with indirect method
import csv
import os
#from tkinter.tix import COLUMN
dir(os.path)
os.path.join("Resources", "election_results.csv")

# Load: Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Save: Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#add the total votes variable and set intial total votes to zero
total_votes = 0

#lesson 3.5.3 candidate options & candidate votes declared 
candidate_options = []

# declare an empty dictionary
candidate_votes = {}

# Track: Winning Candidate & Winning Count Tracker (vote count and percentage)
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. added a second with statement
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

 #read the header row
    headers = next(file_reader)
   #print(headers)

    ##use a for statement to iterate through the rows and pull data including header
    for row in file_reader:
        #add total votes
        total_votes += 1
        #print(total_votes)

        #add option to get & print candidate name
        candidate_name = row[2]

        #add "if/not in " statement so name only prints once
        if candidate_name not in candidate_options:
         
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
            candidate_options.append(candidate_name)

         #initalize at zero to track candidate's vote count; 
            candidate_votes[candidate_name] = 0

        #track candidate's votes & add by 1 (and move out of the if statement)
        candidate_votes[candidate_name] += 1
#save results to txt file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
            # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
            #calculate vote percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results =(
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    
        print(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #vote count and percentage
            winning_count = votes
            winning_candidate =  candidate_name
            winning_percentage = vote_percentage
    #set winning candidate equal to winning name
            winning_candidate = candidate_name
    #print winning results to term
    winning_candidate_summary =(
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results)
    # Save the final vote count to the text file.
    txt_file.write(election_results)
   
    








   



   




