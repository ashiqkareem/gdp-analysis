import re
import xlrd
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import xlsxwriter
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_squared_log_error

userSelection = 'Germany'

# Dataframes
dataGDP = pd.read_csv('../SampleGDPAnalysis/rawDataSet/GDP per capita (constant LCU).csv')
dataAgri = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Agriculture, forestry, and fishing, value added (% of GDP).csv')
dataArab = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Arable land (% of land area).csv')
dataBirth = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Birth rate, crude (per 1,000 people).csv')
dataDeath = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Death rate, crude (per 1,000 people).csv')
dataIndiv = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Individuals using the Internet (% of population).csv')
dataIndus = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Industry (including construction), value added (% of GDP).csv')
dataMobile = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Mobile cellular subscriptions (per 100 people).csv')
dataMort = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Mortality rate, infant (per 1,000 live births).csv')
dataCrop = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Permanent cropland (% of land area).csv')
dataPopDen = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Population density (people per sq. km of land area).csv')
dataPop = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Population, total.csv')
dataServ = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Services, value added (% of GDP).csv')
dataArea = pd.read_csv('../SampleGDPAnalysis/rawDataSet/Surface area (sq. km).csv')

# # print(dataGDP)
# rowGDP = dataGDP.loc[dataGDP['Country Name'] == userSelection]
# print(rowGDP.T)

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
colCrop = rowCrop.T
colPopDen = rowPopDen.T
colPop = rowPop.T
colServ = rowServ.T
colArea = rowArea.T

# Concatenating the different factors into 1 dataframe
df = pd.concat([colGDP, colAgri, colArab, colBirth, colDeath, colIndiv, colIndus, colMobile, colMort, colCrop,
                colPopDen, colPop, colServ, colArea], axis=1)
df.columns = ['GDP', 'Agriculture', 'Arable Land', 'Birth Rate', 'Death Rate', 'Individuals using Internet', 'Industry',
              'Mobile Subscriptions', 'Mortality Rate', 'Cropland', 'Population Density', 'Population', 'Services',
              'Surface Area']
df.drop(['Series Name', 'Series Code', 'Country Name', 'Country Code'], axis=0, inplace=True)
new_index = []
for i in df.index:
    x = re.split("\s", i)
    new_index.append(int(x[0]))
df['Years'] = new_index
df = df.set_index('Years')
df = df.replace('..', np.nan).dropna()
df = df.replace('...', np.nan).dropna()
df = df.dropna()
df = pd.DataFrame(df, dtype=float)
print(df)