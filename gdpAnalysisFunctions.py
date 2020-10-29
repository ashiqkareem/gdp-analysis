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
import requests
import zipfile
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_squared_log_error
from pandastable import Table
from pandastable import config

# Function that creates a dataframe for the selected country
def dataframeCreation(singleCountry):
    # Pathways to various datasets used
    dataGDP = pd.read_csv('../gdp-analysis/rawDataSet/GDP, PPP (current international $).csv')
    dataAgri = pd.read_csv('../gdp-analysis/rawDataSet/Agriculture, forestry, and fishing, value added (% of GDP).csv')
    dataArab = pd.read_csv('../gdp-analysis/rawDataSet/Arable land (% of land area).csv')
    dataBirth = pd.read_csv('../gdp-analysis/rawDataSet/Birth rate, crude (per 1,000 people).csv')
    dataDeath = pd.read_csv('../gdp-analysis/rawDataSet/Death rate, crude (per 1,000 people).csv')
    dataIndiv = pd.read_csv('../gdp-analysis/rawDataSet/Individuals using the Internet (% of population).csv')
    dataIndus = pd.read_csv('../gdp-analysis/rawDataSet/Industry (including construction), value added (% of GDP).csv')
    dataMobile = pd.read_csv('../gdp-analysis/rawDataSet/Mobile cellular subscriptions (per 100 people).csv')
    dataMort = pd.read_csv('../gdp-analysis/rawDataSet/Mortality rate, infant (per 1,000 live births).csv')
    dataCrop = pd.read_csv('../gdp-analysis/rawDataSet/Permanent cropland (% of land area).csv')
    dataPopDen = pd.read_csv('../gdp-analysis/rawDataSet/Population density (people per sq. km of land area).csv')
    dataPop = pd.read_csv('../gdp-analysis/rawDataSet/Population, total.csv')
    dataServ = pd.read_csv('../gdp-analysis/rawDataSet/Services, value added (% of GDP).csv')

    #Selecting row based on country selected
    rowGDP = dataGDP.loc[dataGDP['Country Name'] == singleCountry]
    rowAgri = dataAgri.loc[dataAgri['Country Name'] == singleCountry]
    rowArab = dataArab.loc[dataArab['Country Name'] == singleCountry]
    rowBirth = dataBirth.loc[dataBirth['Country Name'] == singleCountry]
    rowDeath = dataDeath.loc[dataDeath['Country Name'] == singleCountry]
    rowIndiv = dataIndiv.loc[dataIndiv['Country Name'] == singleCountry]
    rowIndus = dataIndus.loc[dataIndus['Country Name'] == singleCountry]
    rowMobile = dataMobile.loc[dataMobile['Country Name'] == singleCountry]
    rowMort = dataMort.loc[dataMort['Country Name'] == singleCountry]
    rowCrop = dataCrop.loc[dataCrop['Country Name'] == singleCountry]
    rowPopDen = dataPopDen.loc[dataPopDen['Country Name'] == singleCountry]
    rowPop = dataPop.loc[dataPop['Country Name'] == singleCountry]
    rowServ = dataServ.loc[dataServ['Country Name'] == singleCountry]

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

    # Concatenating the different factors into 1 dataframe
    df = pd.concat([colGDP, colAgri, colArab, colBirth, colDeath, colIndiv, colIndus, colMobile, colMort, colCrop,
                    colPopDen, colPop, colServ], axis=1)
    df.columns = ['GDP', 'Agriculture', 'Arable Land', 'Birth Rate', 'Death Rate', 'Individuals using Internet', 'Industry',
                  'Mobile Subscriptions', 'Mortality Rate', 'Cropland', 'Population Density', 'Population', 'Services']
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

    # Check to see if dataframe is empty or not
    if df.empty:
        return False
    else:
        return df

# Tab 1 -Function that allows for downloading of datasets
def download_zip():
    url = 'https://raw.github.com/ashiqkareem/gdp-analysis/master/files.zip'

    r = requests.get(url)
    with open("files.zip", "wb") as code:
        code.write(r.content)

    tk.messagebox.showinfo("Success", "Download completed successfully!")

# Tab 1 - Function that allows for importing of datasets

def unzip():
    with zipfile.ZipFile('files.zip', 'r') as my_zip:
        my_zip.extractall('Datasets')

        # Dataframes
        path ="../gdp-analysis/rawDataSet/"
        dataGDP = pd.read_csv(path + 'GDP, PPP (current international $).csv')
        dataAgri = pd.read_csv(path + 'Agriculture, forestry, and fishing, value added (% of GDP).csv')
        dataArab = pd.read_csv(path + 'Arable land (% of land area).csv')
        dataBirth = pd.read_csv(path + 'Birth rate, crude (per 1,000 people).csv')
        dataDeath = pd.read_csv(path + 'Death rate, crude (per 1,000 people).csv')
        dataIndiv = pd.read_csv(path + 'Individuals using the Internet (% of population).csv')
        dataIndus = pd.read_csv(path + 'Industry (including construction), value added (% of GDP).csv')
        dataMobile = pd.read_csv(path + 'Mobile cellular subscriptions (per 100 people).csv')
        dataMort = pd.read_csv(path + 'Mortality rate, infant (per 1,000 live births).csv')
        dataCrop = pd.read_csv(path + 'Permanent cropland (% of land area).csv')
        dataPopDen = pd.read_csv(path + 'Population density (people per sq. km of land area).csv')
        dataPop = pd.read_csv(path + 'Population, total.csv')
        dataServ = pd.read_csv(path + 'Services, value added (% of GDP).csv')
        dataArea = pd.read_csv(path + 'Surface area (sq. km).csv')
        
    tk.messagebox.showinfo("Success", "Import completed successfully!")

# Prerequisites for Tab 2 - Correlation value of GDP vs Factor
def corrGDPDict(dataframe):
    df = dataframe
    if df is False:
        tk.messagebox.showinfo("Error", "Insufficient data")
        return 0
    else:
        corrDict = {}
        for i in range(1, len(df.columns)):
            col1 = df['GDP']
            col2 = df[df.columns[i]]
            correlation = col1.corr(col2)
            corrDict[df.columns[i]] = correlation
        GDPCorrDict = sorted(corrDict.items(), key=lambda x: x[1], reverse=True)
        return GDPCorrDict


# Prerequisites for Tab 2 - Correlation Dictionary
def dict(dataframe):
    df = dataframe
    if df is False:
        tk.messagebox.showinfo("Error", "Insufficient data")
        return 0
    else:
        corrDict = {}
        for i in range(1, len(df.columns)):
            col1 = df['GDP']
            col2 = df[df.columns[i]]
            correlation = col1.corr(col2)
            corrDict[df.columns[i]] = correlation
        # print(corrDict)
        return corrDict


# Tab 2 - Function that displays Correlation Table
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


# Tab 2 - Function that displays heatmap consisting correlation values
def heatMap(dataframe, country):
    df = dataframe
    if df is False:
        tk.messagebox.showinfo("Error", "Insufficient data")
    else:
        plt.figure("%s - Correlation Values In Heatmap"%country,figsize=(12, 6))
        sns.heatmap(data=df.iloc[:, 0:].corr(), annot=True, fmt='.2f', cmap='coolwarm')
        plt.tight_layout()
        plt.show()
    


# Tab 2 - Function that displays GDP Factor graph
def displayFactorsGraph(dict, dataframe, country):
    GDPCorrDict = dict
    df = dataframe
    plt.figure("%s - GDP Factors"%country, figsize=(12,6))
    plt.suptitle("GDP Factors")
    for i in range(len(GDPCorrDict)):
        plt.subplot(5, 3, i + 1)
        sns.lineplot(x=GDPCorrDict[i][0], y='GDP', data=df)
    plt.tight_layout()
    plt.show()


# Tab 2 - Simple Linear Regression Models (GDP vs Factors)
def displayLinearRegFactor(dataframe, country):
    df = dataframe
    if df is False:
        tk.messagebox.showinfo("Error", "Insufficient data")
    else:
        x = 0
        for i in df.columns:
            if i == 'GDP':
                pass
            else:
                plt.figure("%s - Simple Linear Regression Models"%country, figsize=(12, 6))
                plt.subplot(5, 3, x + 1)
                x += 1
                X = df[i].values.reshape(-1, 1)
                Y = df['GDP'].values.reshape(-1, 1)
                lr = LinearRegression()
                lr.fit(X, Y)
                y_pred = lr.predict(X)
                plt.scatter(X, Y, s=5)
                plt.plot(X, y_pred, color='red')
                # plt.title(i + ' - (Simple Linear Regression Model)') # Better Graph Title
                plt.xlabel(i)
                plt.ylabel('GDP')
        plt.tight_layout()
        plt.show()


# Tab 2 - Function that predicts the GDP value of a country/countries
def linearReg(countryInput, dataframe):
    df = dataframe
    if df is False:
        tk.messagebox.showinfo("Error", "Insufficient data")
    else:
        X = df.index.values.reshape(-1, 1)
        Y = df['GDP'].values.reshape(-1, 1)
        lr = LinearRegression()
        lr.fit(X, Y)
        y_pred = lr.predict(X)
        plt.scatter(X, Y, s=10)
        plt.plot(X, y_pred, color='red')
        # plt.title(countryInput + "'s Best Fit Line") # Better Graph Title
        plt.xlabel('Years')
        plt.ylabel('GDP, PPP (current international $)')
        plt.show()
        # print(countryInput, lr.predict([[yearInput]]))


# Tab 2 - Function that allows user to view factor specific data
def displayFactor(country, dataframe, factor):
    countryName = country
    df = dataframe
    if df is False:
        tk.messagebox.showinfo("Error", "Insufficient data")
    else:
        dfFactor = df[factor]
        df = pd.concat([dfFactor], axis=1)
        window = tk.Toplevel()
        window.title(countryName + " - " + factor + ' Data')
        f = Frame(window)
        f.pack(fill=BOTH, expand=1)
        pt = Table(f, dataframe=df, showstatusbar=True, width=200, height=300)
        options = {'cellwidth': 150, 'floatprecision': 4, 'align': 'center'}
        config.apply_options(options, pt)
        pt.showIndex()
        pt.show()


# Tab 2 - Function that allows users to export all datasets for country
def exportCSV(dataframe, country):
    df = dataframe
    if df is False:
        tk.messagebox.showinfo("Error", "Insufficient data")
    else:
        df.to_csv(r'../gdp-analysis/output/'+country+'.csv', index=True)

# Checking whether functions work here

def countryList():
    countries = ['United States', 'China', 'India', 'Japan', 'Germany', 'Russian Federation', 'Brazil',
                 'United Kingdom', 'France', 'Indonesia', 'Italy', 'Mexico', 'Turkey', 'Korea, Rep.', 'Spain',
                 'Canada', 'Saudi Arabia', 'Australia', 'Thailand', 'Iran, Islamic Rep.', 'Egypt, Arab Rep.', 'Poland',
                 'Nigeria', 'Pakistan', 'Argentina', 'Netherlands', 'Malaysia', 'Philippines', 'South Africa',
                 'Colombia']
    return countries

def linearReg2(countryInput, yearInput, dataframe):
    df = dataframe
    X = df.index.values.reshape(-1, 1)
    Y = df['GDP'].values.reshape(-1, 1)
    lr = LinearRegression()
    lr.fit(X, Y)
    y_pred = lr.predict(X)
    plt.scatter(X, Y, s=10)
    plt.plot(X, y_pred, color='red')
    plt.title(countryInput + "'s Best Fit Line") # Better Graph Title
    plt.xlabel('Years')
    plt.ylabel('GDP, PPP (current international $)')
    # plt.show()
    return countryInput, lr.predict([[yearInput]])

# Tab 3 - Functions that displays GDP of all countries in Year X
def allYearsGDPPrediction(countries, predictionYear):
    df = pd.DataFrame(columns=['Countries', 'GDP in 2015', 'Predicted GDP in '+ str(predictionYear)])
    for i in countries:
        if dataframeCreation(i) is False:
            print(i + "'s dataframe is empty!")
            df = df.append(pd.Series([i, 'No Data To Make Prediction'], index=df.columns), ignore_index=True)
        else:
            pred1 = linearReg2(i, 2015, dataframeCreation(i))[1][0][0]
            pred2 = linearReg2(i, predictionYear, dataframeCreation(i))[1][0][0]
            df = df.append(pd.Series([i, pred1, pred2], index=df.columns), ignore_index=True)
            df.index += 1
    window = tk.Toplevel()
    window.title("All Countries' GDP Prediction in the year: %s" % predictionYear)
    f = Frame(window)
    f.pack(fill=BOTH, expand=1)
    pt = Table(f, dataframe=df, showstatusbar=True, width=200, height=300)
    options = {'cellwidth': 150, 'floatprecision': 4, 'align': 'center'}
    config.apply_options(options, pt)
    pt.showIndex()
    pt.show()
    return df