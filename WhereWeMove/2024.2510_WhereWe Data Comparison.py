# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os 
import palettable as pl #pip install palettable in the Anaconda terminal
import seaborn as sns
from seaborn import palplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#pip install pandas openpyxl

#Reading the original dataset
game = pd.read_excel('Game data.xlsx')
game.to_csv('Game data.csv', index=False)
game = pd.read_csv('Game data.csv')

#Reading the checked dataset
game_checked = pd.read_excel('240902_Analysed Game data.xlsx', sheet_name='Game Data')
game_checked.to_csv('Game checked.csv', index=False)
game_checked = pd.read_csv('Game checked.csv')

#Extracting the headers of the original dataset for comparison
column_headers = list(game.columns.values)

#Comparing the initial and checked game dataset to categorise the errors type
# gamevschecked = game[["PlayerID","Round"]]
# for item in column_headers[2:]:    
#     com_game = game[["PlayerID","Round",item]]
#     com_checked = game_checked[["PlayerID","Round",item]]
#     compareColumn = []
#     for index, row_checked in com_checked.iterrows():#iterate each row in the dataframe
#         for jndex, row_game in com_game.iterrows():
#             if row_checked["PlayerID"] == row_game["PlayerID"] and row_checked["Round"] == row_game["Round"]:
#                 check = False
#                 if row_checked[item] == row_game[item]:
#                     compareColumn.append("OK")
#                     check = True
#                     break
#                 if check == False:
#                     compareColumn.append(row_checked[item])
#     #Using .loc[] to assign the result of the comparison
#     gamevschecked.loc[:, item] = compareColumn
# gamevschecked.to_excel("gamevschecked.xlsx", index=False)#saves the DataFrame without row indices and with the specified headers.

#Analysing how do players distribute their average income among the game choices?
# Sample data for area plot
# data = {
#     'A': [1, 2, 3, 4, 5],
#     'B': [2, 3, 4, 5, 6],
#     'C': [3, 4, 5, 6, 7]
#     }
# # Creating a DataFrame for area plot
# df = pd.DataFrame(data)

# # Sample data for stacked bar plot
# labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
# men_means = [20, 35, 30, 35]
# women_means = [25, 32, 34, 20]
# children_means = [10, 15, 20, 10]

# # Positions for the bars
# x = np.arange(len(labels))

# # Create a figure and axis
# fig, ax = plt.subplots(figsize=(10, 6))
# # Plotting the area chart
# df.plot(kind='area', alpha=0.4, stacked=True, ax=ax)

# # Plotting the stacked bar chart on the same axes
# ax.bar(x - 0.2, men_means, width=0.2, label='Men', align='center')
# ax.bar(x, women_means, width=0.2, bottom=men_means, label='Women', align='center')
# ax.bar(x + 0.2, children_means, width=0.2, bottom=np.array(men_means) + np.array(women_means), label='Children', align='center')

# # Customizing the plot
# ax.set_title('Area and Stacked Bar Chart Combined')
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()

# Adjust layout and display the plot
# plt.tight_layout()
# plt.show()

tips = pd.read_csv("SampleFiles/tips.csv")
print(tips.head(4))#head() method returns a specified number of rows, string from the top. Default value is 5
df = (tips
      .groupby("sex")["smoker"]
      .value_counts(normalize=True)
      .mul(100)#The mul() method multiplies each value in the DataFrame with a specified value.
      .round(2)
      .unstack())
print(df)

fig, ax = plt.subplots(figsize = (12,6))
ax.bar(df.index, df["No"], label = "No", width = 0.3)
ax.bar(df.index, df["Yes"], bottom = df.No, label = "Yes", width = 0.3)  

income_dist_labels = ["PlayerID","Round", "Income", "LivingCost", "Savings", "SpendableIncome", "PayingDebt", "PayingSatisfaction", "PayingMeasures"]
income_dist_data = game.loc[:, income_dist_labels]
# Convert None to NaN
income_dist_data = income_dist_data.replace({"nan": np.nan})
income_dist_plt = income_dist_data.groupby("Income")
                   

