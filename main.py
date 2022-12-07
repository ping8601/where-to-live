from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.title("Where to Live?")

ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# root.configure(bg='white')
def step1(): # rank properties, 1 of 4
    global count_res
    global climate_choice
    count_res = [0,0,0,0,0,0] # Living cost, Crime rate, Income, Living environment, Education, Health
    climate_choice = [0,0,0,0]

    root.eval('tk::PlaceWindow . center')

    status = Label(root, text="Step 1 of 5  ",bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=9,column=0,columnspan=4,sticky=W+E)

    # Step 1

    global text3
    global text4
    global text5

    text3 = StringVar()
    text4 = StringVar()
    text5 = StringVar()

    text3.set("Living Cost")
    text4.set("Safety (Crime Rate)")
    text5.set("Income")


    options1 = ["1","2","3"]
    options2 = ["1","2","3"]
    options3 = ["1","2","3"]

    Label0 = Label(root, text="                       ")
    Label0.grid(row=0, column=0,columnspan=4)

    Label1 = Label(root, text="       Please rank the following properties:       ")
    Label1.grid(row=1, column=0,columnspan=4)

    Label2 = Label(root, text="                       ")
    Label2.grid(row=2, column=0,columnspan=4)

    Label3 = Label(root, textvariable=text3)
    Label3.grid(row=3, column=0,columnspan=3)
    Label4 = Label(root, textvariable=text4)
    Label4.grid(row=4, column=0,columnspan=3)
    Label5 = Label(root, textvariable=text5)
    Label5.grid(row=5, column=0,columnspan=3)

    global clicked0
    global clicked1
    global clicked2

    clicked0 = StringVar()
    clicked1 = StringVar()
    clicked2 = StringVar()

    drop1 = OptionMenu(root, clicked0, *options1)
    drop1.grid(row=3, column=3)

    drop2 = OptionMenu(root, clicked1, *options2)
    drop2.grid(row=4, column=3)

    drop3 = OptionMenu(root, clicked2, *options3)
    drop3.grid(row=5, column=3)

    Label7 = Label(root, text="                       ")
    Label7.grid(row=6, column=0,columnspan=4)

    global button_next1
    global button_next2
    global button_next3
    global button_next4

    button_next1 = Button(root, text="Next Step",command=next1)
    button_next2 = Button(root, text="Next Step",command=next2)
    button_next3 = Button(root, text="Next Step",command=next3)
    button_next4 = Button(root, text="Next Step",command=next4)
    button_next1.grid(row=7, column=0,columnspan=4)

    Label5 = Label(root, text="                       ")
    Label5.grid(row=8, column=0,columnspan=4)

def next1(): # save values of step 1 and go to step 2
    global clicked0
    global clicked1
    global clicked2
    global count_res
    value_set = {clicked0.get(), clicked1.get(), clicked2.get()}
    if value_set != {'1', '2', '3'}:
        Label1 = Label(root, text=" Invalid values, please check and try again. ", fg="red")
        Label1.grid(row=6, column=0,columnspan=4)
        return

    Label7 = Label(root, text="                                                                         ")
    Label7.grid(row=6, column=0,columnspan=4)
    text3.set("Living Environment")
    text4.set("Education")
    text5.set("Health")
    count_res[0] += (3-int(clicked0.get()))*0.5
    count_res[1] += (3-int(clicked1.get()))*0.5
    count_res[2] += (3-int(clicked2.get()))*0.5
    print(count_res)
    clicked0.set("")
    clicked1.set("")
    clicked2.set("")
    status = Label(root, text="Step 2 of 5  ",bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=9,column=0,columnspan=4,sticky=W+E)
    step2()

def next2(): # save values of step 2 and go to step 3
    global clicked0
    global clicked1
    global clicked2
    global count_res

    value_set = {clicked0.get(), clicked1.get(), clicked2.get()}
    if value_set != {'1', '2', '3'}:
        Label1 = Label(root, text=" Invalid values, please check and try again. ", fg="red")
        Label1.grid(row=6, column=0,columnspan=4)
        return

    Label7 = Label(root, text="                                                                         ")
    Label7.grid(row=6, column=0,columnspan=4)

    text3.set("Living Cost")
    text4.set("Income")
    text5.set("Health")

    count_res[3] += (3-int(clicked0.get()))*0.5
    count_res[4] += (3-int(clicked1.get()))*0.5
    count_res[5] += (3-int(clicked2.get()))*0.5
    print(count_res)
    clicked0.set("")
    clicked1.set("")
    clicked2.set("")
    status = Label(root, text="Step 3 of 5  ",bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=9,column=0,columnspan=4,sticky=W+E)
    step3()

def next3(): # save values of step 3 and go to step 4
    global clicked0
    global clicked1
    global clicked2
    global count_res
    value_set = {clicked0.get(), clicked1.get(), clicked2.get()}
    if value_set != {'1', '2', '3'}:
        Label1 = Label(root, text=" Invalid values, please check and try again. ", fg="red")
        Label1.grid(row=6, column=0,columnspan=4)
        return

    Label7 = Label(root, text="                                                                         ")
    Label7.grid(row=6, column=0,columnspan=4)
    text3.set("Safety (Crime Rate)")
    text4.set("Living Environment")
    text5.set("Education")
    count_res[0] += (3-int(clicked0.get()))*0.5
    count_res[2] += (3-int(clicked1.get()))*0.5
    count_res[5] += (3-int(clicked2.get()))*0.5
    print(count_res)
    clicked0.set("")
    clicked1.set("")
    clicked2.set("")
    status = Label(root, text="Step 4 of 5  ",bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=9,column=0,columnspan=4,sticky=W+E)
    step4()

def next4(): # save values of step 4 and go to step 5
    global clicked0
    global clicked1
    global clicked2
    global count_res

    value_set = {clicked0.get(), clicked1.get(), clicked2.get()}
    if value_set != {'1', '2', '3'}:
        Label1 = Label(root, text=" Invalid values, please check and try again. ", fg="red")
        Label1.grid(row=6, column=0,columnspan=4)
        return

    Label7 = Label(root, text="                                                                         ")
    Label7.grid(row=6, column=0,columnspan=4)
    count_res[1] += (3-int(clicked0.get()))*0.5
    count_res[3] += (3-int(clicked1.get()))*0.5
    count_res[4] += (3-int(clicked2.get()))*0.5
    print(count_res)
    status = Label(root, text="Step 5 of 5  ",bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=9,column=0,columnspan=4,sticky=W+E)
    step5()

def next5(): # save values of step 5 and go to step 6 (result page)
    global climate_choice
    climate_choice[0]=summer_tmp.get()
    climate_choice[1]=summer_prcp.get()
    climate_choice[2]=winter_tmp.get()
    climate_choice[3]=winter_prcp.get()
    print("climate_choice is:")
    print(climate_choice)
    step6()

def step2(): # rank properties, 2 of 4
    button_next1.grid_forget
    button_next2.grid(row=7, column=0,columnspan=4)

def step3(): # rank properties, 3 of 4
    button_next2.grid_forget
    button_next3.grid(row=7, column=0,columnspan=4)

def step4(): # rank properties, 1 of 4
    button_next3.grid_forget
    button_next4.grid(row=7, column=0,columnspan=4)

def step5(): # select climate type
    button_next2.grid_forget
    button_next3.grid(row=7, column=0,columnspan=4)
    for widget in root.winfo_children():
        widget.destroy()

    Label0 = Label(root, text="                       ")
    Label0.grid(row=0, column=0,columnspan=4)

    Label1 = Label(root, text="       Please select your preferred climate type:       ")
    Label1.grid(row=1, column=0,columnspan=4)

    Label2 = Label(root, text="                       ")
    Label2.grid(row=2, column=0,columnspan=4)

    status = Label(root, text="Step 5 of 5  ",bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=9,column=0,columnspan=4,sticky=W+E)
    # Drop Down Boxes

    global summer_tmp
    global summer_prcp
    global winter_tmp
    global winter_prcp

    summer_tmp = IntVar()
    summer_tmp.set(0)

    Label3 = Label(root, text="  Summer Temperature: ")
    Label3.grid(row=3, column=0)

    Radiobutton(root, text="Hot", variable= summer_tmp, value = 0).grid(row=3, column=1)
    Radiobutton(root, text="Cool", variable= summer_tmp, value = 1).grid(row=3, column=2)

    summer_prcp = IntVar()
    summer_prcp.set(1)

    Label4 = Label(root, text="  Summer Precipitation: ")
    Label4.grid(row=4, column=0)
    Radiobutton(root, text="Rainy", variable= summer_prcp, value = 1).grid(row=4, column=1)
    Radiobutton(root, text="Dry", variable= summer_prcp, value = 0).grid(row=4, column=2)

    winter_tmp = IntVar()
    winter_tmp.set(0)

    Label5 = Label(root, text="  Winter Temperature: ")
    Label5.grid(row=5, column=0)

    Radiobutton(root, text="Warm", variable= winter_tmp, value = 0).grid(row=5, column=1)
    Radiobutton(root, text="Cold", variable= winter_tmp, value = 1).grid(row=5, column=2)

    winter_prcp = IntVar()
    winter_prcp.set(1)

    Label6 = Label(root, text="  Winter Precipitation: ")
    Label6.grid(row=6, column=0)

    Radiobutton(root, text="Wet", variable= winter_prcp, value = 1).grid(row=6, column=1)
    Radiobutton(root, text="Dry", variable= winter_prcp, value = 0).grid(row=6, column=2)

    button_next5 = Button(root, text="View Result",command=next5)
    button_next5.grid(row=7, column=0,columnspan=4)

    Label7 = Label(root, text="                       ")
    Label7.grid(row=8, column=0,columnspan=4)

def step6(): # show the result and detail data
    # calculate the rank
    df = pd.read_csv('generate_csv/all_rank_normal.csv')
    df_climate = pd.read_csv('climate/climate_classification.csv')
    df['result'] = df.apply(lambda row: row.Expense_ranking*count_res[0]+row.Education_ranking*count_res[4]+row.GreenSpace_ranking*count_res[3]+row.Crime_ranking*count_res[1]+row.HealthFund_ranking*count_res[5]+row.Incomes_ranking*count_res[2], axis=1)
    print(df.sort_values(by=['result'],ascending = False))
    df_res = df.sort_values(by=['result'],ascending = False)

    us_state_to_abbrev = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "District of Columbia": "DC",
        "American Samoa": "AS",
        "Guam": "GU",
        "Northern Mariana Islands": "MP",
        "Puerto Rico": "PR",
        "United States Minor Outlying Islands": "UM",
        "U.S. Virgin Islands": "VI",
    }
    global abbr
    global final_res
    final_res = ''
    for i in range(50):
        abbr = us_state_to_abbrev[df_res.iloc[i,0]]
        climate_list = df_climate[df_climate['State Name'].str.contains(abbr)].values.flatten().tolist()
        print(climate_list)
        print(climate_choice)
        if climate_list[1:] == climate_choice:
            final_res = str(df_res.iloc[i,0])
            break
    
    if final_res == '':
        for i in range(50):
            abbr = us_state_to_abbrev[df_res.iloc[i,0]]
            climate_list = df_climate[df_climate['State Name'].str.contains(abbr)].values.flatten().tolist()
            print(climate_list)
            print(climate_choice)
            if climate_list[2:] == climate_choice[1:]:
                final_res = str(df_res.iloc[i,0])
                break

    print("final result is: "+ final_res)

    final_res_var = StringVar()
    final_res_var.set(final_res)

    for widget in root.winfo_children():
        widget.destroy()

    status = Label(root, text="Result   ",bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=14,column=0,columnspan=4,sticky=W+E)

    Label0 = Label(root, text="                       ")
    Label0.grid(row=0, column=0,columnspan=4)

    Label1 = Label(root, text="       The most suitable state for you to live is:       ")
    Label1.grid(row=1, column=0,columnspan=4)

    Label2 = Label(root, text="                       ")
    Label2.grid(row=2, column=0,columnspan=4)

    Label3 = Label(root, textvariable=final_res_var)
    Label3.grid(row=3, column=0,columnspan=4)

    Label4 = Label(root, text="                       ")
    Label4.grid(row=4, column=0,columnspan=4)

    df_data = pd.read_csv('generate_csv/all_data.csv')

    data_list = df_data[df_data.iloc[:,0]==final_res].values.flatten().tolist()
    print(data_list)

    cost = StringVar()
    cost.set("Average Living Cost: "+ str(data_list[1]) +"$ / Year")

    edu = StringVar()
    edu.set("Higher Education Rate: "+ str(data_list[2]) +"%")

    crime = StringVar()
    crime.set("Crime Rate: "+ str(data_list[3]) +" cases / 10000 people")

    health = StringVar()
    health.set("Public Health Funding: "+ str(data_list[4]) +"$ / Capita")

    income = StringVar()
    income.set("Average Income: "+ str(data_list[5]) +"$ / Year")


        
    Label5 = Label(root, textvariable=cost)
    Label5.grid(row=5, column=0,columnspan=4)
    Label6 = Label(root, textvariable=edu)
    Label6.grid(row=6, column=0,columnspan=4)
    Label7 = Label(root, textvariable=crime)
    Label7.grid(row=7, column=0,columnspan=4)
    Label8 = Label(root, textvariable=health)
    Label8.grid(row=8, column=0,columnspan=4)
    Label9 = Label(root, textvariable=income)
    Label9.grid(row=9, column=0,columnspan=4)

    Label11 = Label(root, text="                       ")
    Label11.grid(row=11, column=0,columnspan=4)


    button_next6 = Button(root, text="Click to View Climate Data",command=step7)
    button_next6.grid(row=12, column=0,columnspan=4)

    Label12 = Label(root, text="                       ")
    Label12.grid(row=13, column=0,columnspan=4)

def restart():
    for widget in root.winfo_children():
        widget.destroy()
    step1()


def step7(): # show the climate plots
    for widget in root.winfo_children():
        widget.destroy()

    df_prcp = pd.read_csv('climate/cleaned/state_prcp.csv')
    print(df_prcp[df_prcp['State Name'].str.contains(abbr)].iloc[:,1:].transpose())
    ax1 = df_prcp[df_prcp['State Name'].str.contains(abbr)].iloc[:,1:].transpose().plot() 
    fig1 = ax1.get_figure()
    xlabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax1.set_xticks(range(12))
    ax1.set_xticklabels(xlabels)
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Precipitation (hundredths of inches)')
    ax1.get_legend().remove()
    fig1.savefig('prcp.png')
    plt.close()

    df_max = pd.read_csv('climate/cleaned/state_tmax.csv')
    df_max_temp = df_max[df_max['State Name'].str.contains(abbr)].iloc[:,1:]
    df_max_temp = df_max_temp.rename(index={df_max_temp.index[0]: 'max average temperature'})
    df_min = pd.read_csv('climate/cleaned/state_tmin.csv')
    df_min_temp = df_min[df_min['State Name'].str.contains(abbr)].iloc[:,1:]
    df_min_temp = df_min_temp.rename(index={df_min_temp.index[0]: 'min average temperature'})
    df_res_temp = df_max_temp.append(df_min_temp)
    ax2 = df_res_temp.transpose().plot()
    fig2 = ax2.get_figure()
    xlabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax2.set_xticks(range(12))
    ax2.set_xticklabels(xlabels)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Temperature (Degree Celsius)')
    fig2.savefig('temp.png')
    plt.close()

    final_res_var_plus = StringVar()
    final_res_var_plus.set("Climate Data of " + final_res)

    Label0 = Label(root, textvariable=final_res_var_plus)
    Label0.grid(row=0, column=0,columnspan=2)

    image1 = ImageTk.PhotoImage(Image.open("temp.png").resize((400,300)))
    image2 = ImageTk.PhotoImage(Image.open("prcp.png").resize((400,300)))
    Label1 = Label(image=image1)
    Label1.image = image1
    Label1.grid(row=1, column=0)
    Label2 = Label(image=image2)
    Label2.image = image2
    Label2.grid(row=1, column=1)

    Label3 = Label(root, text="Temperature by Month")
    Label3.grid(row=2, column=0)
    Label4 = Label(root, text="Precipitation by Month")
    Label4.grid(row=2, column=1)

    Label0 = Label(root, text="                       ")
    Label0.grid(row=3, column=0,columnspan=2)

    button_exit = Button(root, text="Restart", command=restart)
    button_exit.grid(row=4, column=0)

    button_exit = Button(root, text="Exit", command=root.destroy)
    button_exit.grid(row=4, column=1)

    Label0 = Label(root, text="                       ")
    Label0.grid(row=5, column=0,columnspan=2)

step1()
root.mainloop()