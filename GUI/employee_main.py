import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from Py.Rbov import Rbov_class


def submit_clicked():
    entry_userid_var_val = entry_userid_var.get()
    entry_password_var_val = entry_password_var.get()
    obj1 = Rbov_class(entry_userid_var_val,entry_password_var_val)
    if obj1.is_present():
        window.destroy()
        overview_window = tk.Tk()
        overview_window.mainloop()
        obj1.get_all_accounts(entry_userid_var_val)
    else:
        tkinter.messagebox.showinfo(title='Error',message='ID not found')
# Main window creation
window = tk.Tk()

# ----------------------------------------Main window settings starts---------------------------------------------------
window.title('VIGNESH AGRICULTURALS')
window.iconbitmap('window_icon.ico')
window.minsize(width=600,height=400)
window.bind('<Escape>',lambda event: window.quit())
# ----------------------------------------Main window settings ends-----------------------------------------------------
main_frame = ttk.Frame(master=window)
frame_userid = ttk.Frame(master=main_frame)
label_userid = ttk.Label(master=frame_userid,text='User ID :',background='red')
entry_userid_var = tk.StringVar()
entry_userid = ttk.Entry(master=frame_userid,textvariable=entry_userid_var)

frame_password = ttk.Frame(master=main_frame)
label_password = ttk.Label(master=frame_password,text='Password:',background='yellow')
entry_password_var = tk.StringVar()
entry_password = ttk.Entry(master=frame_password,textvariable=entry_password_var)

button_submit = ttk.Button(master=main_frame,text='Submit',command=submit_clicked)

label_message_var = tk.StringVar()
label_message = ttk.Label(master=main_frame,text='message',textvariable=label_message_var,foreground='red')


label_userid.pack(side='left',expand=True,fill='both')
entry_userid.pack(side='left',expand=True,padx=10)
frame_userid.pack(padx=10,pady=10)

label_password.pack(side='left',expand=True,fill='both')
entry_password.pack(side='left',expand=True,padx=10)
frame_password.pack(padx=10,pady=10)

button_submit.pack(padx=10,pady=10)
label_message.pack(padx=10,pady=10)

window.columnconfigure((0,1,2),weight=1)
window.rowconfigure((0,1,2),weight=1)
main_frame.grid(row=1,column=1,sticky='ns')

window.mainloop()