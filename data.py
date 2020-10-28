import pandas as pd


# Raw DataSet
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
file_selection = [dataGDP, dataAgri, dataArab, dataBirth, dataDeath, dataIndiv, dataIndus, dataMobile, dataMort,
                  dataCrop, dataPopDen, dataPop, dataServ, dataArea]


