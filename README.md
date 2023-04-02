# Election Analysis

## Project Overview
Tom, a Colorado Board of Elections employee, has asked me to complete the audit of a recent local congressional election and provide the following data points:

  1. The total number of votes cast.
  2. A complete list of candidates who received votes.
  3. Calculate the votes per candidate.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.
  6. Determine voter turnout by county.
  7. Determine which county had the largest turnout.

## Resources
* Data Source: [election_results.csv](https://github.com/laurlen2112/election_analysis/blob/main/resources/election_results.csv)
* Software: 
  * Python 3.7.9
  * Visual Studio Code 1.66.2

## [Summary](https://github.com/laurlen2112/election_analysis/blob/main/resources/Election%20Results%20Print%20to%20txt.png) 
The analysis of the election shows that:

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
  
* Turnout by county was:
  * Jefferson county cast 38,855 votes with a 10.5% turnout.
  * Denver county cast 306,055 votes with a 82.8% turnout.
  * Arapahoe county cast 24,801 votes with a 6.7% turnout.
 
* Largest county turnout was:
  * Denver had the largest turnout by county with 306,055 votes cast and a 82.8% turnout.
  
## Challenge Overview
The intial purpose of this project was to tabulate election results for a recent congressional election.  Once that task was complete, the election  commission requested that the code be modified to track county turnout.

## Election Audit Summary  
Seth, Tom, and I have developed a versatile code that can be easily adapted to analyze nearly any election. The code extracts data from a [CSV file](https://github.com/laurlen2112/election_analysis/blob/main/resources/import%20csv.png) and uses [“for loops” and “if statements”](https://github.com/laurlen2112/election_analysis/blob/main/resources/County%20Code%20Modeled%20after%20Candidate%20Code.png) to tabulate results, making it possible to modify it to account for different election scenarios.

For instance, if needed for a county election, the code can be altered to track town-level turnout within that county by modifying the inputs that record county turnout ((pictured [here](https://github.com/laurlen2112/election_analysis/blob/main/resources/step%201%20creat%20county%20list%20and%20dict.png), and [here](https://github.com/laurlen2112/election_analysis/blob/main/resources/step%202%20declare%20variables%20to%20track%20county%20turnout.png)). By changing the list, dictionary, and variables from the original code, the "for loop" and "if statement" can be customized to tabulate results by town.

Furthermore, our code can be extended to track votes in favor of ballot propositions by adding an extra "for loop" to track and tally votes and employing a nested "if statement" to determine the outcome. This new feature can be modeled after the "for loop" and "if statement" used to [track candidate votes](https://github.com/laurlen2112/election_analysis/blob/main/resources/candidate%20for%20and%20if%20statements.png). Our code is well-suited for this purpose, as it has already been successfully adapted to [tabulate voter turnout by county](https://github.com/laurlen2112/election_analysis/blob/main/resources/County%20Code%20Modeled%20after%20Candidate%20Code.png).

In light of the above, we respectfully request that the election commission consider licensing our code for future elections. We are available to answer any queries about our code's functionality and its capacity to handle future use cases. Thank you for your time and consideration.
