import tkinter as tk
from tkinter import ttk, PhotoImage
from hospital import *

window = tk.Tk()
window.title('CARE HOSPITAL')
#window.geometry('300x300+300+100')
window.minsize(width=600,height=400)
window.maxsize(width=600,height=400)
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

def open_specific_portal(user):
    specific_portal = tk.Toplevel()
    specific_portal.grab_set()
    specific_portal.minsize(width=300, height=300)
    #specific_portal.geometry('300x300+300+300')
    specific_portal.rowconfigure(0,weight=1)
    specific_portal.columnconfigure(0,weight=1)
    specific_portal_frame = ttk.Frame(master=specific_portal,borderwidth=20)
    specific_portal_frame.rowconfigure((0,1,2,3,4),weight=1)
    specific_portal_frame.columnconfigure((0,1,2),weight=1)
    if user == 'P':
        label_patient_heading = ttk.Label(master=specific_portal_frame,text='PATIENT PORTAL LOGIN',background='red',font='Ariel,40,bold')
        label_patient_heading.grid(row=0,column=0,columnspan=3,pady=10)
        global rbutton_select_str
        rbutton_select_str = tk.StringVar()
        rbutton_select1 = ttk.Radiobutton(master=specific_portal_frame,text='First time user?',variable=rbutton_select_str,value='new',command=new_patient_selected)
        rbutton_select1.grid(row=1,column=0)
        #rbutton_select_str = tk.StringVar()
        rbutton_select2 = ttk.Radiobutton(master=specific_portal_frame,text='Existing user?',variable=rbutton_select_str,value='existing',command=exist_patient_selected)
        rbutton_select2.grid(row=1,column=2)
        global entry_id_str
        entry_id_str = tk.StringVar(value='Enter patient ID')
        global entry_id
        entry_id = tk.Entry(master=specific_portal_frame,textvariable=entry_id_str,state='disabled')
        entry_id.grid(row=2,column=0,columnspan=3,sticky='ew')
        entry_pwd_str = tk.StringVar(value='Enter your password')
        global entry_pwd
        entry_pwd = tk.Entry(master=specific_portal_frame,textvariable=entry_pwd_str,show='*',state='disabled')
        entry_pwd.grid(row=3,column=0,columnspan=3,sticky='ew')
        global button_submit
        button_submit = ttk.Button(master=specific_portal_frame,text='SUBMIT',state='disabled',command=show_patient_det)
        button_submit.grid(row=4,column=0,columnspan=3,)
    elif user == 'D':
        pass
    else:
        pass
    specific_portal_frame.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
def exist_patient_selected():
    if rbutton_select_str.get() == 'existing':
        entry_id.configure(state='normal')
        entry_pwd.configure(state='normal')
        button_submit.configure(state='enabled')
def new_patient_selected():
    pass
def show_patient_det():
    print(entry_id_str.get())
    PortalUser(user='P', id=entry_id_str.get(), name=None, dob=None, gender=None,email=None,phone_no=None,address=None).get_portal_user_info(user='P',user_id=entry_id.get())

window.mainloop()
