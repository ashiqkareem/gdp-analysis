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

# User input
user_year = 1960
user_factor ="Agriculture, forestry, and fishing, value added (% of GDP)"


# Declare var and GDP dataframe
num = 10
df = pd.DataFrame(dataGDP)


# Create data frame base on factor user selected
def file_to_execute(file_to_show):
    for file in file_selection:
        if file["Series Name"][0] == file_to_show:
            df_2 = pd.DataFrame(file)
    return df_2


# Setting the basic style for plots
def plot_design(title):
    plt.title(title)
    plt.xlabel("GPD")
    plt.ylabel("Countries")
    plt.style.use('ggplot')
    plt.show()


def display_all(user_input):
    df[user_input] = df[user_input].astype(int)
    plt.barh(df['Country Name'], df[user_input])
    plot_design("GPD For All Countries")


def display_top_gpd(user_input):
    df.sort_values(by=[user_input, "Country Name"], inplace=True)
    plt.barh(df['Country Name'][-num:], df[user_input][-num:])
    plot_design("GPD Of Top Countries")


def display_btm_gpd(user_input):
    df.sort_values(by=[user_input, "Country Name"], inplace=True)
    plt.barh(df['Country Name'][:num], df[user_input][:num])
    plot_design("GPD Of Bottom Countries")


def display_specific_factor(user_input, factor_input):
    x = file_to_execute(user_factor)
    x.sort_values(by=[user_input, "Country Name"], inplace=True)
    plt.barh(x['Country Name'][-num:], x[user_input][-num:])
    plot_design(factor_input)

# display_all(user_year)
# display_top_gpd(user_year)
# display_btm_gpd(user_year)
# display_specific_factor(user_year,user_factor)
