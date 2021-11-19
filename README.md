# Election_Analysis

## Overview of Election Audit

A Colorado elections committee provided the results of their recently concluded local elections. With over 360,000 ballots cast for three candidates in three different counties, the main objective of this project is to determine the winner of the election based on popular vote. In addition, the following results are also to be determined and recorded: total number of votes cast, a complete list of candidates who received votes, total number of votes each candidate received and the percentage of votes each candidate won. The election results is also to be audited and the following information analyzed, recorded and reported: the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout.

Python was utilized to formulate and write the code to complete the goal, and the execution was done in visual studio code. In general, the analysis compriprsed of creating list and dictionaries, initialzing variables to store and or count data and writing code to loop through the data to collect the necessary information to complete the aim.

## Resources

* Data source: election-results.csv
* Software: Python 3.7.6, Visual Studio Code 1.62.2

## Election-Audit Results

* The total number of votes cast in the election was 369,711.

* The percentage of total votes and the number of votes for each county in the precinct is presented below
   * Jefferson: 10.5% (38,855)
   * Denver:    82.8% (306,055)
   * Arapahoe:  6.7%  (24,801)

* Denver had the largest number of votes, 306,055. The number of votes in Denver represented 82.8% of the total number of votes. 

* The results for each candidate from the election is summarized below.
   * Charles Casper Stokham received 23.0 % of the votes and 85,213 number of votes
   * Diana Degette received 73.8 % of the votes and 272,892 number of votes
   * Raymon Anthony Doane received 3.1 % of the votes and 11,606 number of votes

* The winner of the election was Diana DeGette. Diana receieved  272,892 votes, which accounts for 73.8% of the total votes.


## Summary

The presented script works well in predicitng the election results. By defining some of the variables as global variables, accurate and reliable results can be obtained for any number of canadiates and counties. This means the code is highly adaptable. However, if the script is to be used for other elections, some modifications may be necessary to ensure its adaptable. Two examples of such modifications include writing a code to check for duplicate (or more) votes and....To preserve the integrity of the election, especially at a larger scale where fraud may be more prominent, it will be important to have a code that loops through the rows to ensure all ballot ID is unique  

