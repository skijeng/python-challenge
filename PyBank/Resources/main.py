import csv
import os
import pandas as pd
from pathlib import Path

#import budget data using path
budget_data = Path('/Users/jesserinskeys/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

#read budget data csv file into a data frame
df = pd.read_csv(budget_data)

#view the main data frame
df.head()

print('----------------------------------------')

print('Financial Analysis')

print('----------------------------------------')

#count the number of months
df_count = df['Date'].count()
print(f'Total Months: {df_count}')

#count the total profit
df_sum = df['Profit/Losses'].sum()
print(f'Total Value: ${df_sum}')

#find the changes between months
Change = df['Profit/Losses'].diff()
ChangeLocMax = Change.idxmax()
ChangeLocMin = Change.idxmin()

#find the mean change
ChangeSum = Change.sum()
ChangeMean = ChangeSum / 85
Mean = round(ChangeMean, 2)
print(f'Average Change: ${Mean}')

#find the greatest increase in profit
MaxProfit = Change.max()
MaxDate = df['Date'].iloc[ChangeLocMax]
print(f'Greatest Increase in Profits: {MaxDate} ${MaxProfit}')

#find the greatest decrease in profit
MinProfit = Change.min()
MinDate = df['Date'].iloc[ChangeLocMin]
print(f'Greatest Decrease in Profits: {MinDate} ${MinProfit}')


#Export the Output to a txt file
PyBankOutput = open('PyBankOutput.txt' , 'w')
PyBankOutput.write('----------------------------------------' + '\n')
PyBankOutput.write('Financial Analysis'+ '\n')
PyBankOutput.write('----------------------------------------'+ '\n')
PyBankOutput.write(f'Total Months: {df_count}'+ '\n')
PyBankOutput.write(f'Total Value: ${df_sum}'+ '\n')
PyBankOutput.write(f'Average Change: ${Mean}'+ '\n')
PyBankOutput.write(f'Greatest Increase in Profits: {MaxDate} ${MaxProfit}'+ '\n')
PyBankOutput.write(f'Greatest Decrease in Profits: {MinDate} ${MinProfit}'+ '\n')
PyBankOutput.close


