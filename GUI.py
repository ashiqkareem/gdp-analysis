import tkinter
from tkinter import ttk
from tkinter import *
from tkintertable import TableCanvas, TableModel


def importMsg():
    if True:
        msgLblT1.config(text="File import success!", fg="green")
    else:
        msgLblT1.config(text="File import failed!", fg="red")


def tableWindow():
    # Create window and disable resize
    newWindow = Toplevel(window, bg="lightblue")
    newWindow.resizable(0, 0)

    # Create table
    tframe = Frame(newWindow)
    tframe.pack()
    data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
       'rec2': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'}
       } 
    table = TableCanvas(tframe, data=data)

    # Update and show table
    table.show()

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

# Create tab1 frames
frameT1 = Frame(tab1, width=700, height=400, bg="lightblue")
frameT1.grid(columnspan=3, row=0)

# Create tab2 frames
frameT2 = Frame(tab2, width=700, height=300, bg="lightblue")
frameT2.grid(columnspan=3, row=0)
frame2T2 = Frame(tab2, width=700, height=100, bg="lightblue")
frame2T2.grid(columnspan=3, row=1)

# Create tab3 frames
frameT3 = Frame(tab3, width=700, height=400, bg="lightblue")
frameT3.grid(columnspan=3, row=0)

# tab1 frame elements
dwlimpLblT1 = Label(frameT1, text="Download/Import Data Sets", bg="lightblue")
dwlimpLblT1.grid(column=0, row=0, padx=30, pady=35, sticky="w")

dwlBtnT1 = Button(frameT1, text="Download GDPAnalysis.ZIP File", width=90)
dwlBtnT1.grid(column=0, row=1, padx=30, pady=35, sticky="w")

impBtnT1 = Button(frameT1, text="Import Your Own .ZIP File",
                  width=90, command=importMsg)
impBtnT1.grid(column=0, row=2, padx=30, pady=55, sticky="w")

msgLblT1 = Label(frameT1, text="", bg="lightblue", width=90)
msgLblT1.grid(column=0, row=3, padx=30, sticky="w")

# tab2 frames elements
seperatorT2 = ttk.Separator(frameT2, orient=HORIZONTAL)
seperatorT2.grid(column=0, row=0, padx=15, pady=40)

countryLblT2 = Label(frameT2, text="Search for a country:", bg="lightblue")
countryLblT2.grid(column=1, row=0)

countryCmbT2 = ttk.Combobox(frameT2, width=62, state="readonly")
countryCmbT2["values"] = (allCountries)
countryCmbT2.current(0)
countryCmbT2.grid(column=2, row=0)

actLblT2 = Label(frameT2, text="Select an action:", bg="lightblue")
actLblT2.grid(column=1, row=1, sticky="w")

actCmbT2 = ttk.Combobox(frameT2, width=62, state="readonly")
actCmbT2["values"] = ("List correlation values of GDP factors",
                      "Display GDP factors in graphs",
                      "Predict GDP in graphs")
actCmbT2.current(0)
actCmbT2.grid(column=2, row=1)

actBtnT2 = Button(frameT2, text="Generate", width=15, command=tableWindow)
actBtnT2.grid(column=3, row=1, padx=20, sticky="w")

msgLblT2 = Label(
    frameT2, text="=================Search by GDP factor=================", bg="lightblue")
msgLblT2.grid(column=2, row=2, pady=40)

country2LblT2 = Label(frameT2, text="Search for a country:", bg="lightblue")
country2LblT2.grid(column=1, row=3)

country2CmbT2 = ttk.Combobox(frameT2, width=62, state="readonly")
country2CmbT2["values"] = (allCountries)
country2CmbT2.current(0)
country2CmbT2.grid(column=2, row=3)

facLblT2 = Label(frameT2, text="Select a GDP factor:", bg="lightblue")
facLblT2.grid(column=1, row=4, pady=30, sticky="w")

facCmbT2 = ttk.Combobox(frameT2, width=62, state="readonly")
facCmbT2["values"] = ("Agriculture, forestry, and fishing, value added (% of GDP)",
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
                      "Services, value added (% of GDP)",
                      "Surface area (sq. km)")
facCmbT2.current(0)
facCmbT2.grid(column=2, row=4)

facBtnT2 = Button(frameT2, text="Generate", width=15)
facBtnT2.grid(column=3, row=4, padx=20, sticky="w")

expBtnT2 = Button(frame2T2, text="Export All Data Sets For Country", width=90)
expBtnT2.grid(column=0, row=0, pady=30, padx=35, sticky="w")

# tab3 frame elements
seperatorT3 = ttk.Separator(frameT3, orient=HORIZONTAL)
seperatorT3.grid(column=0, row=0, padx=15, pady=30)

yearLblT3 = Label(frameT3, text="Select a year:", bg="lightblue")
yearLblT3.grid(column=1, row=0, sticky="w")

yearList = []
year = 1960
while year <= 2020:
    yearList.append(year)
    year += 1

yearCmbT3 = ttk.Combobox(frameT3, width=62, state="readonly")
yearCmbT3["values"] = (yearList)
yearCmbT3.current(0)
yearCmbT3.grid(column=2, row=0)

actLblT3 = Label(frameT3, text="Select an action:", bg="lightblue")
actLblT3.grid(column=1, row=1, pady=10, sticky="w")

actCmbT3 = ttk.Combobox(frameT3, width=62, state="readonly")
actCmbT3["values"] = ("List GDP of all countries",
                      "Display GDP of top 10 countries in bar graphs",
                      "Display GDP of bottom 10 countries in bar graphs")
actCmbT3.current(0)
actCmbT3.grid(column=2, row=1)

actBtnT3 = Button(frameT3, text="Generate", width=15)
actBtnT3.grid(column=3, row=1, padx=10, sticky="w")

facLblT3 = Label(frameT3, text="Select a GDP factor:", bg="lightblue")
facLblT3.grid(column=1, row=2, pady=30, sticky="w")

facCmbT3 = ttk.Combobox(frameT3, width=62, state="readonly")
facCmbT3["values"] = ("Agriculture, forestry, and fishing, value added (% of GDP)",
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
                      "Services, value added (% of GDP)",
                      "Surface area (sq. km)")
facCmbT3.current(0)
facCmbT3.grid(column=2, row=2)

facBtnT3 = Button(frameT3, text="Generate", width=15)
facBtnT3.grid(column=3, row=2, padx=10, sticky="w")

seperator2T3 = ttk.Separator(frameT3, orient=VERTICAL)
seperator2T3.grid(column=1, row=3, padx=15, pady=30)

preYearLblT3 = Label(
    frameT3, text="Select year of prediction:", bg="lightblue")
preYearLblT3.grid(column=1, row=4, sticky="w")

preYearList = []
preYear = 2021
while preYear <= 2099:
    preYearList.append(preYear)
    preYear += 1

preYearCmbT3 = ttk.Combobox(frameT3, width=62, state="readonly")
preYearCmbT3["values"] = (preYearList)
preYearCmbT3.current(0)
preYearCmbT3.grid(column=2, row=4)

actLbl2T3 = Label(frameT3, text="Select an action:", bg="lightblue")
actLbl2T3.grid(column=1, row=5, pady=30, sticky="w")

acT3CmbT3 = ttk.Combobox(frameT3, width=62, state="readonly")
acT3CmbT3["values"] = ("Display GDP in X years",
                       "Display top 10 GDP predictions in X years in bar graphs",
                       "Display bottom 10 GDP predictions in X years in bar graphs")
acT3CmbT3.current(0)
acT3CmbT3.grid(column=2, row=5)

actBtn2T3 = Button(frameT3, text="Generate", width=15)
actBtn2T3.grid(column=3, row=5, padx=10, sticky="w")

# Apply elements to frames
frameT1.grid_propagate(0)
frameT2.grid_propagate(0)
frame2T2.grid_propagate(0)
frameT3.grid_propagate(0)

# Size window and disable resize
window.geometry("700x400")
window.resizable(0, 0)

# Run window
window.mainloop()
