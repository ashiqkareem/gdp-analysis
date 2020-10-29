import zipfile
import pandas as pd

with zipfile.ZipFile('files.zip','r') as my_zip:
    my_zip.extractall('Datasets')

    # Dataframes
    path = '../gdp-analysis/rawDataSet/'
    dataGDP = pd.read_excel(path + 'GDP, PPP (current international $).csv')
    dataAgri = pd.read_excel(path + 'Agriculture, forestry, and fishing, value added (% of GDP).xlsx')
    dataArab = pd.read_excel(path + 'Arable land (% of land area).xlsx')
    dataBirth = pd.read_excel(path + 'Birth rate, crude (per 1,000 people).xlsx')
    dataDeath = pd.read_excel(path + 'Death rate, crude (per 1,000 people).xlsx')
    dataIndiv = pd.read_excel(path + 'Individuals using the Internet (% of population).xlsx')
    dataIndus = pd.read_excel(path + 'Industry (including construction), value added (% of GDP).xlsx')
    dataMobile = pd.read_excel(path + 'Mobile cellular subscriptions (per 100 people).xlsx')
    dataMort = pd.read_excel(path + 'Mortality rate, infant (per 1,000 live births).xlsx')
    dataCrop = pd.read_excel(path + 'Permanent cropland (% of land area).xlsx')
    dataPopDen = pd.read_excel(path + 'Population density (people per sq. km of land area).xlsx')
    dataPop = pd.read_excel(path + 'Population, total.xlsx')
    dataServ = pd.read_excel(path + 'Services, value added (% of GDP).xlsx')
    dataArea = pd.read_excel(path + 'Surface area (sq. km).xlsx')

#     import requests

# url = 'https://raw.github.com/ashiqkareem/gdp-analysis/master/files.zip'

# r = requests.get(url)
# with open("files.zip", "wb") as code:
#     code.write(r.content)