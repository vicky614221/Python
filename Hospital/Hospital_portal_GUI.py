import tkinter as tk
import tkinter.messagebox
from doctest import master
from tkinter import ttk, PhotoImage
from hospital import *

window = tk.Tk()
window.title('WE CARE HOSPITAL')
scr_width = window.winfo_screenwidth()
scr_height = window.winfo_screenheight()
window.minsize(width=scr_width,height=scr_height)
window.columnconfigure(0,weight=1)
window.rowconfigure((0,1,2),weight=1)

# we will use only one window with header and trailer and navigate between screens using different frame by hiding and bringing back when required
#-----------------------window header frame creation and widgets-------------------------------
window_header_frame = ttk.Frame(master=window)
window_header_frame.rowconfigure(0,weight=1)
window_header_frame.columnconfigure(0,weight=1)
label_hospital_name = ttk.Label(master=window_header_frame,text='WE CARE HOSPITAL',font='Ariel,90,bold',foreground='blue',anchor='center',background='orange')
label_hospital_name.grid(row=0,column=0,sticky='nsew')
window_header_frame.grid(row=0,column=0,sticky='nsew')
#-----------------------window trailer frame creation and widgets-------------------------------
window_trailer_frame = tk.Frame(master=window)
window_trailer_frame.rowconfigure(0,weight=1)
window_trailer_frame.columnconfigure(0,weight=1)
label_trailer = ttk.Label(master=window_trailer_frame,text='This is a trailer placeholder',font='Ariel,90,bold',foreground='blue',background='green',anchor='center')
label_trailer.grid(row=0,column=0,sticky='nsew')
window_trailer_frame.grid(row=2,column=0,sticky='nsew')
#-----------------------main window frame creation and widgets----------------------------
window_frame = ttk.Frame(master=window)
window_frame.rowconfigure(0,weight=1)
window_frame.columnconfigure(0,weight=1)
#image = PhotoImage(file='hospital_image.png')
#label_image = ttk.Label(master=window_frame,image=image)
#label_image.grid(row=0,column=0)
window_frame.grid(row=1,column=0,sticky='nsew',padx=5,pady=5)
#----------------------portal selection frame creation and widgets-------------------------
window_portal_select_frame = tk.Frame(master=window_frame)
window_portal_select_frame.rowconfigure(0,weight=1)
window_portal_select_frame.columnconfigure((0,1,2),weight=1)
button_patient_portal = ttk.Button(master=window_portal_select_frame,text="PATIENT'S PORTAL",command=lambda :open_specific_portal('P'))
button_patient_portal.grid(row=0,column=0,sticky='nsew',pady=5,padx=10)
button_doctor_portal = ttk.Button(master=window_portal_select_frame,text="DOCTOR'S PORTAL")
button_doctor_portal.grid(row=0,column=1,sticky='nsew',pady=5,padx=10)
button_admin_portal = ttk.Button(master=window_portal_select_frame,text="ADMIN'S PORTAL")
button_admin_portal.grid(row=0,column=2,sticky='nsew',pady=5,padx=10)
window_portal_select_frame.grid(row=0,column=0,sticky='nsew')



def open_specific_portal(user):
    if user == 'P':
        window_portal_select_frame.grid_forget()
        global window_patient_login_frame
        window_patient_login_frame = tk.Frame(master=window_frame)
        window_patient_login_frame.rowconfigure((0,1,2,3,4,5),weight=1)
        window_patient_login_frame.columnconfigure((0,1,2),weight=1)
        label_patient_heading = ttk.Label(master=window_patient_login_frame,text='PATIENT PORTAL LOGIN',background='red',font='Ariel,40,bold')
        label_patient_heading.grid(row=0,column=0,columnspan=3,pady=10)
        global rbutton_select_str
        rbutton_select_str = tk.StringVar()
        rbutton_select1 = ttk.Radiobutton(master=window_patient_login_frame,text='First time user?',variable=rbutton_select_str,value='new',command=new_patient_selected)
        rbutton_select1.grid(row=1,column=0)
        #rbutton_select_str = tk.StringVar()
        rbutton_select2 = ttk.Radiobutton(master=window_patient_login_frame,text='Existing user?',variable=rbutton_select_str,value='existing',command=exist_patient_selected)
        rbutton_select2.grid(row=1,column=2)
        global entry_id_str
        entry_id_str = tk.StringVar(value='Enter patient ID')
        global entry_id
        entry_id = tk.Entry(master=window_patient_login_frame,textvariable=entry_id_str,state='disabled')
        entry_id.grid(row=2,column=2,padx=5,pady=5)
        global entry_pwd_str
        entry_pwd_str = tk.StringVar(value='Enter your password')
        global entry_pwd
        entry_pwd = tk.Entry(master=window_patient_login_frame,textvariable=entry_pwd_str,show='*',state='disabled')
        entry_pwd.grid(row=3,column=2,padx=5,pady=5)
        global button_submit
        button_submit = ttk.Button(master=window_patient_login_frame,text='SUBMIT',state='disabled',command=lambda :validate_and_show(user))
        button_submit.grid(row=4,column=2)

        global button_p_login_back
        button_p_login_back = ttk.Button(master=window_patient_login_frame,text='BACK',command=go_back_to_portal_select)
        button_p_login_back.grid(row=5,column=2)

        window_patient_login_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    elif user == 'D':
        pass
    else:
        pass

def exist_patient_selected():
    if rbutton_select_str.get() == 'existing':
        entry_id.configure(state='normal')
        entry_pwd.configure(state='normal')
        button_submit.configure(state='enabled')
        try:
            window_new_patient_frame.grid_forget()
        except:
            pass

def new_patient_selected():
    if rbutton_select_str.get() == 'new':
        entry_id.configure(state='disabled')
        entry_pwd.configure(state='disabled')
        button_submit.configure(state='disabled')
        global window_new_patient_frame
        window_new_patient_frame = tk.Frame(master=window_patient_login_frame)
        window_new_patient_frame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
        window_new_patient_frame.columnconfigure((0,1),weight=1)

        label_p_name = ttk.Label(master=window_new_patient_frame,text='Patient Full Name: ')
        label_p_name.grid(row=0,column=0,sticky='ew',padx=5,pady=5)

        global entry_p_name_str
        entry_p_name_str = tk.StringVar()
        entry_p_name = ttk.Entry(master=window_new_patient_frame,textvariable=entry_p_name_str)
        entry_p_name.grid(row=0,column=1,sticky='ew',padx=5,pady=5)

        label_p_dob = ttk.Label(master=window_new_patient_frame, text='Patient D.O.B(YYYY/MM/DD): ')
        label_p_dob.grid(row=1, column=0,sticky='ew',padx=5,pady=5)
        global entry_p_dob_str
        entry_p_dob_str = tk.StringVar()
        entry_p_dob = ttk.Entry(master=window_new_patient_frame, textvariable=entry_p_dob_str)
        entry_p_dob.grid(row=1, column=1,sticky='ew',padx=5,pady=5)

        label_p_gen = ttk.Label(master=window_new_patient_frame, text='Patient Gender: ')
        label_p_gen.grid(row=2, column=0,sticky='ew',padx=5,pady=5)
        global combo_p_gen_str
        combo_p_gen_str = tk.StringVar()
        gen_list = ['MALE','FEMALE']
        combo_p_gen = ttk.Combobox(master=window_new_patient_frame, textvariable=combo_p_gen_str)
        combo_p_gen.configure(values=gen_list)
        combo_p_gen.grid(row=2, column=1,sticky='ew',padx=5,pady=5)

        label_p_email = ttk.Label(master=window_new_patient_frame, text='Patient Email ID: ')
        label_p_email.grid(row=3, column=0, sticky='ew', padx=5,pady=5)
        global entry_p_email_str
        entry_p_email_str = tk.StringVar()
        entry_p_email = ttk.Entry(master=window_new_patient_frame, textvariable=entry_p_email_str)
        entry_p_email.grid(row=3, column=1, sticky='ew', padx=5,pady=5)

        label_p_phone = ttk.Label(master=window_new_patient_frame, text='Patient Phone No.: ')
        label_p_phone.grid(row=4, column=0, sticky='ew', padx=5,pady=5)
        global entry_p_phone_str
        entry_p_phone_str = tk.StringVar()
        entry_p_phone = ttk.Entry(master=window_new_patient_frame, textvariable=entry_p_phone_str)
        entry_p_phone.grid(row=4, column=1, sticky='ew', padx=5,pady=5)

        label_p_adhar = ttk.Label(master=window_new_patient_frame, text='Patient Aadhar No.: ')
        label_p_adhar.grid(row=5, column=0, sticky='ew', padx=5,pady=5)
        global entry_p_adhar_str
        entry_p_adhar_str = tk.StringVar()
        entry_p_adhar = ttk.Entry(master=window_new_patient_frame, textvariable=entry_p_adhar_str)
        entry_p_adhar.grid(row=5, column=1, sticky='ew', padx=5,pady=5)

        label_p_addr = ttk.Label(master=window_new_patient_frame, text='Patient Address: ')
        label_p_addr.grid(row=6, column=0, sticky='ew', padx=5,pady=5)
        global entry_p_addr_str
        entry_p_addr_str = tk.StringVar()
        entry_p_addr = ttk.Entry(master=window_new_patient_frame, textvariable=entry_p_addr_str)
        entry_p_addr.grid(row=6, column=1, sticky='ew', padx=5,pady=5)

        button_submit_patient = ttk.Button(master=window_new_patient_frame,
                                           text='SUBMIT',
                                           command=add_patient)
        button_submit_patient.grid(row=7,column=0)

        button_p_login_back_from_new_p = ttk.Button(master=window_new_patient_frame,text='BACK',command=go_back_to_portal_select)
        button_p_login_back_from_new_p.grid(row=7,column=1)

        window_new_patient_frame.grid(row=1, column=0, rowspan=6)

def add_patient():
    PortalUser(user=None, id=None, name=None, dob=None,
               gender=None, email=None, phone_no=None, aadhar=None, address=None).add_portal_user(user='P', patient_name=entry_p_name_str.get(),
                     patient_dob=entry_p_dob_str.get(),
                     patient_gen=combo_p_gen_str.get(),
                     patient_email=entry_p_email_str.get(),
                     patient_phone=entry_p_phone_str.get(),
                     patient_adhar=entry_p_adhar_str.get(),
                     patient_addr=entry_p_addr_str.get())

def show_patient_det():
    print(entry_id_str.get())
    PortalUser(user='P', id=entry_id_str.get(), name=None, dob=None, gender=None,email=None,phone_no=None,address=None).get_portal_user_info(user='P',user_id=entry_id.get())

def validate_and_show(user):
    if user == 'P':
        patient_obj = PortalUser(user='P', id=entry_id_str.get(),name=None, dob=None, gender=None,email=None,phone_no=None,aadhar=None,address=None)
        (is_valid,patient_basic_det) = patient_obj.is_valid_user('P',entry_id_str.get(),entry_pwd_str.get())
        if is_valid:
            patient_name = patient_basic_det[0][2]
            window_portal_select_frame.grid_forget()
            window_patient_login_frame.grid_forget()
            global window_show_p_frame
            window_show_p_frame = ttk.Frame(master=window_frame)
            window_show_p_frame.columnconfigure((0,1),weight=1)
            window_show_p_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)
            label_p_heading = ttk.Label(master=window_show_p_frame,text=('Hello '+ patient_name.upper()),font=('Times New Roman', 15, 'bold'),foreground='blue')
            label_p_heading.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
            button_book_apt = ttk.Button(master=window_show_p_frame,text='Book an appointment')
            button_book_apt.grid(row=1,column=0,columnspan=2,sticky='nsew',padx=10,pady=10)
            button_check_apt = ttk.Button(master=window_show_p_frame, text='Check next appointment',command=check_appointment)
            button_check_apt.grid(row=2, column=0, columnspan=2,sticky='nsew',padx=10,pady=10)
            button_edit_per = ttk.Button(master=window_show_p_frame, text='Edit personal details',command=edit_personal_det)
            button_edit_per.grid(row=3, column=0, columnspan=2,sticky='nsew',padx=10,pady=10)
            button_back_patient_portal = ttk.Button(master=window_show_p_frame,text='Go back',command=go_back_to_patient_p_login_portal)
            button_back_patient_portal.grid(row=4,column=1)
            window_show_p_frame.grid(row=0,column=0)

def edit_personal_det():
    tkinter.messagebox.showinfo(title='ACCESS DENIED',message='Please reach out to hospital admin team to edit details')

def go_back_to_patient_p_login_portal():
    window_show_p_frame.grid_forget()
    entry_id_str.set('Enter your ID')
    entry_pwd_str.set('Enter your password')
    window_patient_login_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

def go_back_to_portal_select():
    window_patient_login_frame.grid_forget()
    window_portal_select_frame.grid(row=0,column=0,sticky='nsew')

button_next_click_count = 0
def check_appointment():
    patient_obj = PortalUser(user='P', id=entry_id_str.get(), name=None, dob=None, gender=None, email=None,
                             phone_no=None, aadhar=None, address=None)
    global patient_and_apmt_det
    patient_and_apmt_det = []
    patient_and_apmt_det = patient_obj.get_portal_user_info()
    if len(patient_and_apmt_det)  > 0:
        window_show_p_frame.grid_forget()
        global frame_appointment_det
        frame_appointment_det = {}
        label_apmt_id = {}
        label_apmt_id_val_str = {}
        label_apmt_id_val = {}
        label_patient_id = {}
        label_patient_id_val_str = {}
        label_patient_id_val = {}
        label_doctor_name = {}
        label_doctor_name_val_str = {}
        label_doctor_name_val = {}
        label_apmt_date = {}
        label_apmt_date_val_str = {}
        label_apmt_date_val = {}
        label_apmt_time = {}
        label_apmt_time_val_str = {}
        label_apmt_time_val ={}
        button_next = {}
        button_prev = {}
        button_back = {}

        number_of_apmt_frames = len(patient_and_apmt_det)
        for i in range(number_of_apmt_frames):
            frame_appointment_det[i] = tk.Frame(master=window_frame)
            frame_appointment_det[i].rowconfigure((0,1,2,3,4,5,6),weight=1)
            frame_appointment_det[i].columnconfigure((0,1),weight=1)

            #label_apmt_id[i] = ttk.Label(master=frame_appointment_det[i],text='Appointment ID: ')
            #label_apmt_id[i].grid(row=0,column=0,sticky='nsew')

            #label_apmt_id_val_str[i] = tk.StringVar(value=patient_and_apmt_det[i][8])
            #label_apmt_id_val[i] = tk.Label(master=frame_appointment_det[i],textvariable=label_apmt_id_val_str[i])
            #label_apmt_id_val[i].grid(row=0,column=1)

            label_patient_id[i] = ttk.Label(master=frame_appointment_det[i], text='Patient ID: ')
            label_patient_id[i].grid(row=1, column=0)

            label_patient_id_val_str[i] = tk.StringVar(value=patient_and_apmt_det[i][0])
            label_patient_id_val[i] = tk.Label(master=frame_appointment_det[i], textvariable=label_patient_id_val_str[i])
            label_patient_id_val[i].grid(row=1, column=1)

            label_doctor_name[i] = ttk.Label(master=frame_appointment_det[i], text='Doctor Name: ')
            label_doctor_name[i].grid(row=2, column=0)

            label_doctor_name_val_str[i] = tk.StringVar(value=patient_and_apmt_det[i][12])
            label_doctor_name_val[i] = tk.Label(master=frame_appointment_det[i], textvariable=label_doctor_name_val_str[i])
            label_doctor_name_val[i].grid(row=2, column=1)

            label_apmt_date[i] = ttk.Label(master=frame_appointment_det[i], text='Appointment Date: ')
            label_apmt_date[i].grid(row=3, column=0)

            label_apmt_date_val_str[i] = tk.StringVar(value=patient_and_apmt_det[i][9])
            label_apmt_date_val[i] = tk.Label(master=frame_appointment_det[i],
                                                textvariable=label_apmt_date_val_str[i])
            label_apmt_date_val[i].grid(row=3, column=1)

            label_apmt_time[i] = ttk.Label(master=frame_appointment_det[i], text='Appointment Time: ')
            label_apmt_time[i].grid(row=4, column=0)

            label_apmt_time_val_str[i] = tk.StringVar(value=patient_and_apmt_det[i][10])
            label_apmt_time_val[i] = tk.Label(master=frame_appointment_det[i],
                                              textvariable=label_apmt_time_val_str[i])
            label_apmt_time_val[i].grid(row=4, column=1)

            button_next[i] = ttk.Button(master=frame_appointment_det[i],text='Next',command= next_button_pressed)
            button_prev[i] = ttk.Button(master=frame_appointment_det[i],text='Prev',command= prev_button_pressed)
            button_back[i] = ttk.Button(master=frame_appointment_det[i],text='Back',command=go_back_patient_show)
            button_next[i].grid(row=5,column=0)
            button_prev[i].grid(row=5,column=1)
            button_back[i].grid(row=6,column=0,columnspan=2)
        global button_next_click_count
        if button_next_click_count == 0:
            frame_appointment_det[0].grid(row=0,column=0,sticky='nsew')
    else:
        tk.messagebox.showinfo(title='No appointments',message='You have no future appointments, Book an appointment to see details')

def next_button_pressed():
    global button_next_click_count
    if button_next_click_count < (len(patient_and_apmt_det)-1):
        frame_appointment_det[button_next_click_count].grid_forget()
        button_next_click_count = button_next_click_count + 1
        frame_appointment_det[button_next_click_count].grid(row=0,column=0,sticky='nsew')
    else:
        tk.messagebox.showinfo(title='Last page',message='This is the last page')

def prev_button_pressed():
    global button_next_click_count
    if button_next_click_count > 0:
        frame_appointment_det[button_next_click_count].grid_forget()
        button_next_click_count = button_next_click_count - 1
        frame_appointment_det[button_next_click_count].grid(row=0,column=0,sticky='nsew')
    else:
        tk.messagebox.showinfo(title='First page',message='This is the first page')

def go_back_patient_show():
    global button_next_click_count
    button_next_click_count = 0
    for i in range(len(patient_and_apmt_det)):
        frame_appointment_det[i].grid_forget()
    window_show_p_frame.grid(row=0, column=0)


window.mainloop()
