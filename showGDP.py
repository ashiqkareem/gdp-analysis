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
from data import *

userSelection = 1960
df = pd.DataFrame(dataGDP)

"""
# Concatenating the different factors into 1 dataframe
df_2 = pd.concat([dataGDP, dataAgri, dataArab, dataBirth, dataDeath, dataIndiv, dataIndus, dataMobile,
                  dataMort, dataCrop, dataPopDen, dataPop, dataServ, dataArea], axis=1)
df_2 = pd.DataFrame(df_2)
df_2 = df_2.T
df_2.drop(['Series Code', 'Series Name', 'Country Code', 'Country Name'], axis=0, inplace=True)

print(df_2)
df_2.to_excel(r'C:\Users\JingX\Desktop\JX_SIT\test.xlsx', index=False)
"""


# Setting the basic style for plots
def plot_design(title):
    plt.style.use('ggplot')
    plt.title(title)
    plt.legend()
    plt.xlabel("GPD")
    plt.ylabel("Countries")
    plt.show()


def display_all(user_input):
    df[user_input] = df[user_input].astype(int)
    plt.barh(df['Country Name'], df[user_input])
    plot_design("GPD For All Countries")


def display_top_gpd(user_input):
    df.sort_values(by=[user_input, "Country Name"], inplace=True)
    plt.barh(df['Country Name'][-5:], df[user_input][-5:])
    plot_design("GPD Of Top Countries")


def display_btm_gpd(user_input):
    df.sort_values(by=[user_input, "Country Name"], inplace=True)
    plt.barh(df['Country Name'][:5], df[user_input][:5])
    plot_design("GPD Of Bottom Countries")


# Still trying
def display_top_factors(user_input):
    """
    Concate the dataframe
    Get all factors
    Find the factor that affected the GPD the most in a specific year
    Display the top N country with the factors
    """

# display_all(userSelection)
# display_top_gpd(userSelection)
# display_btm_gpd(userSelection)
# display_top_factors(userSelection)
