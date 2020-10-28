import numpy as np
import pandas as pd
from pandastable import Table
from pandastable import config
from matplotlib import pyplot as plt
from data import *
import tkinter as tk
from tkinter import *


# User input
# user_year = "1960"
# user_factor ="Agriculture, forestry, and fishing, value added (% of GDP)"


# Clean columns in data frame
def clean_dataframe(frame):
    frame.columns = frame.columns.str.replace(r"\[.*?\]", "")  # Remove Brackets
    frame.rename(columns=lambda x: x.strip(), inplace=True)  # Strip the spaces
    frame = frame.dropna()
    return frame


# Declare var and GDP dataframe
num = 10
df = pd.DataFrame(dataGDP)
df = clean_dataframe(df)

"""
# Dropping columns that are not needed after cleaning based on user selection
def drop_column(user_year):
    for column in df.columns[4:]:
        if column != user_year:
            df = df.drop(column, 1)
    df = df.replace('..', np.nan).dropna()
    df = df.replace('...', np.nan).dropna()
    df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1, inplace=True)


# Create data frame base on factor user selected
def file_to_execute(file_to_show):
    for file in file_selection:
        if file["Series Name"][0] == file_to_show:
            df_2 = pd.DataFrame(file)
            df_2 = clean_dataframe(df_2)
    return df_2
"""

# Setting the basic style for plots
def plot_design(title):
    plt.title(title)
    plt.style.use('ggplot')
    plt.xlabel("GPD")
    plt.ylabel("Countries")
    plt.tight_layout()
    plt.show()


# Display GPD for all Countries based on year
def display_all(user_input):
    df = pd.DataFrame(dataGDP)
    df = clean_dataframe(df)
    for column in df.columns[4:]:
        if column != user_input:
            df = df.drop(column, 1)

    df = df.replace('..', np.nan).dropna()
    df = df.replace('...', np.nan).dropna()
    df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1, inplace=True)
    window = tk.Toplevel()
    window.title('GPD For All Countries')
    f = Frame(window)
    f.pack(fill=BOTH, expand=1)
    pt = Table(f, dataframe=df, showstatusbar=True, width=200, height=300)
    options = {'cellwidth': 150, 'floatprecision': 4, 'align': 'center'}
    config.apply_options(options, pt)
    pt.showIndex()
    pt.show()


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
    for file in file_selection:
        if file["Series Name"][0] == factor_input:
            df_2 = pd.DataFrame(file)
            df_2 = clean_dataframe(df_2)
            df_2.sort_values(by=[user_input, "Country Name"], inplace=True)
            plt.barh(df_2['Country Name'][-num:], df_2[user_input][-num:])
            plot_design(factor_input)


# display_all()
# display_top_gpd(user_year)
# display_btm_gpd(user_year)
# display_specific_factor(user_year,user_factor)


# mainloop()