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
user_year = "1960"
user_factor ="Agriculture, forestry, and fishing, value added (% of GDP)"


# Clean columns in data frame
def clean_dataframe(frame):
    frame.columns = frame.columns.str.replace(r"\[.*?\]", "")  # Remove Brackets
    frame.rename(columns=lambda x: x.strip(), inplace=True)  # Strip the spaces
    frame = frame.dropna()
    # frame = frame.replace('..', np.nan).dropna()
    # frame = frame.replace('...', np.nan).dropna()
    return frame


# Declare var and GDP dataframe
num = 10
df = pd.DataFrame(dataGDP)
df = clean_dataframe(df)

# Dropping columns that are not needed after cleaning based on user selection
for column in df.columns[4:]:
    if column != user_year:
        df = df.drop(column, 1)
df = df.replace('..', np.nan).dropna()
df = df.replace('...', np.nan).dropna()


# Create data frame base on factor user selected
def file_to_execute(file_to_show):
    for file in file_selection:
        if file["Series Name"][0] == file_to_show:
            df_2 = pd.DataFrame(file)
            df_2 = clean_dataframe(df_2)
    return df_2


# Setting the basic style for plots
def plot_design(title):
    plt.title(title)
    plt.style.use('ggplot')
    plt.xlabel("GPD")
    plt.ylabel("Countries")
    plt.show()


# Display GPD for all Countries based on year
def display_all(user_input):
    plt.barh(df['Country Name'], df[user_input])
    plot_design("GPD For All Countries")


# Display GDP of top 10 Countries based on year
def display_top_gpd(user_input):
    df.sort_values(by=[user_input, "Country Name"], inplace=True)
    plt.barh(df['Country Name'][-num:], df[user_input][-num:])
    plot_design("GPD Of Top Countries")


# Display GDP of bottom 10 Countries based on year
def display_btm_gpd(user_input):
    df.sort_values(by=[user_input, "Country Name"], inplace=True)
    print(df[user_input])
    plt.barh(df['Country Name'][:num], df[user_input][:num])
    plot_design("GPD Of Bottom Countries")


# Display top 10 countries of specific factor in specific year
def display_specific_factor(user_input, factor_input):
    x = file_to_execute(factor_input)
    x.sort_values(by=[user_input, "Country Name"], inplace=True)
    plt.barh(x['Country Name'][-num:], x[user_input][-num:])
    plot_design(factor_input)

# display_all(user_year)
# display_top_gpd(user_year)
# display_btm_gpd(user_year)
# display_specific_factor(user_year,user_factor)


# file_to_execute(user_factor)