import tkinter
from tkinter import ttk
from tkinter import *
from tkintertable import TableCanvas, TableModel
from gdpAnalysisFunctions import *
from pandastable import Table
from pandastable import config
from showGDP import *
from data import *


def importMsg():
    if True:
        msgLblT1.config(text="File import success!", fg="green")
    else:
        msgLblT1.config(text="File import failed!", fg="red")

# Define all countries
allCountries = ["Afghanistan",
                "Albania",
                "Algeria",
                "American Samoa",
                "Andorra",
                "Angola",
                "Antigua and Barbuda",
                "Argentina",
                "Armenia",
                "Aruba",
                "Australia",
                "Austria",
                "Azerbaijan",
                "Bahamas, The",
                "Bahrain",
                "Bangladesh",
                "Barbados",
                "Belarus",
                "Belgium",
                "Belize",
                "Benin",
                "Bermuda",
                "Bhutan",
                "Bolivia",
                "Bosnia and Herzegovina",
                "Botswana",
                "Brazil",
                "British Virgin Islands",
                "Brunei Darussalam",
                "Bulgaria",
                "Burkina Faso",
                "Burundi",
                "Cabo Verde",
                "Cambodia",
                "Cameroon",
                "Canada",
                "Cayman Islands",
                "Central African Republic",
                "Chad",
                "Channel Islands",
                "Chile",
                "China",
                "Colombia",
                "Comoros",
                "Congo, Dem. Rep.",
                "Congo, Rep.",
                "Costa Rica",
                "Cote d'Ivoire",
                "Croatia",
                "Cuba",
                "Curacao",
                "Cyprus",
                "Czech Republic",
                "Denmark",
                "Djibouti",
                "Dominica",
                "Dominican Republic",
                "Ecuador",
                "Egypt, Arab Rep.",
                "El Salvador",
                "Equatorial Guinea",
                "Eritrea",
                "Estonia",
                "Eswatini",
                "Ethiopia",
                "Faroe Islands",
                "Fiji",
                "Finland",
                "France",
                "French Polynesia",
                "Gabon",
                "Gambia, The",
                "Georgia",
                "Germany",
                "Ghana",
                "Gibraltar",
                "Greece",
                "Greenland",
                "Grenada",
                "Guam",
                "Guatemala",
                "Guinea",
                "Guinea-Bissau",
                "Guyana",
                "Haiti",
                "Honduras",
                "Hong Kong SAR, China",
                "Hungary",
                "Iceland",
                "India",
                "Indonesia",
                "Iran, Islamic Rep.",
                "Iraq",
                "Ireland",
                "Isle of Man",
                "Israel",
                "Italy",
                "Jamaica",
                "Japan",
                "Jordan",
                "Kazakhstan",
                "Kenya",
                "Kiribati",
                "Korea, Dem. People’s Rep.",
                "Korea, Rep.",
                "Kosovo",
                "Kuwait",
                "Kyrgyz Republic",
                "Lao PDR",
                "Latvia",
                "Lebanon",
                "Lesotho",
                "Liberia",
                "Libya",
                "Liechtenstein",
                "Lithuania",
                "Luxembourg",
                "Macao SAR, China",
                "Madagascar",
                "Malawi",
                "Malaysia",
                "Maldives",
                "Mali",
                "Malta",
                "Marshall Islands",
                "Mauritania",
                "Mauritius",
                "Mexico",
                "Micronesia, Fed. Sts.",
                "Moldova",
                "Monaco",
                "Mongolia",
                "Montenegro",
                "Morocco",
                "Mozambique",
                "Myanmar",
                "Namibia",
                "Nauru",
                "Nepal",
                "Netherlands",
                "New Caledonia",
                "New Zealand",
                "Nicaragua",
                "Niger",
                "Nigeria",
                "North Macedonia",
                "Northern Mariana Islands",
                "Norway",
                "Oman",
                "Pakistan",
                "Palau",
                "Panama",
                "Papua New Guinea",
                "Paraguay",
                "Peru",
                "Philippines",
                "Poland",
                "Portugal",
                "Puerto Rico",
                "Qatar",
                "Romania",
                "Russian Federation",
                "Rwanda",
                "Samoa",
                "San Marino",
                "Sao Tome and Principe",
                "Saudi Arabia",
                "Senegal",
                "Serbia",
                "Seychelles",
                "Sierra Leone",
                "Singapore",
                "Sint Maarten (Dutch part)",
                "Slovak Republic",
                "Slovenia",
                "Solomon Islands",
                "Somalia",
                "South Africa",
                "South Sudan",
                "Spain",
                "Sri Lanka",
                "St. Kitts and Nevis",
                "St. Lucia",
                "St. Martin (French part)",
                "St. Vincent and the Grenadines",
                "Sudan",
                "Suriname",
                "Sweden",
                "Switzerland",
                "Syrian Arab Republic",
                "Tajikistan",
                "Tanzania",
                "Thailand",
                "Timor-Leste",
                "Togo",
                "Tonga",
                "Trinidad and Tobago",
                "Tunisia",
                "Turkey",
                "Turkmenistan",
                "Turks and Caicos Islands",
                "Tuvalu",
                "Uganda",
                "Ukraine",
                "United Arab Emirates",
                "United Kingdom",
                "United States",
                "Uruguay",
                "Uzbekistan",
                "Vanuatu",
                "Venezuela, RB",
                "Vietnam",
                "Virgin Islands (U.S.)",
                "West Bank and Gaza",
                "Yemen, Rep.",
                "Zambia",
                "Zimbabwe"
                ]

gdpFactorsList = ["GDP, PPP (current international $)",
                  "Agriculture, forestry, and fishing, value added (% of GDP)",
                  "Arable land (% of land area)",
                  "Birth rate, crude (per 1,000 people)",
                  "Death rate, crude (per 1,000 people)",
                  "Individuals using the Internet (% of population)",
                  "Industry (including construction), value added (% of GDP)",
                  "Literacy rate, adult total (% of people ages 15 and above)",
                  "Mobile cellular subscriptions (per 100 people)",
                  "Mortality rate, infant (per 1,000 live births)",
                  "Permanent cropland (% of land area)",
                  "Population density (people per sq. km of land area)",
                  "Population, total",
                  "Services, value added (% of GDP)"]

# Create window
window = tkinter.Tk()
window.title("GDP Analysis")

# Create tabs
tabList = ttk.Notebook(window)
tab1 = ttk.Frame(tabList)
tab2 = ttk.Frame(tabList)
tab3 = ttk.Frame(tabList)
tabList.add(tab1, text="Files Section")
tabList.add(tab2, text="Single Country")
tabList.add(tab3, text="All Countries")
tabList.pack(expand=1, fill="both")

# Create tab 1 frames
frameT1 = Frame(tab1, width=700, height=400, bg="lightblue")
frameT1.grid(columnspan=3, row=0)

# Create tab 2 frames
frameT2 = Frame(tab2, width=700, height=160, bg="lightblue")
frameT2.grid(columnspan=3, row=0)
frame2T2 = Frame(tab2, width=700, height=90, bg="lightblue")
frame2T2.grid(columnspan=3, row=1)
frame3T2 = Frame(tab2, width=700, height=150, bg="lightblue")
frame3T2.grid(columnspan=3, row=2)

# Create tab 3 frames
frameT3 = Frame(tab3, width=700, height=50, bg="lightblue")
frameT3.grid(columnspan=3, row=0)
frame2T3 = Frame(tab3, width=700, height=180, bg="lightblue")
frame2T3.grid(columnspan=3, row=1)
frame3T3 = Frame(tab3, width=700, height=40, bg="lightblue")
frame3T3.grid(columnspan=3, row=2)
frame4T3 = Frame(tab3, width=700, height=130, bg="lightblue")
frame4T3.grid(columnspan=3, row=3)

# Tab 1 frame elements
dwlimpLblT1 = Label(frameT1, text="Download/Import Data Sets", bg="lightblue")
dwlimpLblT1.grid(column=0, row=0, padx=30, pady=35, sticky="w")

dwlBtnT1 = Button(frameT1, text="Download GDPAnalysis.ZIP File", width=90)
dwlBtnT1.grid(column=0, row=1, padx=30, pady=35, sticky="w")

impBtnT1 = Button(frameT1, text="Import Your Own .ZIP File",
                  width=90, command=importMsg)
impBtnT1.grid(column=0, row=2, padx=30, pady=55, sticky="w")

msgLblT1 = Label(frameT1, text="", bg="lightblue", width=90)
msgLblT1.grid(column=0, row=3, padx=30, sticky="w")

# Tab 2 frames elements
seperatorT2 = ttk.Separator(frameT2, orient=HORIZONTAL)
seperatorT2.grid(column=0, row=0, padx=15, pady=40)

countryLblT2 = Label(frameT2, text="Select a country:", bg="lightblue")
countryLblT2.grid(column=1, row=0)

countryCmbT2 = ttk.Combobox(frameT2, width=62, state="readonly")
countryCmbT2["values"] = (allCountries)
countryCmbT2.current(0)
countryCmbT2.grid(column=2, row=0)

actLblT2 = Label(frameT2, text="Select an action:", bg="lightblue")
actLblT2.grid(column=1, row=1, sticky="w")

actCmbT2 = ttk.Combobox(frameT2, width=62, state="readonly")
actCmbT2["values"] = ("List correlation values of GDP factors",
                      "Display correlations values in heat map",
                      "Display GDP factors in graphs",
                      "Display simple linear regression graphs (GDP VS Factors)",
                      "Display best fit line of GDP")
actCmbT2.current(0)
actCmbT2.grid(column=2, row=1)


def countryAct():
    '''Link country to action button'''
    if actCmbT2.get() == "List correlation values of GDP factors":
        displayCorrTable(dict(dataframeCreation(countryCmbT2.get())), countryCmbT2.get())
    elif actCmbT2.get() == "Display correlations values in heat map":
        heatMap(dataframeCreation(countryCmbT2.get()))
    elif actCmbT2.get() == "Display GDP factors in graphs":
        displayFactorsGraph(corrGDPDict(dataframeCreation(countryCmbT2.get())), dataframeCreation(countryCmbT2.get()))
    elif actCmbT2.get() == "Display simple linear regression graphs (GDP VS Factors)":
        displayLinearRegFactor(dataframeCreation(countryCmbT2.get()))
    else:
        linearReg(countryCmbT2, dataframeCreation(countryCmbT2.get()))


actBtnT2 = Button(frameT2, text="Generate", width=15, command=countryAct)
actBtnT2.grid(column=3, row=1, padx=20, sticky="w")

expBtnT2 = Button(
    frame2T2, text="Export All Data Sets For Country", width=90, command=lambda: exportCSV(dataframeCreation(countryCmbT2.get()), countryCmbT2.get()))
expBtnT2.grid(column=0, row=0, pady=10, padx=35, sticky="w")

seperatorT2 = ttk.Separator(frame3T2, orient=HORIZONTAL)
seperatorT2.grid(column=0, row=0, padx=15)

country2LblT2 = Label(frame3T2, text="Select a country:", bg="lightblue")
country2LblT2.grid(column=1, row=0, sticky="w")

country2CmbT2 = ttk.Combobox(frame3T2, width=62, state="readonly")
country2CmbT2["values"] = (allCountries)
country2CmbT2.current(0)
country2CmbT2.grid(column=2, row=0)

facLblT2 = Label(frame3T2, text="Select a GDP factor:", bg="lightblue")
facLblT2.grid(column=1, row=1, pady=30, sticky="w")

facCmbT2 = ttk.Combobox(frame3T2, width=62, state="readonly")
facCmbT2["values"] = gdpFactorsList
facCmbT2.current(0)
facCmbT2.grid(column=2, row=1)


def gdpFac():
    '''Link country to GDP factor button'''
    if facCmbT2.get() == "GDP, PPP (current international $)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "GDP")
    elif facCmbT2.get() == "Agriculture, forestry, and fishing, value added (% of GDP)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Agriculture")
    elif facCmbT2.get() == "Arable land (% of land area)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Arable Land")
    elif facCmbT2.get() == "Birth rate, crude (per 1,000 people)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Birth Rate")
    elif facCmbT2.get() == "Death rate, crude (per 1,000 people)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Death Rate")
    elif facCmbT2.get() == "Individuals using the Internet (% of population)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Individuals using Internet")
    elif facCmbT2.get() == "Industry (including construction), value added (% of GDP)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Industry")
    elif facCmbT2.get() == "Mobile cellular subscriptions (per 100 people)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Mobile Subscriptions")
    elif facCmbT2.get() == "Mortality rate, infant (per 1,000 live births)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Mortality Rate")
    elif facCmbT2.get() == "Permanent cropland (% of land area)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Cropland")
    elif facCmbT2.get() == "Population density (people per sq. km of land area)":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Population Density")
    elif facCmbT2.get() == "Population, total":
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Population")
    else:
        displayFactor(country2CmbT2.get(), dataframeCreation(country2CmbT2.get()), "Services")

facBtnT2 = Button(frame3T2, text="Generate", width=15, command=gdpFac)
facBtnT2.grid(column=3, row=1, padx=20, sticky="w")

# Tab 3 frame elements
seperatorT3 = ttk.Separator(frameT3, orient=HORIZONTAL)
seperatorT3.grid(column=0, row=0, padx=45, pady=30)

yearLblT3 = Label(frameT3, text="Select a year:", bg="lightblue")
yearLblT3.grid(column=1, row=0, sticky="w")

# Create list of years for combo box
yearList = []
year = 1990
while year <= 2016:
    yearList.append(year)
    year += 1

yearCmbT3 = ttk.Combobox(frameT3, width=62, state="readonly")
yearCmbT3["values"] = (yearList)
yearCmbT3.current(0)
yearCmbT3.grid(column=2, row=0)

facLblT3 = Label(frame2T3, text="Select a GDP factor", bg="lightblue")
facLblT3.grid(column=0, row=0, padx=125, pady=30)

facCmbT3 = ttk.Combobox(frame2T3, width=50, state="readonly")
facCmbT3["values"] = gdpFactorsList
facCmbT3.current(0)
facCmbT3.grid(column=0, row=1)

facBtnT3 = Button(frame2T3, text="Generate", width=45, command=lambda: display_specific_factor(yearCmbT3.get(), facCmbT3.get()))
facBtnT3.grid(column=0, row=2, pady=20)

actLblT3 = Label(frame2T3, text="Select an action:", bg="lightblue")
actLblT3.grid(column=1, row=0, padx=100)

actCmbT3 = ttk.Combobox(frame2T3, width=50, state="readonly")
actCmbT3["values"] = ("List GDP of all countries",
                      "Display GDP of top 10 countries in bar graphs",
                      "Display GDP of bottom 10 countries in bar graphs")
actCmbT3.current(0)
actCmbT3.grid(column=1, row=1)

def yearAct():
    '''Link year to action button'''
    if actCmbT3.get() == "List GDP of all countries":
        display_all(yearCmbT3.get())
    elif actCmbT3.get() == "Display GDP of top 10 countries in bar graphs":
        display_top_gdp(yearCmbT3.get())
    else:
        display_btm_gdp(yearCmbT3.get())

actBtnT3 = Button(frame2T3, text="Generate", width=45, command=yearAct)
actBtnT3.grid(column=1, row=2)

warnLblT3 = Label(frame3T3, text="WARNING: EXPERIMENTAL FEATURE BELOW. PLEASE WAIT 2 MINUTES FOR GRAPH TO BE GENERATED", bg="lightblue", fg="red")
warnLblT3.grid(column=0, row=0, padx=70)

seperator2T3 = ttk.Separator(frame4T3, orient=HORIZONTAL)
seperator2T3.grid(column=0, row=0, padx=15)

preYearLblT3 = Label(frame4T3, text="Select year of prediction:", bg="lightblue")
preYearLblT3.grid(column=1, row=0, sticky="w")

# Create list of prediction years for combo box
preYearList = []
preYear = 2020
while preYear <= 2099:
    preYearList.append(preYear)
    preYear += 1

preYearCmbT3 = ttk.Combobox(frame4T3, width=62, state="readonly")
preYearCmbT3["values"] = (preYearList)
preYearCmbT3.current(0)
preYearCmbT3.grid(column=2, row=0)

actLbl2T3 = Label(frame4T3, text="Select an action:", bg="lightblue")
actLbl2T3.grid(column=1, row=1, pady=30, sticky="w")

act2CmbT3 = ttk.Combobox(frame4T3, width=62, state="readonly")
act2CmbT3["values"] = ("Display GDP of all countries in Year X",
                       "Display top 10 GDP predictions in Year X in bar graphs",
                       "Display bottom 10 GDP predictions in Year X in bar graphs")
act2CmbT3.current(0)
act2CmbT3.grid(column=2, row=1)

def preYearAct():
    '''Link prediction year to action button'''
    if act2CmbT3.get() == "Display GDP of all countries in Year X":
        allYearsGDPPrediction(countryList(), 2020)
    elif act2CmbT3.get() == "Display GDP of top 10 countries in Year X in bar graphs":
        print(act2CmbT3.get(), preYearCmbT3.get())
    else:
        print(act2CmbT3.get(), preYearCmbT3.get())

actBtn2T3 = Button(frame4T3, text="Generate", width=15, command=preYearAct)
actBtn2T3.grid(column=3, row=1, padx=10, sticky="w")

# Apply elements to frames
frameT1.grid_propagate(0)
frameT2.grid_propagate(0)
frame2T2.grid_propagate(0)
frame3T2.grid_propagate(0)
frameT3.grid_propagate(0)
frame2T3.grid_propagate(0)
frame3T3.grid_propagate(0)
frame4T3.grid_propagate(0)

# Size window and disable resize
window.geometry("700x400")
window.resizable(0, 0)

# Run window
window.mainloop()
