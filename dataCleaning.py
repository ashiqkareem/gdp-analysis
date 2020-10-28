import re
import xlrd
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import *
import xlsxwriter
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_squared_log_error
from pandastable import Table
from pandastable import config

# Function that creates a dataframe for the selected country
def dataframeCreation(userSelection):
    dataGDP = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/GDP (current USD).csv')
    dataAgri = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Agriculture, forestry, and fishing, value added (% of GDP).csv')
    dataArab = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Arable land (% of land area).csv')
    dataBirth = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Birth rate, crude (per 1,000 people).csv')
    dataDeath = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Death rate, crude (per 1,000 people).csv')
    dataIndiv = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Individuals using the Internet (% of population).csv')
    dataLit = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Literacy rate, adult total (% of people ages 15 and above).csv')
    dataIndus = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Industry (including construction), value added (% of GDP).csv')
    dataMobile = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Mobile cellular subscriptions (per 100 people).csv')
    dataMort = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Mortality rate, infant (per 1,000 live births).csv')
    dataCrop = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Permanent cropland (% of land area).csv')
    dataPopDen = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Population density (people per sq. km of land area).csv')
    dataPop = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Population, total.csv')
    dataServ = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Services, value added (% of GDP).csv')
    dataArea = pd.read_csv('D:/Git/1002 VS/gdp-analysis/rawDataSet/Surface area (sq. km).csv')

    #Selecting row based on country selected
    rowGDP = dataGDP.loc[dataGDP['Country Name'] == userSelection]
    rowAgri = dataAgri.loc[dataAgri['Country Name'] == userSelection]
    rowArab = dataArab.loc[dataArab['Country Name'] == userSelection]
    rowBirth = dataBirth.loc[dataBirth['Country Name'] == userSelection]
    rowDeath = dataDeath.loc[dataDeath['Country Name'] == userSelection]
    rowIndiv = dataIndiv.loc[dataIndiv['Country Name'] == userSelection]
    rowIndus = dataIndus.loc[dataIndus['Country Name'] == userSelection]
    rowLit = dataLit.loc[dataLit['Country Name'] == userSelection]
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
    colLit = rowLit.T
    colMobile = rowMobile.T
    colMort = rowMort.T
    colCrop = rowCrop.T
    colPopDen = rowPopDen.T
    colPop = rowPop.T
    colServ = rowServ.T
    colArea = rowArea.T

    # Concatenating the different factors into 1 dataframe
    df = pd.concat([colGDP, colAgri, colArab, colBirth, colDeath, colIndiv, colIndus, colLit, colMobile, colMort, colCrop,
                    colPopDen, colPop, colServ, colArea], axis=1)
    df.columns = ['GDP', 'Agriculture', 'Arable Land', 'Birth Rate', 'Death Rate', 'Individuals using Internet', 'Industry',
                  'Literacy','Mobile Subscriptions', 'Mortality Rate', 'Cropland', 'Population Density', 'Population', 'Services',
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

    return df

# Correlation value of GDP vs factor (requires a for loop implementation)
def corrGDPDict(dataframe):
    df = dataframe
    corrDict = {}
    for i in range(1, len(df.columns)):
         col1 = df['GDP']
         col2 = df[df.columns[i]]
         correlation = col1.corr(col2)
         corrDict[df.columns[i]] = correlation
    GDPCorrDict = sorted(corrDict.items(), key=lambda x: x[1], reverse=True)
    return GDPCorrDict

# Correlation Dictionary
def dict(dataframe):
    df = dataframe
    corrDict = {}
    for i in range(1, len(df.columns)):
         col1 = df['GDP']
         col2 = df[df.columns[i]]
         correlation = col1.corr(col2)
         corrDict[df.columns[i]] = correlation
    # print(corrDict)
    return corrDict


# Display GDP Factor graph
def displayFactorsGraph(dict, dataframe):
    GDPCorrDict = dict
    df = dataframe
    plt.figure("GDP Factors", figsize=(12,6))
    plt.suptitle("GDP Factors")
    for i in range(len(GDPCorrDict)):
        plt.subplot(5, 3, i + 1)
        sns.lineplot(x=GDPCorrDict[i][0], y='GDP', data=df)
    plt.tight_layout()
    plt.show()


# Display Correlation Table
def displayCorrTable(dict,userSelection):
    corrDict = dict
    df = pd.DataFrame(data=corrDict, index=[0]).T
    df.columns = ['Correlation Value']
    window = tk.Toplevel()
    window.title('%s - GDP Factors correlation values' % userSelection)
    f = Frame(window)
    f.pack(fill=BOTH, expand=1)
    pt = Table(f, dataframe=df, showstatusbar=True, width=200, height=300)
    options = {'cellwidth': 150, 'floatprecision': 4, 'align': 'center'}
    config.apply_options(options, pt)
    pt.showIndex()
    pt.show()

# Linear Regression to predict GDP values
def linearReg(dataframe):
    df = dataframe
    Y = df.iloc[:, 0].values.reshape(-1, 1)
    X = df.index.values.reshape(-1, 1)
    lr = LinearRegression()
    lr.fit(X, Y)
    y_pred = lr.predict(X)
    plt.scatter(X, Y, s=10)
    plt.plot(X, y_pred, color='red')
    plt.title(userSelection + ' - GDP (Simple Linear Regression Model)') # Better Graph Title
    plt.xlabel('Years')
    plt.ylabel('GDP Per Capita (Constant LCU)')
    plt.show()
    print(lr.predict([[2050]]))

    # Heatmap to see general pattern in dataset
    plt.figure(figsize=(12, 12))
    sns.heatmap(data=df.iloc[:, 0:].corr(), annot=True, fmt='.2f', cmap='coolwarm')
    plt.show()

# # Showing Linear Regression Mathematical Scores (?)
# linReg = LinearRegression(normalize=True)
# linReg.fit(X, Y)
# print(linReg.score(X, Y))
# print(linReg.coef_)
# print(linReg.intercept_)

# Select a GDP Factor
def displayFactor(dataframe,factor):
    df = dataframe
    inputFactor = factor
    print(df[inputFactor])

# Exporting all datasets for country
def exportCSV(dataframe, country):
    df = dataframe
    df.to_csv(r'../gdp-analysis/output/'+country+'.csv', index=True)

# displayCorrTable(dict(dataframeCreation("China")))
# mainloop()