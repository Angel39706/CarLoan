from pickle import TRUE
import pandas as pd
import numpy as np

#reads .csv file into  the data frame
df = pd.read_csv('car_loan.csv')

#exports panda files information into a out.csv
export_csv = df.to_csv(r'out.csv')

#renames columns
df = df.rename(columns={'Starting Balance':'starting_balance','Interest Paid':'interest_paid', 'Principal Paid':'principal_paid','New Balance':'new_balance'})
#removes columns
df = df.drop(['Repayment', 'term'], axis = 1)

#display if interest was paid (boolean expression)
interest_missing = df['interest_paid'].isna()

#displays how much was paid(float)
numMissing = df.loc[:, 'interest_paid']

#prints the total amount of interest paid
total_interest_paid = df['interest_paid'].sum()

#comand to run previous functions
df_info = df.info()

#prints all information from data frame
print(df_info)

#prints how much is paid
print(interest_missing)


print(numMissing)
df.dropna(inplace= True)

#displays the total amount of interest paid
print(total_interest_paid)

# Displays the sum of all values for each column
print(df.sum())

#displays class 'numpy.ndarray'>
df.to_numpy()

#imports libraries that are needed
from matplotlib import pyplot as plt

import seaborn as sns

# reads out file with removed nan and sets it to df
df= pd.read_csv('out.csv')

# focus on one columns value for future use
month_numbe    = df.loc[:,'Month'].values
interest_paid  = df.loc[:,'Interest Paid'].values
principal_paid = df.loc[:,'Principal Paid'].values
#drops the nan value for acurrate graph
df.dropna(inplace= True)

#prints <class 'numpy.ndarray'>
print(type(month_numbe))

# creates x and y axis for plotting
x1 = df['Interest Paid']
y = df['Month']
#plots x and y axis for interest paid with dispay a black colored line


#plots principal payed as x2 with blue colored line
x2 = df['Principal Paid']


from matplotlib import style
 #displays the names of different styles that are available along with the syntax
print(plt.style.available)
 #one of many styles that are available
plt.style.use('seaborn')


#I had to plot the lines after style in order to have the style to actually work
plt.plot(y,x1, color = 'black')
plt.plot(y,x2, color = 'blue')

#addes labels to the graphs to make it more appealing/knowing what is being displayed
title_font = {'size': 12}
plt.title('Interest and Principal Paid Each Month ',**title_font)
plt.xlabel('Month',**title_font )
plt.ylabel('Cost $',**title_font)
plt.legend(['Interest Paid','Principal Paid'],loc='center right')

#displays both lines on one graph
plt.show()

