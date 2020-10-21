import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import xlsxwriter
import os
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error, mean_squared_log_error

userSelection = 'Singapore'

# Dataframes
data1 = pd.read_excel("../Datasets/SAMPLE - Agriculture, forestry, and fishing, value added (% of GDP).xlsx")
data2 = pd.read_excel("../Datasets/SAMPLE - Arable land (% of land area).xlsx")
data3 = pd.read_excel("../Datasets/SAMPLE - GDP per capita (constant LCU).xlsx")
sgrow1 = data1.loc[data1['Country Name'] == userSelection]
sgrow2 = data2.loc[data2['Country Name'] == userSelection]
sgrow3 = data3.loc[data3['Country Name'] == userSelection]

# Transposing columns and rows
sgcol3 = sgrow3.T
sgcol1 = sgrow1.T
sgcol2 = sgrow2.T
sgcol3 = sgrow3.T

# Concatenating the different factors into 1 dataframe
df = pd.concat([sgcol3, sgcol1, sgcol2], axis=1)
df.columns = ['GDP', 'Agriculture', 'Arable Land']
df.drop(['Series Name', 'Series Code', 'Country Name', 'Country Code'], axis=0, inplace=True)
df = pd.DataFrame(df, dtype=float)

# Making of a line graph
ax = sns.lineplot(x='Arable Land', y='GDP', data=df)
plt.show()

# Correlation value of GDP vs factor (requires a for loop implementation)
col1 = df["GDP"]
col2 = df["Agriculture"]
correlation = col1.corr(col2)
print(correlation)
