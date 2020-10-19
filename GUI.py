import tkinter
from tkinter import ttk
from tkinter import *

#Create window
window = tkinter.Tk()
window.title("GDP Analysis")

#Create tabs
tabList = ttk.Notebook(window)
tab1 = ttk.Frame(tabList)
tab2 = ttk.Frame(tabList)
tab3 = ttk.Frame(tabList)
tabList.add(tab1, text="View a Country's GDP")
tabList.add(tab2, text="Compare Countries' GDP")
tabList.add(tab3, text="Display all Countries' GDP")
tabList.pack(expand=1, fill="both")

#Create tab1 frames
topFrame1 = Frame(tab1, width=800, height=80, bg="lightblue")
topFrame1.grid(columnspan=3, row=0)
midFrame1 = Frame(tab1, width=800, height=400, bg="lightgreen")
midFrame1.grid(columnspan=3, row=2)
botFrame1 = Frame(tab1, width=800, height=110, bg="salmon")
botFrame1.grid(columnspan=3, row=4)

#Create dividers between tab1 frames
horFrame1 = Frame(tab1, width=800, height=5, bg="black")
horFrame1.grid(row=1, columnspan=3)
horFrame2 = Frame(tab1, width=800, height=5, bg="black")
horFrame2.grid(row=3, columnspan=3)

#tab1 top frame elements
countryLbl = Label(topFrame1, text = "Select Country:", bg="lightblue")
countryLbl.grid(column=0, row=0, padx=10, pady=20)

countryCmb = ttk.Combobox(topFrame1, width=30)
countryCmb["values"]=(1,2,3,4,5)
countryCmb.current(0)
countryCmb.grid(column=1, row=0)

gdpBtn = Button(topFrame1, text="Show GDP", width=30)
gdpBtn.grid(column=3, row=0, padx=240, pady=10, sticky="e")

#tab1 middle frame elements
indicatorLbl = Label(midFrame1, text = "Indicators", bg="lightgreen")
indicatorLbl.grid(column=0, row=0, padx=10, pady=20, sticky="w")

agriLbl = Label(midFrame1, text = "Agriculture, forestry, and fishing, value added (% of GDP)", bg="lightgreen")
agriLbl.grid(column=0, row=1, padx=10, pady=8, sticky="w")
agriE = Entry(midFrame1, width=5)
agriE.grid(column=1, row=1)

araLbl = Label(midFrame1, text = "Arable land (% of land area)", bg="lightgreen")
araLbl.grid(column=0, row=2, padx=10, pady=8, sticky="w")
araE = Entry(midFrame1, width=5)
araE.grid(column=1, row=2)

birthLbl = Label(midFrame1, text = "Birth rate, crude (per 1,000 people)", bg="lightgreen")
birthLbl.grid(column=0, row=3, padx=10, pady=8, sticky="w")
birthE = Entry(midFrame1, width=5)
birthE.grid(column=1, row=3)

deathLbl = Label(midFrame1, text = "Death rate, crude (per 1,000 people)", bg="lightgreen")
deathLbl.grid(column=0, row=4, padx=10, pady=8, sticky="w")
deathE = Entry(midFrame1, width=5)
deathE.grid(column=1, row=4)

gdpLbl = Label(midFrame1, text = "GDP per capita (constant LCU)", bg="lightgreen")
gdpLbl.grid(column=0, row=5, padx=10, pady=8, sticky="w")
gdpE = Entry(midFrame1, width=5)
gdpE.grid(column=1, row=5)

netLbl = Label(midFrame1, text = "Individuals using the Internet (% of population)", bg="lightgreen")
netLbl.grid(column=0, row=6, padx=10, pady=8, sticky="w")
netE = Entry(midFrame1, width=5)
netE.grid(column=1, row=6)

indLbl = Label(midFrame1, text = "Industry (including construction), value added (% of GDP)", bg="lightgreen")
indLbl.grid(column=0, row=7, padx=10, pady=8, sticky="w")
indE = Entry(midFrame1, width=5)
indE.grid(column=1, row=7)

litLbl = Label(midFrame1, text = "Literacy rate, adult total (% of people ages 15 and above)", bg="lightgreen")
litLbl.grid(column=0, row=8, padx=10, pady=8, sticky="w")
litE = Entry(midFrame1, width=5)
litE.grid(column=1, row=8)

updBtn = Button(midFrame1, text="Update Values", width=30)
updBtn.grid(column=0, row=9, padx=10, pady=10, sticky="w")

mobLbl = Label(midFrame1, text = "Mobile cellular subscriptions (per 100 people)", bg="lightgreen")
mobLbl.grid(column=2, row=1, padx=55, pady=8, sticky="w")
mobE = Entry(midFrame1, width=5)
mobE.grid(column=3, row=1)

morLbl = Label(midFrame1, text = "Mortality rate, infant (per 1,000 live births)", bg="lightgreen")
morLbl.grid(column=2, row=2, padx=55, pady=8, sticky="w")
morE = Entry(midFrame1, width=5)
morE.grid(column=3, row=2)

migLbl = Label(midFrame1, text = "Net Migration", bg="lightgreen")
migLbl.grid(column=2, row=3, padx=55, pady=8, sticky="w")
migE = Entry(midFrame1, width=5)
migE.grid(column=3, row=3)

cropLbl = Label(midFrame1, text = "Permanent cropland (% of land area)", bg="lightgreen")
cropLbl.grid(column=2, row=4, padx=55, pady=8, sticky="w")
cropE = Entry(midFrame1, width=5)
cropE.grid(column=3, row=4)

denLbl = Label(midFrame1, text = "Population density (people per sq. km of land area)", bg="lightgreen")
denLbl.grid(column=2, row=5, padx=55, pady=8, sticky="w")
denE = Entry(midFrame1, width=5)
denE.grid(column=3, row=5)

popLbl = Label(midFrame1, text = "Population, total", bg="lightgreen")
popLbl.grid(column=2, row=6, padx=55, pady=8, sticky="w")
popE = Entry(midFrame1, width=5)
popE.grid(column=3, row=6)

svcLbl = Label(midFrame1, text = "Services, value added (% of GDP)", bg="lightgreen")
svcLbl.grid(column=2, row=7, padx=55, pady=8, sticky="w")
svcE = Entry(midFrame1, width=5)
svcE.grid(column=3, row=7)

surLbl = Label(midFrame1, text = "Surface area (sq. km)", bg="lightgreen")
surLbl.grid(column=2, row=8, padx=55, pady=8, sticky="w")
surE = Entry(midFrame1, width=5)
surE.grid(column=3, row=8)

#tab1 bottom frame elements
top3Btn = Button(botFrame1, text="Display Top 3 GDP Factors", width=30)
top3Btn.grid(column=0, row=0, padx=23, pady=30)

bot3Btn = Button(botFrame1, text="Display Bottom 3 GDP Factors", width =30)
bot3Btn.grid(column=1, row=0, padx=23, pady=30)

preBtn = Button(botFrame1, text="Predict GDP", width=30)
preBtn.grid(column=2, row=0, padx=23, pady=30)

#Create tab2 frames
topFrame2 = Frame(tab2, width=800, height=80, bg="lightblue")
topFrame2.grid(columnspan=3, row=0)
midFrame2 = Frame(tab2, width=800, height=400, bg="lightgreen")
midFrame2.grid(columnspan=3, row=2)
botFrame2 = Frame(tab2, width=800, height=110, bg="salmon")
botFrame2.grid(columnspan=3, row=4)

#Create dividers between tab 2 frames
horFrame1 = Frame(tab2, width=800, height=5, bg="black")
horFrame1.grid(row=1, columnspan=3)
horFrame2 = Frame(tab2, width=800, height=5, bg="black")
horFrame2.grid(row=3, columnspan=3)

#Apply elements to frames
topFrame1.grid_propagate(0)
midFrame1.grid_propagate(0)
botFrame1.grid_propagate(0)
topFrame2.grid_propagate(0)
midFrame2.grid_propagate(0)
botFrame2.grid_propagate(0)

#Size window and disable resize
window.geometry("800x600")
window.resizable(0,0)

#Run window
window.mainloop()