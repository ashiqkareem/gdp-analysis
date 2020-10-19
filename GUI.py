import tkinter
from tkinter import ttk
from tkinter import *

# Create window
window = tkinter.Tk()
window.title("GDP Analysis")

# Create tabs
tabList = ttk.Notebook(window)
tab1 = ttk.Frame(tabList)
tab2 = ttk.Frame(tabList)
tab3 = ttk.Frame(tabList)
tabList.add(tab1, text="View a Country's GDP")
tabList.add(tab2, text="Compare Countries' GDP")
tabList.add(tab3, text="Display all Countries' GDP")
tabList.pack(expand=1, fill="both")

# Create tab1 frames
topFrameT1 = Frame(tab1, width=800, height=160, bg="lightblue")
topFrameT1.grid(columnspan=3, row=0)
midFrameT1 = Frame(tab1, width=800, height=400, bg="lightgreen")
midFrameT1.grid(columnspan=3, row=2)
botFrameT1 = Frame(tab1, width=800, height=110, bg="salmon")
botFrameT1.grid(columnspan=3, row=4)

# Create dividers between tab1 frames
horFrame1T1 = Frame(tab1, width=800, height=5, bg="black")
horFrame1T1.grid(row=1, columnspan=3)
horFrame2T1 = Frame(tab1, width=800, height=5, bg="black")
horFrame2T1.grid(row=3, columnspan=3)

# tab1 top frame elements
countryLblT1 = Label(topFrameT1, text="Select Country:", bg="lightblue")
countryLblT1.grid(column=0, row=0, padx=50, pady=50)

countryCmbT1 = ttk.Combobox(topFrameT1, width=30)
countryCmbT1["values"] = (1, 2, 3, 4, 5)
countryCmbT1.current(0)
countryCmbT1.grid(column=1, row=0)

gdpBtnT1 = Button(topFrameT1, text="Show GDP", width=30)
gdpBtnT1.grid(column=3, row=0, padx=100, pady=10, sticky="e")

# tab1 middle frame elements
indicatorLblT1 = Label(midFrameT1, text="Indicators", bg="lightgreen")
indicatorLblT1.grid(column=0, row=0, padx=10, pady=20, sticky="w")

agriLblT1 = Label(midFrameT1, text="Agriculture, forestry, and fishing, value added (% of GDP)", bg="lightgreen")
agriLblT1.grid(column=0, row=1, padx=10, pady=8, sticky="w")
agriET1 = Entry(midFrameT1, width=5)
agriET1.grid(column=1, row=1)

araLblT1 = Label(midFrameT1, text="Arable land (% of land area)", bg="lightgreen")
araLblT1.grid(column=0, row=2, padx=10, pady=8, sticky="w")
araET1 = Entry(midFrameT1, width=5)
araET1.grid(column=1, row=2)

birthLblT1 = Label(midFrameT1, text="Birth rate, crude (per 1,000 people)", bg="lightgreen")
birthLblT1.grid(column=0, row=3, padx=10, pady=8, sticky="w")
birthET1 = Entry(midFrameT1, width=5)
birthET1.grid(column=1, row=3)

deathLblT1 = Label(midFrameT1, text="Death rate, crude (per 1,000 people)", bg="lightgreen")
deathLblT1.grid(column=0, row=4, padx=10, pady=8, sticky="w")
deathET1 = Entry(midFrameT1, width=5)
deathET1.grid(column=1, row=4)

gdpLblT1 = Label(midFrameT1, text="GDP per capita (constant LCU)", bg="lightgreen")
gdpLblT1.grid(column=0, row=5, padx=10, pady=8, sticky="w")
gdpET1 = Entry(midFrameT1, width=5)
gdpET1.grid(column=1, row=5)

netLblT1 = Label(midFrameT1, text="Individuals using the Internet (% of population)", bg="lightgreen")
netLblT1.grid(column=0, row=6, padx=10, pady=8, sticky="w")
netET1 = Entry(midFrameT1, width=5)
netET1.grid(column=1, row=6)

indLblT1 = Label(midFrameT1, text="Industry (including construction), value added (% of GDP)", bg="lightgreen")
indLblT1.grid(column=0, row=7, padx=10, pady=8, sticky="w")
indET1 = Entry(midFrameT1, width=5)
indET1.grid(column=1, row=7)

litLblT1 = Label(midFrameT1, text="Literacy rate, adult total (% of people ages 15 and above)", bg="lightgreen")
litLblT1.grid(column=0, row=8, padx=10, pady=8, sticky="w")
litET1 = Entry(midFrameT1, width=5)
litET1.grid(column=1, row=8)

updBtnT1 = Button(midFrameT1, text="Update Values", width=30)
updBtnT1.grid(column=0, row=9, padx=10, pady=10, sticky="w")

mobLblT1 = Label(midFrameT1, text="Mobile cellular subscriptions (per 100 people)", bg="lightgreen")
mobLblT1.grid(column=2, row=1, padx=55, pady=8, sticky="w")
mobET1 = Entry(midFrameT1, width=5)
mobET1.grid(column=3, row=1)

morLblT1 = Label(midFrameT1, text="Mortality rate, infant (per 1,000 live births)", bg="lightgreen")
morLblT1.grid(column=2, row=2, padx=55, pady=8, sticky="w")
morET1 = Entry(midFrameT1, width=5)
morET1.grid(column=3, row=2)

migLblT1 = Label(midFrameT1, text="Net Migration", bg="lightgreen")
migLblT1.grid(column=2, row=3, padx=55, pady=8, sticky="w")
migET1 = Entry(midFrameT1, width=5)
migET1.grid(column=3, row=3)

cropLblT1 = Label(midFrameT1, text="Permanent cropland (% of land area)", bg="lightgreen")
cropLblT1.grid(column=2, row=4, padx=55, pady=8, sticky="w")
cropET1 = Entry(midFrameT1, width=5)
cropET1.grid(column=3, row=4)

denLblT1 = Label(midFrameT1, text="Population density (people per sq. km of land area)", bg="lightgreen")
denLblT1.grid(column=2, row=5, padx=55, pady=8, sticky="w")
denET1 = Entry(midFrameT1, width=5)
denET1.grid(column=3, row=5)

popLblT1 = Label(midFrameT1, text="Population, total", bg="lightgreen")
popLblT1.grid(column=2, row=6, padx=55, pady=8, sticky="w")
popET1 = Entry(midFrameT1, width=5)
popET1.grid(column=3, row=6)

svcLblT1 = Label(midFrameT1, text="Services, value added (% of GDP)", bg="lightgreen")
svcLblT1.grid(column=2, row=7, padx=55, pady=8, sticky="w")
svcET1 = Entry(midFrameT1, width=5)
svcET1.grid(column=3, row=7)

surLblT1 = Label(midFrameT1, text="Surface area (sq. km)", bg="lightgreen")
surLblT1.grid(column=2, row=8, padx=55, pady=8, sticky="w")
surET1 = Entry(midFrameT1, width=5)
surET1.grid(column=3, row=8)

# tab1 bottom frame elements
top3BtnT1 = Button(botFrameT1, text="Display Top 3 GDP Factors", width=30)
top3BtnT1.grid(column=0, row=0, padx=23, pady=35)

bot3BtnT1 = Button(botFrameT1, text="Display Bottom 3 GDP Factors", width=30)
bot3BtnT1.grid(column=1, row=0, padx=23, pady=35)

preBtnT1 = Button(botFrameT1, text="Predict GDP", width=30)
preBtnT1.grid(column=2, row=0, padx=23, pady=35)

# Create tab2 frames
topFrameT2 = Frame(tab2, width=800, height=160, bg="lightblue")
topFrameT2.grid(columnspan=3, row=0)
midFrameT2 = Frame(tab2, width=800, height=400, bg="lightgreen")
midFrameT2.grid(columnspan=3, row=2)
botFrameT2 = Frame(tab2, width=800, height=110, bg="salmon")
botFrameT2.grid(columnspan=3, row=4)

# Create dividers between tab 2 frames
horFrame1T2 = Frame(tab2, width=800, height=5, bg="black")
horFrame1T2.grid(row=1, columnspan=3)
horFrame2T2 = Frame(tab2, width=800, height=5, bg="black")
horFrame2T2.grid(row=3, columnspan=3)

countryLbl1T2 = Label(topFrameT2, text="Select Country:", bg="lightblue")
countryLbl1T2.grid(column=0, row=0, padx=10, pady=15)

countryCmb1T2 = ttk.Combobox(topFrameT2, width=30)
countryCmb1T2["values"] = (1, 2, 3, 4, 5)
countryCmb1T2.current(0)
countryCmb1T2.grid(column=1, row=0)

countryLbl2T2 = Label(topFrameT2, text="Select Country:", bg="lightblue")
countryLbl2T2.grid(column=0, row=1, padx=10, pady=15)

countryCmb2T2 = ttk.Combobox(topFrameT2, width=30)
countryCmb2T2["values"] = (1, 2, 3, 4, 5)
countryCmb2T2.current(0)
countryCmb2T2.grid(column=1, row=1)

countryLbl3T2 = Label(topFrameT2, text="Select Country:", bg="lightblue")
countryLbl3T2.grid(column=0, row=2, padx=10, pady=15)

countryCmb3T2 = ttk.Combobox(topFrameT2, width=30)
countryCmb3T2["values"] = (1, 2, 3, 4, 5)
countryCmb3T2.current(0)
countryCmb3T2.grid(column=1, row=2)

sep1T1 = ttk.Separator(topFrameT2, orient=HORIZONTAL)
sep1T1.grid(column=2, row=0, padx=75)

countryLbl4T2 = Label(topFrameT2, text="Select Country:", bg="lightblue")
countryLbl4T2.grid(column=3, row=0, padx=10, pady=15)

countryCmb4T2 = ttk.Combobox(topFrameT2, width=30)
countryCmb4T2["values"] = (1, 2, 3, 4, 5)
countryCmb4T2.current(0)
countryCmb4T2.grid(column=4, row=0)

countryLbl5T2 = Label(topFrameT2, text="Select Country:", bg="lightblue")
countryLbl5T2.grid(column=3, row=1, padx=10, pady=15)

countryCmb5T2 = ttk.Combobox(topFrameT2, width=30)
countryCmb5T2["values"] = (1, 2, 3, 4, 5)
countryCmb5T2.current(0)
countryCmb5T2.grid(column=4, row=1)

countryLbl6T2 = Label(topFrameT2, text="Select Country:", bg="lightblue")
countryLbl6T2.grid(column=3, row=2, padx=10, pady=15)

countryCmb6T2 = ttk.Combobox(topFrameT2, width=30)
countryCmb6T2["values"] = (1, 2, 3, 4, 5)
countryCmb6T2.current(0)
countryCmb6T2.grid(column=4, row=2)

# tab2 middle frame elements
indicatorLblT2 = Label(midFrameT2, text="Indicators", bg="lightgreen")
indicatorLblT2.grid(column=0, row=0, padx=10, pady=20, sticky="w")

countryInCmbT2 = ttk.Combobox(midFrameT2, width=30)
countryInCmbT2["values"] = (1, 2, 3, 4, 5)
countryInCmbT2.current(0)
countryInCmbT2.grid(column=2, row=0, padx=55, sticky="w")

agriLblT2 = Label(midFrameT2, text="Agriculture, forestry, and fishing, value added (% of GDP)", bg="lightgreen")
agriLblT2.grid(column=0, row=1, padx=10, pady=8, sticky="w")
agriET2 = Entry(midFrameT2, width=5)
agriET2.grid(column=1, row=1)

araLblT2 = Label(midFrameT2, text="Arable land (% of land area)", bg="lightgreen")
araLblT2.grid(column=0, row=2, padx=10, pady=8, sticky="w")
araET2 = Entry(midFrameT2, width=5)
araET2.grid(column=1, row=2)

birthLblT2 = Label(midFrameT2, text="Birth rate, crude (per 1,000 people)", bg="lightgreen")
birthLblT2.grid(column=0, row=3, padx=10, pady=8, sticky="w")
birthET2 = Entry(midFrameT2, width=5)
birthET2.grid(column=1, row=3)

deathLblT2 = Label(midFrameT2, text="Death rate, crude (per 1,000 people)", bg="lightgreen")
deathLblT2.grid(column=0, row=4, padx=10, pady=8, sticky="w")
deathET2 = Entry(midFrameT2, width=5)
deathET2.grid(column=1, row=4)

gdpLblT2 = Label(midFrameT2, text="GDP per capita (constant LCU)", bg="lightgreen")
gdpLblT2.grid(column=0, row=5, padx=10, pady=8, sticky="w")
gdpET2 = Entry(midFrameT2, width=5)
gdpET2.grid(column=1, row=5)

netLblT2 = Label(midFrameT2, text="Individuals using the Internet (% of population)", bg="lightgreen")
netLblT2.grid(column=0, row=6, padx=10, pady=8, sticky="w")
netET2 = Entry(midFrameT2, width=5)
netET2.grid(column=1, row=6)

indLblT2 = Label(midFrameT2, text="Industry (including construction), value added (% of GDP)", bg="lightgreen")
indLblT2.grid(column=0, row=7, padx=10, pady=8, sticky="w")
indET2 = Entry(midFrameT2, width=5)
indET2.grid(column=1, row=7)

litLblT2 = Label(midFrameT2, text="Literacy rate, adult total (% of people ages 15 and above)", bg="lightgreen")
litLblT2.grid(column=0, row=8, padx=10, pady=8, sticky="w")
litET2 = Entry(midFrameT2, width=5)
litET2.grid(column=1, row=8)

updBtnT2 = Button(midFrameT2, text="Update Values", width=30)
updBtnT2.grid(column=0, row=9, padx=10, pady=10, sticky="w")

mobLblT2 = Label(midFrameT2, text="Mobile cellular subscriptions (per 100 people)", bg="lightgreen")
mobLblT2.grid(column=2, row=1, padx=55, pady=8, sticky="w")
mobET2 = Entry(midFrameT2, width=5)
mobET2.grid(column=3, row=1)

morLblT2 = Label(midFrameT2, text="Mortality rate, infant (per 1,000 live births)", bg="lightgreen")
morLblT2.grid(column=2, row=2, padx=55, pady=8, sticky="w")
morET2 = Entry(midFrameT2, width=5)
morET2.grid(column=3, row=2)

migLblT2 = Label(midFrameT2, text="Net Migration", bg="lightgreen")
migLblT2.grid(column=2, row=3, padx=55, pady=8, sticky="w")
migET2 = Entry(midFrameT2, width=5)
migET2.grid(column=3, row=3)

cropLblT2 = Label(midFrameT2, text="Permanent cropland (% of land area)", bg="lightgreen")
cropLblT2.grid(column=2, row=4, padx=55, pady=8, sticky="w")
cropET2 = Entry(midFrameT2, width=5)
cropET2.grid(column=3, row=4)

denLblT2 = Label(midFrameT2, text="Population density (people per sq. km of land area)", bg="lightgreen")
denLblT2.grid(column=2, row=5, padx=55, pady=8, sticky="w")
denET2 = Entry(midFrameT2, width=5)
denET2.grid(column=3, row=5)

popLblT2 = Label(midFrameT2, text="Population, total", bg="lightgreen")
popLblT2.grid(column=2, row=6, padx=55, pady=8, sticky="w")
popET2 = Entry(midFrameT2, width=5)
popET2.grid(column=3, row=6)

svcLblT2 = Label(midFrameT2, text="Services, value added (% of GDP)", bg="lightgreen")
svcLblT2.grid(column=2, row=7, padx=55, pady=8, sticky="w")
svcET2 = Entry(midFrameT2, width=5)
svcET2.grid(column=3, row=7)

surLblT2 = Label(midFrameT2, text="Surface area (sq. km)", bg="lightgreen")
surLblT2.grid(column=2, row=8, padx=55, pady=8, sticky="w")
surET2 = Entry(midFrameT2, width=5)
surET2.grid(column=3, row=8)

# tab1 bottom frame elements
recessionBtnT2 = Button(botFrameT2, text="Simulate Recession", width=30)
recessionBtnT2.grid(column=0, row=0, padx=85, pady=35)

pandemicBtnT2 = Button(botFrameT2, text="Simulate Pandemic", width=30)
pandemicBtnT2.grid(column=1, row=0, padx=85, pady=35)

# Apply elements to frames
topFrameT1.grid_propagate(0)
midFrameT1.grid_propagate(0)
botFrameT1.grid_propagate(0)
topFrameT2.grid_propagate(0)
midFrameT2.grid_propagate(0)
botFrameT2.grid_propagate(0)

# Size window and disable resize
window.geometry("800x700")
window.resizable(0, 0)

# Run window
window.mainloop()
