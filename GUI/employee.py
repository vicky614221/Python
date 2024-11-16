import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Employee portal')
screen_width = int(window.winfo_screenwidth()/2)-300
screen_height = int(window.winfo_screenheight()/2)-350
window.geometry(('600x700+%d+%d'%(screen_width,screen_height)))
window.minsize(width=600,height=700)
window.maxsize(width=600,height=700)
window.bind('<Escape>',lambda event: window.quit())
window.iconbitmap('window_icon.ico')

style = ttk.Style()
style.configure("frame_choice.TFrame",foreground="green", relief="raised", borderwidth=5)
style.configure("")

frame_choice = ttk.Frame(master=window,style="frame_choice.TFrame")
label_emp_enquiry = ttk.Label(master=frame_choice,text='ENQUIRE EMPLOYEE',foreground='green')
entry_emp_enquiry_int = tk.IntVar(value=None)
entry_emp_enquiry = ttk.Entry(master=frame_choice,textvariable=entry_emp_enquiry_int)
button_emp_enquiry = ttk.Button(master = frame_choice,text='Click here')
label_emp_update = ttk.Label(master=frame_choice,text='UPDATE EMPLOYEE DETAILS',foreground='orange')
entry_emp_update_int = tk.IntVar(value=None)
entry_emp_update = ttk.Entry(master=frame_choice,textvariable=entry_emp_update_int)
button_emp_update = ttk.Button(master = frame_choice,text='Click here')
label_emp_add = ttk.Label(master=frame_choice,text='ADD NEW EMPLOYEE',foreground='blue')
button_emp_add = ttk.Button(master = frame_choice,text='Click here')

window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=10)

frame_choice.columnconfigure((0,1,2),weight=1)
frame_choice.rowconfigure((0,1,2),weight=1)

label_emp_enquiry.grid(row=0,column=0,padx=20,pady=10)
entry_emp_enquiry.grid(row=1,column=0,padx=5,pady=5)
button_emp_enquiry.grid(row=2,column=0,padx=5,pady=5)

label_emp_update.grid(row=0,column=1,padx=20,pady=10)
entry_emp_update.grid(row=1,column=1,padx=5,pady=5)
button_emp_update.grid(row=2,column=1,padx=5,pady=5)

label_emp_add.grid(row=0,column=2,padx=20,pady=10)
button_emp_add.grid(row=2,column=2,padx=5,pady=5)

frame_choice.grid(row=0,column=0)

window.mainloop()