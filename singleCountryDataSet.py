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
dataGDP = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - GDP per capita (constant LCU).xlsx')
dataAgri = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Agriculture, forestry, and fishing, value added (% of GDP).xlsx')
dataArab = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Arable land (% of land area).xlsx')
dataBirth = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Birth rate, crude (per 1,000 people).xlsx')
dataDeath = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Death rate, crude (per 1,000 people).xlsx')
dataIndiv = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Individuals using the Internet (% of population).xlsx')
dataIndus = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Industry (including construction), value added (% of GDP).xlsx')
dataMobile = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Mobile cellular subscriptions (per 100 people).xlsx')
dataMort = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Mortality rate, infant (per 1,000 live births).xlsx')
dataMig = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Net migration.xlsx')
dataCrop = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Permanent cropland (% of land area).xlsx')
dataPopDen = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Population density (people per sq. km of land area).xlsx')
dataPop = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Population, total.xlsx')
dataServ = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Services, value added (% of GDP).xlsx')
dataArea = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Surface area (sq. km).xlsx')

#Selecting row based on country selected
rowGDP = dataGDP.loc[dataGDP['Country Name'] == userSelection]
rowAgri = dataAgri.loc[dataAgri['Country Name'] == userSelection]
rowArab = dataArab.loc[dataArab['Country Name'] == userSelection]
rowBirth = dataBirth.loc[dataBirth['Country Name'] == userSelection]
rowDeath = dataDeath.loc[dataDeath['Country Name'] == userSelection]
rowIndiv = dataIndiv.loc[dataIndiv['Country Name'] == userSelection]
rowIndus = dataIndus.loc[dataIndus['Country Name'] == userSelection]
rowMobile = dataMobile.loc[dataMobile['Country Name'] == userSelection]
rowMort = dataMort.loc[dataMort['Country Name'] == userSelection]
rowMig = dataMig.loc[dataMig['Country Name'] == userSelection]
rowCrop = dataCrop.loc[dataCrop['Country Name'] == userSelection]
rowPopDen = dataPopDen.loc[dataPopDen['Country Name'] == userSelection]
rowPop = dataPop.loc[dataPop['Country Name'] == userSelection]
rowServ = dataServ.loc[dataServ['Country Name'] == userSelection]
rowArea = dataArea.loc[dataArea['Country Name'] == userSelection]

# Transposing columns and rows
colGDP = rowGDP.T
colAgri = rowAgri.T
colArab = rowArab.T
colBirth = rowBirth.T
colDeath = rowDeath.T
colIndiv = rowIndiv.T
colIndus = rowIndus.T
colMobile = rowMobile.T
colMort = rowMort.T
colMig = rowMig.T
colCrop = rowCrop.T
colPopDen = rowPopDen.T
colPop = rowPop.T
colServ = rowServ.T
colArea = rowArea.T

# Concatenating the different factors into 1 dataframe
df = pd.concat([colGDP, colAgri, colArab, colBirth, colDeath, colIndiv, colIndus, colMobile, colMort, colMig, colCrop, colPopDen,
                colPop, colServ, colArea], axis=1)
df.columns = ['GDP', 'Agriculture', 'Arable Land', 'Birth Rate', 'Death Rate', 'Individual Internet usage', 'Industry',
              'Mobile Subscriptions', 'Mortality Rate','Migration Net','Cropland','Population Density','Population',
              'Services', 'Surface Area']
df.drop(['Series Name', 'Series Code', 'Country Name', 'Country Code'], axis=0, inplace=True)
df = pd.DataFrame(df, dtype=float)

# Making of a line graph
plt.figure(1)
sns.lineplot(x='Agriculture', y='GDP', data=df)
plt.figure(2)
sns.lineplot(x='Arable Land', y='GDP', data=df)
plt.figure(3)
sns.lineplot(x='Birth Rate', y='GDP', data=df)
plt.show()

# Correlation value of GDP vs factor (requires a for loop implementation)
corrList = []
for i in range(1, len(df.columns)):
    col1 = df['GDP']
    col2 = df[df.columns[i]]
    correlation = col1.corr(col2)
    corrList.append(correlation)


print(corrList)

