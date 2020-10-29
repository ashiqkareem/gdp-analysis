import requests
import zipfile
import pandas as pd

def download_zip():
    url = 'https://raw.github.com/ashiqkareem/gdp-analysis/master/files.zip'

    r = requests.get(url)
    with open("files.zip", "wb") as code:
        code.write(r.content)

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

# download_zip()
# unzip()