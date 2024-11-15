import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('My App')
window.geometry('600x400+0+0')
window.iconbitmap('window_icon.ico')
button1_var = tk.StringVar()

button1 = ttk.Button(master=window,text='click here',textvariable=button1_var)
button1.pack()
window.mainloop()