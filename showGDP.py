"""This file contains the features for All Countries"""

# Import all necessary modules
import numpy as np
import pandas as pd
from pandastable import Table
from pandastable import config
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import *
from matplotlib.ticker import ScalarFormatter

# RawDataSet
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


# Store the files into  a list
file_selection = [dataGDP, dataAgri, dataArab, dataBirth, dataDeath, dataIndiv, dataIndus, dataMobile, dataMort,
                  dataCrop, dataPopDen, dataPop, dataServ, dataArea]


# Clean values in data frame
def clean_dataframe(frame):
    """
    :param frame: Takes in a dataframe
    Clean the data frame and remove any unwanted values
    :return: return a clean data frame
    """
    frame.columns = frame.columns.str.replace(r"\[.*?\]", "")  # Remove Brackets
    frame.rename(columns=lambda x: x.strip(), inplace=True)  # Strip the spaces
    frame = frame.dropna()
    return frame


# Declare variable and GDP dataframe
num = 10
df = pd.DataFrame(dataGDP)
df = clean_dataframe(df)


# Trim columns that are not needed
def trim_column(df,user_input):
    """
    :param df: Take in a data frame as input
    :param user_input: Fetch year value from user input
    :return: Dataframe with trim columns
    """
    for column in df.columns[4:]:
        if column != user_input:
            df = df.drop(column, 1)
    df = df.replace('..', np.nan).dropna()
    df = df.replace('...', np.nan).dropna()
    return df


# Setting the basic style for plots
def plot_design(title):
    """
    :param title: Main title for plot graph
    Add a standard style for all graphs
    """
    plt.title(title)
    plt.xlabel("GDP")
    plt.ylabel("Countries")
    plt.tight_layout()
    plt.xticks(fontsize='8')
    plt.show()


# Display GDP for all Countries based on year
def display_all(user_input):
    """
    :param user_input: Fetch year value from user input
    Generate DataFrame based on factor value and plot accordingly
    """
    new_df = trim_column(df, user_input)
    new_df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1, inplace=True)
    new_df.reset_index(drop=True,inplace=True)
    window = tk.Toplevel()
    window.title('GPD For All Countries In ' + user_input)
    window.geometry("500x700")
    f = Frame(window)
    f.pack(fill=BOTH, expand=1)
    pt = Table(f, dataframe=new_df, showstatusbar=True, width=200, height=300)
    options = {'cellwidth': 150, 'floatprecision': 4, 'align': 'center'}
    config.apply_options(options, pt)
    pt.showIndex()
    pt.show()


# Display GDP of top 10 Countries based on year
def display_top_gdp(user_input):
    """
    :param user_input: Fetch year value from user input
    Generate DataFrame based on factor value and plot accordingly
    """
    new_df = trim_column(df, user_input)
    new_df[user_input] = new_df[user_input].astype(float)
    new_df = new_df.sort_values(by=[user_input], ascending=False)
    plt.barh(new_df['Country Name'][:num], new_df[user_input][:num])
    plot_design("GDP Of Top Countries")


# Display GDP of bottom 10 Countries based on year
def display_btm_gdp(user_input):
    """
    :param user_input: Fetch year value from user input
    Generate DataFrame based on year value and plot accordingly
    """
    new_df = trim_column(df, user_input)
    new_df[user_input] = new_df[user_input].astype(float)
    new_df.sort_values(by=[user_input], inplace=True)
    plt.barh(new_df['Country Name'][:num], new_df[user_input][:num])
    plot_design("GDP Of Bottom Countries")


# Display top 10 countries of specific factor in specific year
def display_specific_factor(user_input, factor_input):
    """
    :param user_input: Fetch year value from user input
    :param factor_input: Fetch factor value from user input
    Generate DataFrame based on factor value and plot accordingly
    """
    for file in file_selection:
        if file["Series Name"][0] == factor_input:
            plt.figure(factor_input + " In " + user_input)
            df_2 = pd.DataFrame(file)
            df_2 = clean_dataframe(df_2)
            df_2[user_input] = pd.to_numeric(df_2[user_input], errors='coerce')
            df_2[user_input] = df_2[user_input].astype(float)
            df_2.sort_values(by=[user_input], ascending=False, inplace=True)
            plt.barh(df_2['Country Name'][:num], df_2[user_input][:num])
            plot_design(factor_input)
