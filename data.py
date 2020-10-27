import pandas as pd

# Dataframes
"""
path ='../gdp-analysis/Datasets/'
dataGDP = pd.read_excel(path + 'SAMPLE - GDP per capita (constant LCU).xlsx')
dataAgri = pd.read_excel(path + 'SAMPLE - Agriculture, forestry, and fishing, value added (% of GDP).xlsx')
dataArab = pd.read_excel(path + 'SAMPLE - Arable land (% of land area).xlsx')
dataBirth = pd.read_excel(path + 'SAMPLE - Birth rate, crude (per 1,000 people).xlsx')
dataDeath = pd.read_excel(path + 'SAMPLE - Death rate, crude (per 1,000 people).xlsx')
dataIndiv = pd.read_excel(path + 'SAMPLE - Individuals using the Internet (% of population).xlsx')
dataIndus = pd.read_excel(path + 'SAMPLE - Industry (including construction), value added (% of GDP).xlsx')
dataMobile = pd.read_excel(path + 'SAMPLE - Mobile cellular subscriptions (per 100 people).xlsx')
dataMort = pd.read_excel(path + 'SAMPLE - Mortality rate, infant (per 1,000 live births).xlsx')
dataCrop = pd.read_excel(path + 'SAMPLE - Permanent cropland (% of land area).xlsx')
dataPopDen = pd.read_excel(path + 'SAMPLE - Population density (people per sq. km of land area).xlsx')
dataPop = pd.read_excel(path + 'SAMPLE - Population, total.xlsx')
dataServ = pd.read_excel(path + 'SAMPLE - Services, value added (% of GDP).xlsx')
dataArea = pd.read_excel(path + 'SAMPLE - Surface area (sq. km).xlsx')
"""
# Raw Data Set
path ='../gdp-analysis/rawDataSet/'
dataGDP = pd.read_csv(path + 'GDP per capita (constant LCU).csv')
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



# Store files in list to select the files to show based on user input
file_selection = []
file_selection.append(dataGDP)
file_selection.append(dataAgri)
file_selection.append(dataArab)
file_selection.append(dataBirth)
file_selection.append(dataDeath)
file_selection.append(dataIndiv)
file_selection.append(dataIndus)
file_selection.append(dataMobile)
file_selection.append(dataMort)
file_selection.append(dataCrop)
file_selection.append(dataPopDen)
file_selection.append(dataPop)
file_selection.append(dataServ)
file_selection.append(dataArea)


