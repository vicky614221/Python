import tkinter as tk
from tkinter import ttk, PhotoImage

def open_specific_portal(user):
    specific_portal = tk.Toplevel()
    specific_portal.grab_set()
    specific_portal.minsize(width=300, height=300)
    specific_portal.geometry('300x300+300+100')
    specific_portal.rowconfigure(0,weight=1)
    specific_portal.columnconfigure(0,weight=1)
    specific_portal_frame = ttk.Frame(master=specific_portal,borderwidth=20)
    specific_portal_frame.rowconfigure((0),weight=5)
    specific_portal_frame.rowconfigure((1,2,3,4),weight=1)
    specific_portal_frame.columnconfigure((0),weight=1)
    if user == 'P':
        label_patient_heading = ttk.Label(master=specific_portal_frame,text='PATIENT PORTAL LOGIN',background='red',font='Ariel,40,bold')
        label_patient_heading.grid(row=0,column=0,columnspan=3,pady=10)
        entry_id_str = tk.StringVar(value="Enter patient ID")
        entry_id = ttk.Entry(master=specific_portal_frame,textvariable=entry_id_str)
        entry_id.grid(row=1,column=0)
        entry_pwd_str = tk.StringVar(value='Enter your password')
        entry_pwd = ttk.Entry(master=specific_portal_frame,textvariable=entry_pwd_str,show='*')
        entry_pwd.grid(row=3,column=0)
    elif user == 'D':
        pass
    else:
        pass
    specific_portal_frame.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
window = tk.Tk()
window.title('CARE HOSPITAL')
window.minsize(width=600,height=400)
window.geometry('300x300+300+100')
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)

window_frame = ttk.Frame(master=window)
window_frame.rowconfigure(0,weight=1)
window_frame.rowconfigure(1,weight=3)
window_frame.columnconfigure((0,1,2),weight=1)
image = PhotoImage(file='hospital_image.png')
label_image = ttk.Label(master=window_frame,image=image)
label_image.grid(row=0,column=0,rowspan=2,columnspan=3)
label_heading = ttk.Label(master=window_frame,text='CARE HOSPITAL MAIN PORTAL',font='Ariel,40,bold',foreground='blue')
label_heading.grid(row=0,column=0,columnspan=3)
button_patient_portal = ttk.Button(master=window_frame,text="PATIENT'S PORTAL",command=lambda :open_specific_portal('P'))
button_patient_portal.grid(row=1,column=0,rowspan=3,sticky='nsew',pady=50,padx=10)
button_doctor_portal = ttk.Button(master=window_frame,text="DOCTOR'S PORTAL")
button_doctor_portal.grid(row=1,column=1,rowspan=3,sticky='nsew',pady=50,padx=10)
button_admin_portal = ttk.Button(master=window_frame,text="ADMIN'S PORTAL")
button_admin_portal.grid(row=1,column=2,rowspan=3,sticky='nsew',pady=50,padx=10)
window_frame.grid(row=0,column=0,sticky='nsew',padx=5,pady=5)


window.mainloop()