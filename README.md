# Election_Analysis


## Election Project Overview
A Colorado State Board Elections employee has requested to help them to analysis the result and automate the process of counting of votes and provide them results of congressional election

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

## Resources
* Data provided by Colorado Board of Elections as : election_results.csv
* Tools Used: Visual Studio Code (1.51.1), Git Bash (2.29.2), Python (3.7.9)
* Stack Overflow

## Summary of Analysis
The analysis of the election is states that:

![election_analyis](https://github.com/shivam0921/Election_Analysis/blob/main/analysis/election_analysis.txt)

Total Votes: 369,711

*Candidates with there respective results:*
  
  * Charles Casper Stockham: 23.0% (85,213)
  
  * Diana DeGette: 73.8% (272,892)
  
  * Raymon Anthony Doane: 3.1% (11,606)

 *Winning Candidate*
  
 * Winner: Diana DeGette
  
 * Winning Vote Count: 272,892
  
 * Winning Percentage: 73.8%

*Vote Percentage By County*
  
  * Jefferson: 10.5% (38,855)

  * Denver: 82.8% (306,055)

  * Arapahoe: 6.7% (24,801)


## Election Challenge Overview
 A Colorado State Board Elections  has requested to help them to analysis the result and automate the process of counting of votes and provide them results of congressional election. This solution will help the board to go more depth in the process and saves them a lot of time in reviewing the results.

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote
6. The total voters in each County
7.Percentage of Voters in each County
8. County with the highest number of voters

![election_analyis](https://github.com/shivam0921/Election_Analysis/blob/main/PyPoll%20Challenge/Resources/election_analysis_challenge_results.PNG)

## Election Challenge Summary
The script provided to the colorado election state board will help them analysis in future with very less changes to the script. They can use the script among different districts and automate the process of counting the votes.
With making some changes to the script we can connect to different database engines after adding this to code:
from sqlalchemy import create_engine.
import numpy as np.
from os import walk.
import pandas as pd.
from tldextract import extract.
The election board can also add more data attributes and we can do more in-depth analyis.



