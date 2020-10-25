import numpy as np
import pandas as pd
import seaborn as sns
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter as tkMessageBox
from pandastable import Table
from pandastable import config
from pandastable import IndexHeader
from matplotlib import pyplot as plt
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error, mean_squared_log_error
from matplotlib.pyplot import table



def countrySelect(country):
    return country


# userSelection = 'Singapore'

# Dataframes
# dataGDP = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - GDP per capita (constant LCU).xlsx')
# dataAgri = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Agriculture, forestry, and fishing, value added (% of GDP).xlsx')
# dataArab = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Arable land (% of land area).xlsx')
# dataBirth = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Birth rate, crude (per 1,000 people).xlsx')
# dataDeath = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Death rate, crude (per 1,000 people).xlsx')
# dataIndiv = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Individuals using the Internet (% of population).xlsx')
# dataIndus = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Industry (including construction), value added (% of GDP).xlsx')
# dataMobile = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Mobile cellular subscriptions (per 100 people).xlsx')
# dataMort = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Mortality rate, infant (per 1,000 live births).xlsx')
# #dataMig = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Net migration.xlsx')
# dataCrop = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Permanent cropland (% of land area).xlsx')
# dataPopDen = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Population density (people per sq. km of land area).xlsx')
# dataPop = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Population, total.xlsx')
# dataServ = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Services, value added (% of GDP).xlsx')
# dataArea = pd.read_excel('../gdp-analysis/Datasets/SAMPLE - Surface area (sq. km).xlsx')

#Selecting row based on country selected
# rowGDP = dataGDP.loc[dataGDP['Country Name'] == userSelection]
# rowAgri = dataAgri.loc[dataAgri['Country Name'] == userSelection]
# rowArab = dataArab.loc[dataArab['Country Name'] == userSelection]
# rowBirth = dataBirth.loc[dataBirth['Country Name'] == userSelection]
# rowDeath = dataDeath.loc[dataDeath['Country Name'] == userSelection]
# rowIndiv = dataIndiv.loc[dataIndiv['Country Name'] == userSelection]
# rowIndus = dataIndus.loc[dataIndus['Country Name'] == userSelection]
# rowMobile = dataMobile.loc[dataMobile['Country Name'] == userSelection]
# rowMort = dataMort.loc[dataMort['Country Name'] == userSelection]
# #rowMig = dataMig.loc[dataMig['Country Name'] == userSelection]
# rowCrop = dataCrop.loc[dataCrop['Country Name'] == userSelection]
# rowPopDen = dataPopDen.loc[dataPopDen['Country Name'] == userSelection]
# rowPop = dataPop.loc[dataPop['Country Name'] == userSelection]
# rowServ = dataServ.loc[dataServ['Country Name'] == userSelection]
# rowArea = dataArea.loc[dataArea['Country Name'] == userSelection]

# Transposing columns and rows
# colGDP = rowGDP.T
# colAgri = rowAgri.T
# colArab = rowArab.T
# colBirth = rowBirth.T
# colDeath = rowDeath.T
# colIndiv = rowIndiv.T
# colIndus = rowIndus.T
# colMobile = rowMobile.T
# colMort = rowMort.T
# #colMig = rowMig.T
# colCrop = rowCrop.T
# colPopDen = rowPopDen.T
# colPop = rowPop.T
# colServ = rowServ.T
# colArea = rowArea.T

# Concatenating the different factors into 1 dataframe
# df = pd.concat([colGDP, colAgri, colArab, colBirth, colDeath, colIndiv, colIndus, colMobile, colMort, colCrop, colPopDen,
#                 colPop, colServ, colArea], axis=1)
# df.columns = ['GDP', 'Agriculture', 'Arable Land', 'Birth Rate', 'Death Rate', 'Individual Internet usage', 'Industry',
#               'Mobile Subscriptions', 'Mortality Rate','Cropland','Population Density','Population',
#               'Services', 'Surface Area']
# df.drop(['Series Name', 'Series Code', 'Country Name', 'Country Code'], axis=0, inplace=True)
# df = pd.DataFrame(df, dtype=float)

# Correlation value of GDP vs factor (requires a for loop implementation)
# corrDict = {}
# for i in range(1, len(df.columns)):
#     col1 = df['GDP']
#     col2 = df[df.columns[i]]
#     correlation = col1.corr(col2)
#     corrDict[df.columns[i]] = correlation

# GDPCorrDict = sorted(corrDict.items(), key=lambda x: x[1], reverse=True)
# Bot3CorrDict = sorted(corrDict.items(), key=lambda x: x[1], reverse=True)[-3:]



# Display GDP Factor graph
def displayFactorsGraph(userSelection):
    plt.figure("GDP Factors")
    plt.suptitle("%s GDP Factors" %userSelection)
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
    df = pd.concat([colGDP, colAgri, colArab, colBirth, colDeath, colIndiv, colIndus, colMobile, colMort, colCrop, colPopDen,
                    colPop, colServ, colArea], axis=1)
    df.columns = ['GDP', 'Agriculture', 'Arable Land', 'Birth Rate', 'Death Rate', 'Individual Internet usage', 'Industry',
                'Mobile Subscriptions', 'Mortality Rate','Cropland','Population Density','Population',
                'Services', 'Surface Area']
    # print(df)
    # df.drop(['Series Name', 'Series Code', 'Country Name', 'Country Code'], axis=0, inplace=True)
    # df = pd.DataFrame(df, dtype=float)

    # Correlation value of GDP vs factor (requires a for loop implementation)
    # corrDict = {}
    # for i in range(1, len(df.columns)):
    #     col1 = df['GDP']
    #     col2 = df[df.columns[i]]
    #     correlation = col1.corr(col2)
    #     corrDict[df.columns[i]] = correlation

    # GDPCorrDict = sorted(corrDict.items(), key=lambda x: x[1], reverse=True)
    # Bot3CorrDict = sorted(corrDict.items(), key=lambda x: x[1], reverse=True)[-3:]

    # for i in range(len(GDPCorrDict)):
    #     plt.subplot(5, 3, i + 1)
    #     sns.lineplot(x=GDPCorrDict[i][0], y='GDP', data=df)
    plt.tight_layout()
    plt.show()

def displayCorrTable():
    df = pd.DataFrame(data=corrDict, index=[0]).T
    df.columns = ['Correlation Value']
    window = tk.Tk()
    window.title('%s GDP Factors correlation values' % userSelection)
    f = Frame(window)
    f.pack(fill=BOTH, expand=1)
    pt = Table(f, dataframe=df, showstatusbar=True, width=200, height=300)
    options = {'cellwidth': 150, 'floatprecision': 4, 'align': 'center'}
    config.apply_options(options, pt)
    pt.showIndex()
    pt.show()

''' 
#Display and save in to excel. Function not used.
def displayCorrExcel():
    corrDF = pd.DataFrame(data=corrDict, index=[0])
    corrDF.index = ['Correlation Value']
    corrDF = (corrDF.T)
    corrDF.to_excel('%s correlation values of GDP Factors.xlsx'%userSelection)


#Display table using Matplotlib. Function not used.
def displayCorrTablePlot():
    plt.figure("GDP Factors correlation values")
    df = pd.DataFrame(data=corrDict, index=[0]).T
    df.columns = ['Correlation Value']
    plt.suptitle("%s GDP Factors correlation values" % userSelection)
    cell_text = np.round(df.values, 3)
    table = plt.table(cellText=cell_text, rowLabels=df.index, colLabels=df.columns, loc="center", cellLoc="center",
                       bbox=[0.5, 0.15, 0.3, 0.8])
    table.set_fontsize(10)
    table.auto_set_font_size(False)
    table.scale(1, 1)
    plt.axis("off")
    plt.grid(False)
    plt.show()
'''



# displayFactorsGraph()


# mainloop()