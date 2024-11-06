from tkinter import *


window = Tk()
width = window.winfo_screenwidth()
heigth = window.winfo_screenheight()
window.geometry('%dx%d' %(width,heigth))
window.title('Royal Bank Of Vellore')
logo_pi = PhotoImage(file='RBV_logo.png')

label_filler = Label(window,text='                                                                                    ')
label_filler.grid(row=0,column=1000)

label_heading = Label(window,text='Royal Bank Of Vellore',bg='#00FF00',fg='Red',font=('Ariel',30,'bold'))
label_heading.grid(row=0,column=1600)



label_online_id = Label(window,text='OnlineID',bg='red')
label_online_id.grid(row=1,column=0)

entry_online_id = Entry(window,text='Enter online ID')
entry_online_id.grid(row=1,column=1)

label_password = Label(window,text='Password')
label_password.grid(row=2,column=0)
window.mainloop()
