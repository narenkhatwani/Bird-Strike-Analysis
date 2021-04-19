




#function5
def function5():
    global screen69,catname2,yearnum
    app_name=StringVar()
    screen69 = Toplevel(screen) 
    screen69.title("FUNCTION 14")
    #adjustWindow(screen24) 
    screen69.geometry("490x310")
    screen.resizable(False,False)
    
    photo14 = PhotoImage(file="dark.png") # opening right side image - Note: If image is in same folder then no need to mention the full path 
    label14 = Label(screen69, image=photo14, text="") # attaching image to the label 
    label14.place(x=-12, y=-12) 
    label14.image = photo14 # it is necessary in Tkinter to keep a instance of image to display image in label 

    catname2= StringVar(screen69)
    catname2.set("drop down menu button")
    
    yearnum= StringVar(screen69)
    yearnum.set("drop down menu button")
    
    def grab_and_assign5(event):
        global chosen_option
        chosen_option1 = catname2.get() 
        label_chosen_variable= Label(screen69, text=chosen_option1)
        label_chosen_variable.pack()
    
    def grab_and_assign6(event):
        global chosen_option
        chosen_option2 = yearnum.get() 
        label_chosen_variable= Label(screen69, text=chosen_option2)
        label_chosen_variable.pack()
        
    drop_menu = OptionMenu(screen69,catname2,'ART_AND_DESIGN','AUTO_AND_VEHICLES','BEAUTY','BOOKS_AND_REFERENCE','BUSINESS','COMICS','COMMUNICATION','DATING','EDUCATION','ENTERTAINMENT','EVENTS','FINANCE','FOOD_AND_DRINK','HEALTH_AND_FITNESS','HOUSE_AND_HOME','LIBRARIES_AND_DEMO','LIFESTYLE','GAME','FAMILY','MEDICAL','SOCIAL','SHOPPING','PHOTOGRAPHY','SPORTS','TRAVEL_AND_LOCAL','TOOLS','PERSONALIZATION','PRODUCTIVITY','PARENTING','WEATHER','VIDEO_PLAYERS','NEWS_AND_MAGAZINES','MAPS_AND_NAVIGATION',command=grab_and_assign5)
    drop_menu.pack()#drop_menu.grid(row=0, column=0)
    
    drop_menu = OptionMenu(screen69,yearnum,'2011','2012','2013','2014','2015','2016','2017','2018',command=grab_and_assign6)
    drop_menu.pack()#drop_menu.grid(row=0, column=0)
    
           
    Button(screen69, text="Proceed", height="2", width="30",  bg='brown', font=("Open Sans", 10, 'bold'), fg='white', command=function5sub).place(x=120,y=220)
    
    screen69.mainloop()

def function5sub():
    global screen70,catname2,yearnum
    screen70 = Toplevel(screen) 
    screen70.title("FUNCTION 14")
    adjustWindow(screen70)
    #screen25.geometry("800x800")
    chosen_option1 = catname2.get()
    chosen_option2 = yearnum.get()
    
    plt.subplots(figsize=(6,6))
    plt.title("THE PERCENTAGE OF DOWNLOADS CATEGORY WISE")
    sns.countplot(x=data_naren['Category']==chosen_option1,label='percentage')
    plt.xticks(fontsize=6,rotation=78)
    plt.savefig('C:\\Users\\Admin\\Desktop\\internship gui\\function5.jpg',dpi=100)
    
    img = ImageTk.PhotoImage(Image.open('function5.jpg'))
    panel =Label(screen70, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    
    screen70.mainloop()

