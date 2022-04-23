#The data we need to retreive
## 1. - the total number of votes cast
## 2. - a complpete list of candidates who received votes
## 3. - the percentage of votes each candidate won
## 4. - the total number of votes each candidate won
## 5. - the winnder of the election based on popular vote

#open CSV with indirect method
import csv
import os
dir(os.path)
os.path.join("Resources", "election_results.csv")
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#add the total votes variable and set intial total votes to zero
total_votes = 0

#candidate options
candidate_options = []

# declare an empty dictionary
candidates_votes ={}
candidate_votes = {"candidate_name1" : votes, "candidate_name2" : votes, "candidate_name3" : votes}


# Open the election results and read the file.
with open(file_to_load) as election_data:
    #to do: read & analyze the data here
    ## read the file object with reader function
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    print(headers)

    ##use a for statement to iterate through the rows and pull data including header
    for row in csv.reader(election_data):
        #add total votes
        total_votes += 1
        print(total_votes)

        #add option to print candidate name
        candidate_name = row[2]

        #add "if/not in " statement so name only prints once
        if candidate_name not in candidate_options:
         
         #add candidate name to the list
         candidate_options.append(candidate_name)

         #track candidate's vote count
         candidate_votes[candidate_name] = 0

#print candidate list
print(candidate_options)


   
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


    # Print the file object.
     #print(election_data)


# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


   




