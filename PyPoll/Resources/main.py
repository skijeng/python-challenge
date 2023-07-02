import csv
import os
import pandas as pd
from pathlib import Path

#pulling the csv file
Poll = Path('/Users/jesserinskeys/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

#store the csv data in a data frame
df = pd.read_csv(Poll)

print('----------------------------------------')
print('Election Results')
print('----------------------------------------')

#count the number of votes
vote_count = df['County'].count()
print(f'Total Votes: {vote_count}')

#locate all the rows where Charles Casper Stockham was voted for
df_Charles = df.loc[df['Candidate'] == 'Charles Casper Stockham']
#count the number of rows/votes for Charles Casper Stockham
df_CharlesCount = df_Charles['County'].count()
#find the percentage of votes for Charles
df_CharlesPercent = (df_CharlesCount/vote_count) * 100
#Round the perchantage to 3 decimals
df_CharlesPer = round(df_CharlesPercent, 3)
#Display the total votes and percentage for Charles
print(f'Charles Casper Stockham: {df_CharlesPer}% ({df_CharlesCount})')

#locate all the rows where Diana was voted for
df_Diana = df.loc[df['Candidate'] == 'Diana DeGette']
#count the number of rows/votes for Diana
df_DianaCount = df_Diana['County'].count()
#find the percentage of votes for Diana
df_DianaPercentage = (df_DianaCount/vote_count) * 100
#round this percentage to 3 decimals
df_DianaPer = round(df_DianaPercentage, 3)
#display the total and percetage of votes for Diana
print(f'Diana DeGette: {df_DianaPer}% ({df_DianaCount})')

#locate all the rows where Raymon was voted for
df_Raymon = df.loc[df['Candidate'] == 'Raymon Anthony Doane']
#count the number of rows/votes for Raymon
df_RaymonCount = df_Raymon['County'].count()
#find the percentage of votes for Raymon
df_RaymonPercentage = (df_RaymonCount/vote_count) * 100
#round the percentage to 3 decimals
df_RaymonPer = round(df_RaymonPercentage, 3)
#display the total and percentage votes for Raymon
print(f'Raymon Anthony Doane: {df_RaymonPer}% ({df_RaymonCount})')

print('----------------------------------------')

#Create a dataframe containing the total votes for each candidate
TotalsData = [['Charles Casper Stockham' , df_CharlesCount] , ['Diana DeGette' , df_DianaCount] , ['Raymon Anthony Doane' , df_RaymonCount]]
df_totals = pd.DataFrame(TotalsData, columns=['Candidate' , 'TotalVotes'])

#find the winner using the above data frame
win = df_totals.loc[df_totals['TotalVotes'].idxmax()]
winner = win.drop('TotalVotes')

#display the winner
print(f'The winner is {winner.to_string(index=False)}')

print('----------------------------------------')


#export all the printed information to a text file
PyPollOutput = open('PyPollOutput.txt' , 'w')
PyPollOutput.write('----------------------------------------' + '\n')
PyPollOutput.write('Election Results' + '\n')
PyPollOutput.write('----------------------------------------' + '\n')
PyPollOutput.write(f'Total Votes: {vote_count}' + '\n')
PyPollOutput.write(f'Charles Casper Stockham: {df_CharlesPer}% ({df_CharlesCount})' + '\n')
PyPollOutput.write(f'Diana DeGette: {df_DianaPer}% ({df_DianaCount})' + '\n')
PyPollOutput.write(f'Raymon Anthony Doane: {df_RaymonPer}% ({df_RaymonCount})' + '\n')
PyPollOutput.write('----------------------------------------' + '\n')
PyPollOutput.write(f'The winner is {winner.to_string(index=False)}' + '\n')
PyPollOutput.write('----------------------------------------')
PyPollOutput.close




