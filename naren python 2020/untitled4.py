from tkinter import *
root = Tk()
root.title("Drop-down boxes for option selections.")

var = StringVar(screen99)
var.set("drop down menu button")



drop_menu = OptionMenu(screen99, var,  "one", "two", "three", "four", "meerkat", "12345", "6789", command=grab_and_assign)
drop_menu.grid(row=0, column=0)

label_left=Label(root, text="chosen variable= ")
label_left.grid(row=1, column=0) 


def grab_and_assign(event):
    chosen_option = var.get() 
    label_chosen_variable= Label(root, text=chosen_option)
    label_chosen_variable.grid(row=1, column=2)
    print(chosen_option)


root.mainloop()