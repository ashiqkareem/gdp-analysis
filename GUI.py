import tkinter
from tkinter import ttk
from tkinter import *

#Open new window function
def openNewWindow(): 
    newWindow = Toplevel(window) 
    newWindow.title("GDP Analysis") 
    newWindow.geometry("500x500") 
    newWindow.resizable(0, 0)

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
topFrameT1 = Frame(tab1, width=800, height=100, bg="lightblue")
topFrameT1.grid(columnspan=3, row=0)
midFrameT1 = Frame(tab1, width=800, height=480, bg="lightgreen")
midFrameT1.grid(columnspan=3, row=2)
botFrameT1 = Frame(tab1, width=800, height=100, bg="salmon")
botFrameT1.grid(columnspan=3, row=4)

# Create dividers between tab1 frames
horFrame1T1 = Frame(tab1, width=800, height=5, bg="black")
horFrame1T1.grid(row=1, columnspan=3)
horFrame2T1 = Frame(tab1, width=800, height=5, bg="black")
horFrame2T1.grid(row=3, columnspan=3)

# tab1 top frame elements
countryLblT1 = Label(topFrameT1, text="Select Country:", bg="lightblue")
countryLblT1.grid(column=0, row=0, padx=30, pady=35)

countryCmbT1 = ttk.Combobox(topFrameT1, width=30)
countryCmbT1["values"] = (1, 2, 3, 4, 5)
countryCmbT1.current(0)
countryCmbT1.grid(column=1, row=0)

gdpBtnT1 = Button(topFrameT1, text="Show GDP", width=30, command=openNewWindow)
gdpBtnT1.grid(column=3, row=0, padx=140, sticky="e")

# tab1 middle frame elements
correlationLblT1 = Label(midFrameT1, text="Correlation Values", bg="lightgreen")
correlationLblT1.grid(column=0, row=0, padx=5, pady=40, sticky="w")

agriLblT1 = Label(midFrameT1, text="Agriculture, forestry, and fishing, value added (% of GDP)", bg="lightgreen")
agriLblT1.grid(column=0, row=1, padx=5, pady=8, sticky="w")
agriET1 = Label(midFrameT1, width=3, text="-1", bg="white")
agriET1.grid(column=1, row=1)
agriBtnT1 = Button(midFrameT1, text="Graph")
agriBtnT1.grid(column=2, row=1, padx=10)

araLblT1 = Label(midFrameT1, text="Arable land (% of land area)", bg="lightgreen")
araLblT1.grid(column=0, row=2, padx=5, pady=8, sticky="w")
araET1 = Label(midFrameT1, width=3, text="-1", bg="white")
araET1.grid(column=1, row=2)
araBtnT1 = Button(midFrameT1, text="Graph")
araBtnT1.grid(column=2, row=2, padx=10)

birthLblT1 = Label(midFrameT1, text="Birth rate, crude (per 1,000 people)", bg="lightgreen")
birthLblT1.grid(column=0, row=3, padx=5, pady=8, sticky="w")
birthET1 = Label(midFrameT1, width=3, text="-1", bg="white")
birthET1.grid(column=1, row=3)
birthBtnT1 = Button(midFrameT1, text="Graph")
birthBtnT1.grid(column=2, row=3, padx=10)

deathLblT1 = Label(midFrameT1, text="Death rate, crude (per 1,000 people)", bg="lightgreen")
deathLblT1.grid(column=0, row=4, padx=5, pady=8, sticky="w")
deathET1 = Label(midFrameT1, width=3, text="-1", bg="white")
deathET1.grid(column=1, row=4)
deathBtnT1 = Button(midFrameT1, text="Graph")
deathBtnT1.grid(column=2, row=4, padx=10)

netLblT1 = Label(midFrameT1, text="Individuals using the Internet (% of population)", bg="lightgreen")
netLblT1.grid(column=0, row=5, padx=5, pady=8, sticky="w")
netET1 = Label(midFrameT1, width=3, text="-1", bg="white")
netET1.grid(column=1, row=5)
netBtnT1 = Button(midFrameT1, text="Graph")
netBtnT1.grid(column=2, row=5, padx=10)

indLblT1 = Label(midFrameT1, text="Industry (including construction), value added (% of GDP)", bg="lightgreen")
indLblT1.grid(column=0, row=6, padx=5, pady=8, sticky="w")
indET1 = Label(midFrameT1, width=3, text="-1", bg="white")
indET1.grid(column=1, row=6)
indBtnT1 = Button(midFrameT1, text="Graph")
indBtnT1.grid(column=2, row=6, padx=10)

litLblT1 = Label(midFrameT1, text="Literacy rate, adult total (% of people ages 15 and above)", bg="lightgreen")
litLblT1.grid(column=0, row=7, padx=5, pady=8, sticky="w")
litET1 = Label(midFrameT1, width=3, text="-1", bg="white")
litET1.grid(column=1, row=7)
litBtnT1 = Button(midFrameT1, text="Graph")
litBtnT1.grid(column=2, row=7, padx=10)

mobLblT1 = Label(midFrameT1, text="Mobile cellular subscriptions (per 100 people)", bg="lightgreen")
mobLblT1.grid(column=0, row=8, padx=5, pady=8, sticky="w")
mobET1 = Label(midFrameT1, width=3, text="-1", bg="white")
mobET1.grid(column=1, row=8)
mobBtnT1 = Button(midFrameT1, text="Graph")
mobBtnT1.grid(column=2, row=8, padx=10)

valBtnT1 = Button(midFrameT1, width="40",text="Generate Values")
valBtnT1.grid(column=0, row=9, padx=5, pady=30, sticky="w")

morLblT1 = Label(midFrameT1, text="Mortality rate, infant (per 1,000 live births)", bg="lightgreen")
morLblT1.grid(column=3, row=1, padx=10, pady=8, sticky="w")
morET1 = Label(midFrameT1, width=3, text="-1", bg="white")
morET1.grid(column=4, row=1)
morBtnT1 = Button(midFrameT1, text="Graph")
morBtnT1.grid(column=5, row=1, padx=10)

migLblT1 = Label(midFrameT1, text="Net Migration", bg="lightgreen")
migLblT1.grid(column=3, row=2, padx=10, pady=8, sticky="w")
migET1 = Label(midFrameT1, width=3, text="-1", bg="white")
migET1.grid(column=4, row=2)
migBtnT1 = Button(midFrameT1, text="Graph")
migBtnT1.grid(column=5, row=2, padx=10)

cropLblT1 = Label(midFrameT1, text="Permanent cropland (% of land area)", bg="lightgreen")
cropLblT1.grid(column=3, row=3, padx=10, pady=8, sticky="w")
cropET1 = Label(midFrameT1, width=3, text="-1", bg="white")
cropET1.grid(column=4, row=3)
cropBtnT1 = Button(midFrameT1, text="Graph")
cropBtnT1.grid(column=5, row=3, padx=10)

denLblT1 = Label(midFrameT1, text="Population density (people per sq. km of land area)", bg="lightgreen")
denLblT1.grid(column=3, row=4, padx=10, pady=8, sticky="w")
denET1 = Label(midFrameT1, width=3, text="-1", bg="white")
denET1.grid(column=4, row=4)
denBtnT1 = Button(midFrameT1, text="Graph")
denBtnT1.grid(column=5, row=4, padx=10)

popLblT1 = Label(midFrameT1, text="Population, total", bg="lightgreen")
popLblT1.grid(column=3, row=5, padx=10, pady=8, sticky="w")
popET1 = Label(midFrameT1, width=3, text="-1", bg="white")
popET1.grid(column=4, row=5)
popBtnT1 = Button(midFrameT1, text="Graph")
popBtnT1.grid(column=5, row=5, padx=10)

svcLblT1 = Label(midFrameT1, text="Services, value added (% of GDP)", bg="lightgreen")
svcLblT1.grid(column=3, row=6, padx=10, pady=8, sticky="w")
svcET1 = Label(midFrameT1, width=3, text="-1", bg="white")
svcET1.grid(column=4, row=6)
svcBtnT1 = Button(midFrameT1, text="Graph")
svcBtnT1.grid(column=5, row=6, padx=10)

surLblT1 = Label(midFrameT1, text="Surface area (sq. km)", bg="lightgreen")
surLblT1.grid(column=3, row=7, padx=10, pady=8, sticky="w")
surET1 = Label(midFrameT1, width=3, text="-1", bg="white")
surET1.grid(column=4, row=7)
surBtnT1 = Button(midFrameT1, text="Graph")
surBtnT1.grid(column=5, row=7, padx=10)

# tab1 bottom frame elements
top3BtnT1 = Button(botFrameT1, text="Display Top 3 GDP Factors", width=30)
top3BtnT1.grid(column=0, row=0, padx=23, pady=35)

bot3BtnT1 = Button(botFrameT1, text="Display Bottom 3 GDP Factors", width=30)
bot3BtnT1.grid(column=1, row=0, padx=23, pady=35)

preBtnT1 = Button(botFrameT1, text="Predict GDP", width=30)
preBtnT1.grid(column=2, row=0, padx=23, pady=35)

# Create tab2 frames
topFrameT2 = Frame(tab2, width=800, height=100, bg="lightblue")
topFrameT2.grid(columnspan=3, row=0)
midFrameT2 = Frame(tab2, width=800, height=480, bg="lightgreen")
midFrameT2.grid(columnspan=3, row=2)
botFrameT2 = Frame(tab2, width=800, height=100, bg="salmon")
botFrameT2.grid(columnspan=3, row=4)

# Create dividers between tab 2 frames
horFrame1T2 = Frame(tab2, width=800, height=5, bg="black")
horFrame1T2.grid(row=1, columnspan=3)
horFrame2T2 = Frame(tab2, width=800, height=5, bg="black")
horFrame2T2.grid(row=3, columnspan=3)

# tab2 top frame elements
countryLbl1T2 = Label(topFrameT2, text="Select Country:", bg="lightblue")
countryLbl1T2.grid(column=0, row=0, padx=30, pady=35)

countryCmb1T2 = ttk.Combobox(topFrameT2, width=30)
countryCmb1T2["values"] = (1, 2, 3, 4, 5)
countryCmb1T2.current(0)
countryCmb1T2.grid(column=1, row=0)

seperator1T2 = ttk.Separator(topFrameT2,orient=HORIZONTAL)
seperator1T2.grid(column=2, row=0, padx=25, pady=35)

countryLbl2T2 = Label(topFrameT2, text="Select Country:", bg="lightblue")
countryLbl2T2.grid(column=3, row=0, padx=30, pady=35)

countryCmb2T2 = ttk.Combobox(topFrameT2, width=30)
countryCmb2T2["values"] = (1, 2, 3, 4, 5)
countryCmb2T2.current(0)
countryCmb2T2.grid(column=4, row=0)

# tab2 middle frame elements
correlationLblT2 = Label(midFrameT2, text="Correlation Values", bg="lightgreen")
correlationLblT2.grid(column=0, row=0, padx=5, pady=40, sticky="w")

agriLblT2 = Label(midFrameT2, text="Agriculture, forestry, and fishing, value added (% of GDP)", bg="lightgreen")
agriLblT2.grid(column=0, row=1, padx=5, pady=8, sticky="w")
agriET2 = Label(midFrameT2, text="-1", bg="white")
agriET2.grid(column=1, row=1)
agriE2T2 = Label(midFrameT2, text="-1", bg="white")
agriE2T2.grid(column=2, row=1, padx=3)
agriBtnT2 = Button(midFrameT2, text="Graph")
agriBtnT2.grid(column=3, row=1, padx=3)

araLblT2 = Label(midFrameT2, text="Arable land (% of land area)", bg="lightgreen")
araLblT2.grid(column=0, row=2, padx=5, pady=8, sticky="w")
araET2 = Label(midFrameT2, text="-1", bg="white")
araET2.grid(column=1, row=2)
araE2T2 = Label(midFrameT2, text="-1", bg="white")
araE2T2.grid(column=2, row=2, padx=3)
araBtnT2 = Button(midFrameT2, text="Graph")
araBtnT2.grid(column=3, row=2, padx=3)

birthLblT2 = Label(midFrameT2, text="Birth rate, crude (per 1,000 people)", bg="lightgreen")
birthLblT2.grid(column=0, row=3, padx=5, pady=8, sticky="w")
birthET2 = Label(midFrameT2, text="-1", bg="white")
birthET2.grid(column=1, row=3)
birthE2T2 = Label(midFrameT2, text="-1", bg="white")
birthE2T2.grid(column=2, row=3, padx=3)
birthBtnT2 = Button(midFrameT2, text="Graph")
birthBtnT2.grid(column=3, row=3, padx=3)

deathLblT2 = Label(midFrameT2, text="Death rate, crude (per 1,000 people)", bg="lightgreen")
deathLblT2.grid(column=0, row=4, padx=5, pady=8, sticky="w")
deathET2 = Label(midFrameT2, text="-1", bg="white")
deathET2.grid(column=1, row=4)
deathE2T2 = Label(midFrameT2, text="-1", bg="white")
deathE2T2.grid(column=2, row=4, padx=3)
deathBtnT2 = Button(midFrameT2, text="Graph")
deathBtnT2.grid(column=3, row=4, padx=3)

netLblT2 = Label(midFrameT2, text="Individuals using the Internet (% of population)", bg="lightgreen")
netLblT2.grid(column=0, row=5, padx=5, pady=8, sticky="w")
netET2 = Label(midFrameT2, text="-1", bg="white")
netET2.grid(column=1, row=5)
netE2T2 = Label(midFrameT2, text="-1", bg="white")
netE2T2.grid(column=2, row=5, padx=3)
netBtnT2 = Button(midFrameT2, text="Graph")
netBtnT2.grid(column=3, row=5, padx=3)

indLblT2 = Label(midFrameT2, text="Industry (including construction), value added (% of GDP)", bg="lightgreen")
indLblT2.grid(column=0, row=6, padx=5, pady=8, sticky="w")
indET2 = Label(midFrameT2, text="-1", bg="white")
indET2.grid(column=1, row=6)
indE2T2 = Label(midFrameT2, text="-1", bg="white")
indE2T2.grid(column=2, row=6, padx=3)
indBtnT2 = Button(midFrameT2, text="Graph")
indBtnT2.grid(column=3, row=6, padx=3)

litLblT2 = Label(midFrameT2, text="Literacy rate, adult total (% of people ages 15 and above)", bg="lightgreen")
litLblT2.grid(column=0, row=7, padx=5, pady=8, sticky="w")
litET2 = Label(midFrameT2, text="-1", bg="white")
litET2.grid(column=1, row=7)
litE2T2 = Label(midFrameT2, text="-1", bg="white")
litE2T2.grid(column=2, row=7, padx=3)
litBtnT2 = Button(midFrameT2, text="Graph")
litBtnT2.grid(column=3, row=7, padx=3)

mobLblT2 = Label(midFrameT2, text="Mobile cellular subscriptions (per 100 people)", bg="lightgreen")
mobLblT2.grid(column=0, row=8, padx=5, pady=8, sticky="w")
mobET2 = Label(midFrameT2, text="-1", bg="white")
mobET2.grid(column=1, row=8)
mobE2T2 = Label(midFrameT2, text="-1", bg="white")
mobE2T2.grid(column=2, row=8, padx=3)
mobBtnT2 = Button(midFrameT2, text="Graph")
mobBtnT2.grid(column=3, row=8, padx=3)

valBtnT2 = Button(midFrameT2, width="40",text="Generate Values")
valBtnT2.grid(column=0, row=9, padx=5, pady=30, sticky="w")

morLblT2 = Label(midFrameT2, text="Mortality rate, infant (per 1,000 live births)", bg="lightgreen")
morLblT2.grid(column=4, row=1, padx=5, pady=8, sticky="w")
morET2 = Label(midFrameT2, text="-1", bg="white")
morET2.grid(column=5, row=1)
morE2T2 = Label(midFrameT2, text="-1", bg="white")
morE2T2.grid(column=6, row=1, padx=3)
morBtnT2 = Button(midFrameT2, text="Graph")
morBtnT2.grid(column=7, row=1, padx=3)

migLblT2 = Label(midFrameT2, text="Net Migration", bg="lightgreen")
migLblT2.grid(column=4, row=2, padx=5, pady=8, sticky="w")
migET2 = Label(midFrameT2, text="-1", bg="white")
migET2.grid(column=5, row=2)
migE2T2 = Label(midFrameT2, text="-1", bg="white")
migE2T2.grid(column=6, row=2, padx=3)
migBtnT2 = Button(midFrameT2, text="Graph")
migBtnT2.grid(column=7, row=2, padx=3)

cropLblT2 = Label(midFrameT2, text="Permanent cropland (% of land area)", bg="lightgreen")
cropLblT2.grid(column=4, row=3, padx=10, pady=8, sticky="w")
cropET2 = Label(midFrameT2, text="-1", bg="white")
cropET2.grid(column=5, row=3)
cropE2T2 = Label(midFrameT2, text="-1", bg="white")
cropE2T2.grid(column=6, row=3, padx=3)
cropBtnT2 = Button(midFrameT2, text="Graph")
cropBtnT2.grid(column=7, row=3, padx=3)

denLblT2 = Label(midFrameT2, text="Population density (people per sq. km of land area)", bg="lightgreen")
denLblT2.grid(column=4, row=4, padx=10, pady=8, sticky="w")
denET2 = Label(midFrameT2, text="-1", bg="white")
denET2.grid(column=5, row=4)
denE2T2 = Label(midFrameT2, text="-1", bg="white")
denE2T2.grid(column=6, row=4, padx=3)
denBtnT2 = Button(midFrameT2, text="Graph")
denBtnT2.grid(column=7, row=4, padx=3)

popLblT2 = Label(midFrameT2, text="Population, total", bg="lightgreen")
popLblT2.grid(column=4, row=5, padx=10, pady=8, sticky="w")
popET2 = Label(midFrameT2, text="-1", bg="white")
popET2.grid(column=5, row=5)
popE2T2 = Label(midFrameT2, text="-1", bg="white")
popE2T2.grid(column=6, row=5, padx=3)
popBtnT2 = Button(midFrameT2, text="Graph")
popBtnT2.grid(column=7, row=5, padx=3)

svcLblT2 = Label(midFrameT2, text="Services, value added (% of GDP)", bg="lightgreen")
svcLblT2.grid(column=4, row=6, padx=10, pady=8, sticky="w")
svcET2 = Label(midFrameT2, text="-1", bg="white")
svcET2.grid(column=5, row=6)
svcE2T2 = Label(midFrameT2, text="-1", bg="white")
svcE2T2.grid(column=6, row=6, padx=3)
svcBtnT2 = Button(midFrameT2, text="Graph")
svcBtnT2.grid(column=7, row=6, padx=3)

surLblT2 = Label(midFrameT2, text="Surface area (sq. km)", bg="lightgreen")
surLblT2.grid(column=4, row=7, padx=10, pady=8, sticky="w")
surET2 = Label(midFrameT2, text="-1", bg="white")
surET2.grid(column=5, row=7)
surE2T2 = Label(midFrameT2, text="-1", bg="white")
surE2T2.grid(column=6, row=7, padx=3)
surBtnT2 = Button(midFrameT2, text="Graph")
surBtnT2.grid(column=7, row=7, padx=3)

# tab2 bottom frame elements
recessionBtnT2 = Button(botFrameT2, text="Simulate Recession", width=30)
recessionBtnT2.grid(column=0, row=0, padx=85, pady=35)

pandemicBtnT2 = Button(botFrameT2, text="Simulate Pandemic", width=30)
pandemicBtnT2.grid(column=1, row=0, padx=85, pady=35)

# Create tab3 frames
topFrameT3 = Frame(tab3, width=800, height=100, bg="lightblue")
topFrameT3.grid(columnspan=3, row=0)
midFrameT3 = Frame(tab3, width=800, height=480, bg="lightgreen")
midFrameT3.grid(columnspan=3, row=2)
botFrameT3 = Frame(tab3, width=800, height=100, bg="salmon")
botFrameT3.grid(columnspan=3, row=4)

# Create dividers between tab3 frames
horFrame1T3 = Frame(tab3, width=800, height=5, bg="black")
horFrame1T3.grid(row=1, columnspan=3)
horFrame2T3 = Frame(tab3, width=800, height=5, bg="black")
horFrame2T3.grid(row=3, columnspan=3)

# tab3 top frame elements
seperator1T3 = ttk.Separator(topFrameT3,orient=HORIZONTAL)
seperator1T3.grid(column=0, row=0, padx=105, pady=35)

yearLbl1T3 = Label(topFrameT3, text="Select Year:", bg="lightblue")
yearLbl1T3.grid(column=1, row=0, padx=30, pady=35)

yearCmb1T3 = ttk.Combobox(topFrameT3, width=30)
yearCmb1T3["values"] = (1, 2, 3, 4, 5)
yearCmb1T3.current(0)
yearCmb1T3.grid(column=2, row=0)

# tab3 middle frame elements
correlationLblT3 = Label(midFrameT3, text="Correlation Values", bg="lightgreen")
correlationLblT3.grid(column=0, row=0, padx=5, pady=40, sticky="w")

agriLblT3 = Label(midFrameT3, text="Agriculture, forestry, and fishing, value added (% of GDP)", bg="lightgreen")
agriLblT3.grid(column=0, row=1, padx=5, pady=8, sticky="w")
agriET3 = Label(midFrameT3, width=3, text="-1", bg="white")
agriET3.grid(column=1, row=1)
agriBtnT3 = Button(midFrameT3, text="Graph")
agriBtnT3.grid(column=2, row=1, padx=10)

araLblT3 = Label(midFrameT3, text="Arable land (% of land area)", bg="lightgreen")
araLblT3.grid(column=0, row=2, padx=5, pady=8, sticky="w")
araET3 = Label(midFrameT3, width=3, text="-1", bg="white")
araET3.grid(column=1, row=2)
araBtnT3 = Button(midFrameT3, text="Graph")
araBtnT3.grid(column=2, row=2, padx=10)

birthLblT3 = Label(midFrameT3, text="Birth rate, crude (per 1,000 people)", bg="lightgreen")
birthLblT3.grid(column=0, row=3, padx=5, pady=8, sticky="w")
birthET3 = Label(midFrameT3, width=3, text="-1", bg="white")
birthET3.grid(column=1, row=3)
birthBtnT3 = Button(midFrameT3, text="Graph")
birthBtnT3.grid(column=2, row=3, padx=10)

deathLblT3 = Label(midFrameT3, text="Death rate, crude (per 1,000 people)", bg="lightgreen")
deathLblT3.grid(column=0, row=4, padx=5, pady=8, sticky="w")
deathET3 = Label(midFrameT3, width=3, text="-1", bg="white")
deathET3.grid(column=1, row=4)
deathBtnT3 = Button(midFrameT3, text="Graph")
deathBtnT3.grid(column=2, row=4, padx=10)

netLblT3 = Label(midFrameT3, text="Individuals using the Internet (% of population)", bg="lightgreen")
netLblT3.grid(column=0, row=5, padx=5, pady=8, sticky="w")
netET3 = Label(midFrameT3, width=3, text="-1", bg="white")
netET3.grid(column=1, row=5)
netBtnT3 = Button(midFrameT3, text="Graph")
netBtnT3.grid(column=2, row=5, padx=10)

indLblT3 = Label(midFrameT3, text="Industry (including construction), value added (% of GDP)", bg="lightgreen")
indLblT3.grid(column=0, row=6, padx=5, pady=8, sticky="w")
indET3 = Label(midFrameT3, width=3, text="-1", bg="white")
indET3.grid(column=1, row=6)
indBtnT3 = Button(midFrameT3, text="Graph")
indBtnT3.grid(column=2, row=6, padx=10)

litLblT3 = Label(midFrameT3, text="Literacy rate, adult total (% of people ages 15 and above)", bg="lightgreen")
litLblT3.grid(column=0, row=7, padx=5, pady=8, sticky="w")
litET3 = Label(midFrameT3, width=3, text="-1", bg="white")
litET3.grid(column=1, row=7)
litBtnT3 = Button(midFrameT3, text="Graph")
litBtnT3.grid(column=2, row=7, padx=10)

mobLblT3 = Label(midFrameT3, text="Mobile cellular subscriptions (per 100 people)", bg="lightgreen")
mobLblT3.grid(column=0, row=8, padx=5, pady=8, sticky="w")
mobET3 = Label(midFrameT3, width=3, text="-1", bg="white")
mobET3.grid(column=1, row=8)
mobBtnT3 = Button(midFrameT3, text="Graph")
mobBtnT3.grid(column=2, row=8, padx=10)

valBtnT3 = Button(midFrameT3, width="40",text="Generate Values")
valBtnT3.grid(column=0, row=9, padx=5, pady=30, sticky="w")

morLblT3 = Label(midFrameT3, text="Mortality rate, infant (per 1,000 live births)", bg="lightgreen")
morLblT3.grid(column=3, row=1, padx=10, pady=8, sticky="w")
morET3 = Label(midFrameT3, width=3, text="-1", bg="white")
morET3.grid(column=4, row=1)
morBtnT3 = Button(midFrameT3, text="Graph")
morBtnT3.grid(column=5, row=1, padx=10)

migLblT3 = Label(midFrameT3, text="Net Migration", bg="lightgreen")
migLblT3.grid(column=3, row=2, padx=10, pady=8, sticky="w")
migET3 = Label(midFrameT3, width=3, text="-1", bg="white")
migET3.grid(column=4, row=2)
migBtnT3 = Button(midFrameT3, text="Graph")
migBtnT3.grid(column=5, row=2, padx=10)

cropLblT3 = Label(midFrameT3, text="Permanent cropland (% of land area)", bg="lightgreen")
cropLblT3.grid(column=3, row=3, padx=10, pady=8, sticky="w")
cropET3 = Label(midFrameT3, width=3, text="-1", bg="white")
cropET3.grid(column=4, row=3)
cropBtnT3 = Button(midFrameT3, text="Graph")
cropBtnT3.grid(column=5, row=3, padx=10)

denLblT3 = Label(midFrameT3, text="Population density (people per sq. km of land area)", bg="lightgreen")
denLblT3.grid(column=3, row=4, padx=10, pady=8, sticky="w")
denET3 = Label(midFrameT3, width=3, text="-1", bg="white")
denET3.grid(column=4, row=4)
denBtnT3 = Button(midFrameT3, text="Graph")
denBtnT3.grid(column=5, row=4, padx=10)

popLblT3 = Label(midFrameT3, text="Population, total", bg="lightgreen")
popLblT3.grid(column=3, row=5, padx=10, pady=8, sticky="w")
popET3 = Label(midFrameT3, width=3, text="-1", bg="white")
popET3.grid(column=4, row=5)
popBtnT3 = Button(midFrameT3, text="Graph")
popBtnT3.grid(column=5, row=5, padx=10)

svcLblT3 = Label(midFrameT3, text="Services, value added (% of GDP)", bg="lightgreen")
svcLblT3.grid(column=3, row=6, padx=10, pady=8, sticky="w")
svcET3 = Label(midFrameT3, width=3, text="-1", bg="white")
svcET3.grid(column=4, row=6)
svcBtnT3 = Button(midFrameT3, text="Graph")
svcBtnT3.grid(column=5, row=6, padx=10)

surLblT3 = Label(midFrameT3, text="Surface area (sq. km)", bg="lightgreen")
surLblT3.grid(column=3, row=7, padx=10, pady=8, sticky="w")
surET3 = Label(midFrameT3, width=3, text="-1", bg="white")
surET3.grid(column=4, row=7)
surBtnT3 = Button(midFrameT3, text="Graph")
surBtnT3.grid(column=5, row=7, padx=10)

# tab3 bottom frame elements
recessionBtnT3 = Button(botFrameT3, text="Display Top 3 GDP Factors", width=30)
recessionBtnT3.grid(column=0, row=0, padx=85, pady=35)

pandemicBtnT3 = Button(botFrameT3, text="Display Bottom 3 GDP Factors", width=30)
pandemicBtnT3.grid(column=1, row=0, padx=85, pady=35)

# Apply elements to frames
topFrameT1.grid_propagate(0)
midFrameT1.grid_propagate(0)
botFrameT1.grid_propagate(0)
topFrameT2.grid_propagate(0)
midFrameT2.grid_propagate(0)
botFrameT2.grid_propagate(0)
topFrameT3.grid_propagate(0)
midFrameT3.grid_propagate(0)
botFrameT3.grid_propagate(0)

# Size window and disable resize
window.geometry("800x700")
window.resizable(0, 0)

# Run window
window.mainloop()
