import pandas as pd

# Dataframes
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

