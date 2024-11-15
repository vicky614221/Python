import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('My App')
window.geometry('400x200+0+0')
window.iconbitmap('window_icon.ico')
window.minsize(width=200,height=600)
window.bind('<Escape>', lambda event: window.quit())

frame1 = ttk.Frame(master=window)
label1 = ttk.Label(master=frame1,text='First Label',background='red')
label2 = ttk.Label(master=frame1,text='Label 2',background='blue')

label3 = ttk.Label(master=window,text='Another label',background='green')

frame2 = ttk.Frame(master=window)
label4 = ttk.Label(master=frame2,text='Last of labels',background='orange')
button1 = ttk.Button(master=frame2,text='A Button')
button2 = ttk.Button(master=frame2,text='Another Button')

frame3 = ttk.Frame(master=window)
button3 = ttk.Button(master=frame3,text='Button3')
button4 = ttk.Button(master=frame3,text='Button4')
button5 = ttk.Button(master=frame3,text='Button5')

label1.pack(side='top',expand=True,fill='both')
label2.pack(side='top',expand=True,fill='both')
frame1.pack(side='top',expand=True,fill='both')
label3.pack(side='top',expand=True)

button1.pack(side='left',expand=True,fill='both')
label4.pack(side='left',expand=True,fill='both')
button2.pack(side='left',expand=True,fill='both')
frame2.pack(side='left',expand=True,fill='both',padx=5,pady=5)

button3.pack(side='top',expand=True,fill='both')
button4.pack(side='top',expand=True,fill='both')
button5.pack(side='top',expand=True,fill='both')
frame3.pack(side='top',expand=True,fill='both',padx=5,pady=5)




window.mainloop()