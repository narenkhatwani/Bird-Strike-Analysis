user_path.get(), y_axis, y_axis
import pandas as pd
import seaborn as sns
import tkinter
from tkinter import ttk
window = Tk()
window.geometry("600x600")
window.title("Visual data")
label_one = ttk.Label(window, text = "Enter your filepath")
label_one.grid(row = 0, column = 0)
label_two = ttk.Label(window, text = "Your file path is")
label_two.grid(row = 1, column = 1)
user_path = tkinter.StringVar()
user_entry = ttk.Entry(window, width = 26, textvariable = user_path)
user_entry.grid(row = 0, column = 1)
y_axis = "age"
x_axis = "errors_time1"
def barplot_function(dataset, name1, name2):
    sns.set(color_codes=True)
    dataset = pd.read_csv(dataset)
    dataset.head()
    plot = sns.barplot(x=name1, y=name2, data=dataset)
    outbox.insert(plot)
def action():
    label_two.configure(text = "Your file path is " + user_path.get())
    barplot_function(user_path, y_axis, y_axis)
button1 = ttk.Button(window, text = "submit", command = action)
button1.grid(row = 0, column = 2)

outbox = Canvas(window, width = 200, height = 200, bg = "light grey")
outbox.grid(row = 3, column = 0, sticky = W)
window.mainloop()