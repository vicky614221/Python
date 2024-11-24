import tkinter as tk
import tkinter.messagebox
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
    global window_specific_portal
    window_specific_portal = tk.Toplevel()
    window_specific_portal.grab_set()
    window_specific_portal.minsize(width=300, height=300)
    #specific_portal.geometry('300x300+300+300')
    window_specific_portal.rowconfigure(0, weight=1)
    window_specific_portal.columnconfigure(0, weight=1)
    global frame_specific_portal
    frame_specific_portal = ttk.Frame(master=window_specific_portal)
    #frame_specific_portal_frame = ttk.Frame(master=specific_portal,borderwidth=20)
    frame_specific_portal.rowconfigure((0,1,2,3,4),weight=1)
    frame_specific_portal.columnconfigure((0,1,2),weight=1)
    if user == 'P':
        label_patient_heading = ttk.Label(master=frame_specific_portal,text='PATIENT PORTAL LOGIN',background='red',font='Ariel,40,bold')
        label_patient_heading.grid(row=0,column=0,columnspan=3,pady=10)
        global rbutton_select_str
        rbutton_select_str = tk.StringVar()
        rbutton_select1 = ttk.Radiobutton(master=frame_specific_portal,text='First time user?',variable=rbutton_select_str,value='new',command=new_patient_selected)
        rbutton_select1.grid(row=1,column=0)
        #rbutton_select_str = tk.StringVar()
        rbutton_select2 = ttk.Radiobutton(master=frame_specific_portal,text='Existing user?',variable=rbutton_select_str,value='existing',command=exist_patient_selected)
        rbutton_select2.grid(row=1,column=2)
        global entry_id_str
        entry_id_str = tk.StringVar(value='Enter patient ID')
        global entry_id
        entry_id = tk.Entry(master=frame_specific_portal,textvariable=entry_id_str,state='disabled')
        entry_id.grid(row=2,column=0,columnspan=3,sticky='ew')
        global entry_pwd_str
        entry_pwd_str = tk.StringVar(value='Enter your password')
        global entry_pwd
        entry_pwd = tk.Entry(master=frame_specific_portal,textvariable=entry_pwd_str,show='*',state='disabled')
        entry_pwd.grid(row=3,column=0,columnspan=3,sticky='ew')
        global button_submit
        button_submit = ttk.Button(master=frame_specific_portal,text='SUBMIT',state='disabled',command=lambda :validate_and_show(user))
        button_submit.grid(row=4,column=0,columnspan=3,)
    elif user == 'D':
        pass
    else:
        pass
    frame_specific_portal.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
def exist_patient_selected():
    if rbutton_select_str.get() == 'existing':
        entry_id.configure(state='normal')
        entry_pwd.configure(state='normal')
        button_submit.configure(state='enabled')
def new_patient_selected():
    if rbutton_select_str.get() == 'new':
        entry_id.configure(state='disabled')
        entry_pwd.configure(state='disabled')
        button_submit.configure(state='disabled')
        global window_np
        window_np = tk.Toplevel(master=window_specific_portal)
        window_np.grab_set()
        window_np.minsize(width=300,height=300)
        window_np.title('New Patient Registration')
        window_np.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
        window_np.columnconfigure((0,1),weight=1)
        label_p_name = ttk.Label(master=window_np,text='Patient Full Name: ')
        label_p_name.grid(row=0,column=0,sticky='ew',padx=5)
        global entry_p_name_str
        entry_p_name_str = tk.StringVar()
        entry_p_name = ttk.Entry(master=window_np,textvariable=entry_p_name_str)
        entry_p_name.grid(row=0,column=1,sticky='ew',padx=5)

        label_p_dob = ttk.Label(master=window_np, text='Patient D.O.B(YYYY/MM/DD): ')
        label_p_dob.grid(row=1, column=0,sticky='ew',padx=5)
        global entry_p_dob_str
        entry_p_dob_str = tk.StringVar()
        entry_p_dob = ttk.Entry(master=window_np, textvariable=entry_p_dob_str)
        entry_p_dob.grid(row=1, column=1,sticky='ew',padx=5)

        label_p_gen = ttk.Label(master=window_np, text='Patient Gender: ')
        label_p_gen.grid(row=2, column=0,sticky='ew',padx=5)
        global combo_p_gen_str
        combo_p_gen_str = tk.StringVar()
        gen_list = ['MALE','FEMALE']
        combo_p_gen = ttk.Combobox(master=window_np, textvariable=combo_p_gen_str)
        combo_p_gen.configure(values=gen_list)
        combo_p_gen.grid(row=2, column=1,sticky='ew',padx=5)

        label_p_email = ttk.Label(master=window_np, text='Patient Email ID: ')
        label_p_email.grid(row=3, column=0, sticky='ew', padx=5)
        global entry_p_email_str
        entry_p_email_str = tk.StringVar()
        entry_p_email = ttk.Entry(master=window_np, textvariable=entry_p_email_str)
        entry_p_email.grid(row=3, column=1, sticky='ew', padx=5)

        label_p_phone = ttk.Label(master=window_np, text='Patient Phone No.: ')
        label_p_phone.grid(row=4, column=0, sticky='ew', padx=5)
        global entry_p_phone_str
        entry_p_phone_str = tk.StringVar()
        entry_p_phone = ttk.Entry(master=window_np, textvariable=entry_p_phone_str)
        entry_p_phone.grid(row=4, column=1, sticky='ew', padx=5)

        label_p_adhar = ttk.Label(master=window_np, text='Patient Aadhar No.: ')
        label_p_adhar.grid(row=5, column=0, sticky='ew', padx=5)
        global entry_p_adhar_str
        entry_p_adhar_str = tk.StringVar()
        entry_p_adhar = ttk.Entry(master=window_np, textvariable=entry_p_adhar_str)
        entry_p_adhar.grid(row=5, column=1, sticky='ew', padx=5)

        label_p_addr = ttk.Label(master=window_np, text='Patient Address: ')
        label_p_addr.grid(row=6, column=0, sticky='ew', padx=5)
        global entry_p_addr_str
        entry_p_addr_str = tk.StringVar()
        entry_p_addr = ttk.Entry(master=window_np, textvariable=entry_p_addr_str)
        entry_p_addr.grid(row=6, column=1, sticky='ew', padx=5)

        button_submit_patient = ttk.Button(master=window_np,
                                           text='SUBMIT',
                                           command=add_patient)
        button_submit_patient.grid(row=7,column=0,columnspan=2)

def add_patient():
    if PortalUser(user=None, id=None, name=None, dob=None,
               gender=None, email=None, phone_no=None, aadhar=None, address=None).add_portal_user(user='P', patient_name=entry_p_name_str.get(),
                     patient_dob=entry_p_dob_str.get(),
                     patient_gen=combo_p_gen_str.get(),
                     patient_email=entry_p_email_str.get(),
                     patient_phone=entry_p_phone_str.get(),
                     patient_adhar=entry_p_adhar_str.get(),
                     patient_addr=entry_p_addr_str.get()):
        window_np.destroy()
def show_patient_det():
    print(entry_id_str.get())
    PortalUser(user='P', id=entry_id_str.get(), name=None, dob=None, gender=None,email=None,phone_no=None,address=None).get_portal_user_info(user='P',user_id=entry_id.get())

def validate_and_show(user):
    if user == 'P':
        patient_obj = PortalUser(user='P', id=entry_id_str.get(),name=None, dob=None, gender=None,email=None,phone_no=None,aadhar=None,address=None)
        if patient_obj.is_valid_user('P',entry_id_str.get(),entry_pwd_str.get()):
            patient_id,patient_name,patient_dob,patient_gen,patient_email,patient_phone,patient_aadhar,patient_addr = patient_obj.get_portal_user_info()
            #add logic to get appointment details
            frame_specific_portal.grid_forget()
            #window_show_p = tk.Toplevel()
            #window_show_p.title('Patient Options')
            #window_show_p.minsize(width=300,height=300)
            #window_show_p.grab_set()
            #window_show_p.rowconfigure((0,1,2,3),weight=1)
            #window_show_p.columnconfigure((0,1),weight=1)
            global frame_show_p
            frame_show_p = ttk.Frame(master=window_specific_portal)
            frame_show_p.columnconfigure((0,1),weight=1)
            frame_show_p.rowconfigure((0, 1, 2, 3, 4), weight=1)
            label_p_heading = ttk.Label(master=frame_show_p,text=('Hello '+ patient_name.upper()),font=('Times New Roman', 15, 'bold'),foreground='blue')
            label_p_heading.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
            button_book_apt = ttk.Button(master=frame_show_p,text='Book an appointment')
            button_book_apt.grid(row=1,column=0,columnspan=2,sticky='nsew',padx=10,pady=10)
            button_check_apt = ttk.Button(master=frame_show_p, text='Check next appointment')
            button_check_apt.grid(row=2, column=0, columnspan=2,sticky='nsew',padx=10,pady=10)
            button_edit_per = ttk.Button(master=frame_show_p, text='Edit personal details',command=edit_personal_det)
            button_edit_per.grid(row=3, column=0, columnspan=2,sticky='nsew',padx=10,pady=10)
            button_back_patient_portal = ttk.Button(master=frame_show_p,text='Go back',command=go_back_to_patient_portal)
            button_back_patient_portal.grid(row=4,column=1)
            frame_show_p.grid(row=0,column=0)

def edit_personal_det():
    tkinter.messagebox.showinfo(title='ACCESS DENIED',message='Please reach out to hospital admin team to edit details')

def go_back_to_patient_portal():
    frame_show_p.grid_forget()
    frame_specific_portal.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')

window.mainloop()
