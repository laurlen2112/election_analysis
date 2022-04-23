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
# Open the election results and read the file.
with open(file_to_load) as election_data:
    #to do: read & analyze the data here
    ## read the file object with reader function
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    print(headers)
      ##use a for statement to iterate through the rows and pull data including header
    #for row in csv.reader(election_data):
        #print(row)
   
    # Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("analysis", "election_analysis.txt")


    # Print the file object.
     #print(election_data)


# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


   




#Test Message - Hellow world in output file
#create a filename variable to a direct or indirect path file (i used unidrect)
#file_to_save = os.path.join("analysis", "election_analysis.txt")

#statement to open the file
##replace this line with "with" statement outfile = open(file_to_save, "w"); 
#with open(file_to_save, "w") as txt_file:

#write data to file
###--replaced due to with statement outfile.write("hello world")
    ##replaced with the counties --txt_file.write("hello world, it's me paisley mae")
    ### replaced to add each county on a new linetxt_file.write("Arapahoe, Denver, Jefferson")
    ## add header "counties in election"
    #txt_file.write("Counties in the Election")
   #txt_file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _")
    #txt_file.write("\nArapahoe\nDenver\nJefferson")
#close file
##-- this line is not needed due to "with" statment outfile.close()