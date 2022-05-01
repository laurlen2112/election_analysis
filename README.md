# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks in order to complete the audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the percentage of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
* Data Source: election_results.csv
* Software: 
  * Python 3.9.7
  * Visual Studio Code, 1.66.2

## Summary 
The analysis of the election show that:
* 369,711 votes were cast in the election.
* The candidates were:
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
* The results were:
  * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
* The winner of the election was:
  * Diane DeGette who received 73.8% of the vote and 272,892 number of votes.
  
  ## Challenge Overview
  
  ## Election Audit Summary

Seth, Tom, and I created a flexible code that is easily modified to enable analysis of almost any election.  Flexibility is possible because the code extracts data from a CSV file (pictured [here](https://github.com/laurlen2112/election_analysis/blob/main/resources/import%20csv.png) and [here](https://github.com/laurlen2112/election_analysis/blob/main/resources/read%20csv.png)) and uses “for loops” and “if statements” to tabulate results.  Therefore, it can be modified to account for different election circumstances.  

For example, for county elections, the code can be modified to track towns or precincts within that county by modifying the [script which tracks county turnout](https://github.com/laurlen2112/election_analysis/blob/main/resources/County%20for%20loop%20and%20print%20results.png).

Also, this code can also be expanded to track votes in favor of ballot propositions by adding an additional “for loop” to track and tally votes and using a nested “if statement” to determine the results.  The “for loop” and “if statement” would be modeled after [the code used to track and tally candidate votes](https://github.com/laurlen2112/election_analysis/blob/main/resources/candidate%20for%20and%20if%20statements.png).  This code snippet successfully served as a model to add the functionality to [tabulate voter turnout by county](https://github.com/laurlen2112/election_analysis/blob/main/resources/County%20Code%20Modeled%20after%20Candidate%20Code.png, so it has proof or reliability.

Based on the foregoing, we ask that the election commission consider licensing our code for future elections.  We remain happy to answer any questions regarding our code’s functionality and its ability to handle future use cases and thank you for your time and consideration.
