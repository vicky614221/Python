import tkinter as tk
import tkinter.messagebox
from random import random, randint
from tkinter import ttk
from tkinter.ttk import Style
import mysql.connector
from datetime import datetime

def get_employee_det(emp_id):
    label_emp_fname_val_str.set('')
    label_emp_mname_val_str.set('')
    label_emp_lname_val_str.set('')
    label_start_date_val_str.set('')
    label_end_date_val_str.set('')
    label_per_hr_rate_val_str.set('')
    label_emp_email_val_str.set('')
    label_emp_dob_val_str.set('')
    label_emp_edu_val_str.set('')
    label_emp_mob_val_str.set('')
    label_emp_gen_val_str.set('')
    button_emp_addr.configure(state='Disabled')
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='vicky',database='rbov',auth_plugin='mysql_native_password')
    my_cursor = mydb.cursor()
    my_cursor.execute("select * from employee where emp_id = %s" ,(emp_id,))
    rows = my_cursor.fetchall()
    if len(rows) > 0:
        row = rows[0]
        label_emp_fname_val_str.set(row[1])
        label_emp_mname_val_str.set(row[2])
        label_emp_lname_val_str.set(row[3])
        label_start_date_val_str.set(row[4])
        label_end_date_val_str.set(row[5])
        label_per_hr_rate_val_str.set(row[6])
        label_emp_email_val_str.set(row[7])
        label_emp_dob_val_str.set(row[10])
        label_emp_edu_val_str.set(row[11])
        label_emp_mob_val_str.set(row[12])
        label_emp_gen_val_str.set(row[13])
        button_emp_addr.configure(state='enable')

    else:
        tkinter.messagebox.showinfo(title='ERROR',message='Row not found')

def get_emp_address(emp_id):
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='vicky',database='rbov',auth_plugin='mysql_native_password')
    my_cur = mydb.cursor()
    my_cur.execute('select address from employee where emp_id = %s' ,(emp_id,))
    rows = my_cur.fetchall()
    if len(rows) > 0:
        row = rows[0]
        tkinter.messagebox.showinfo(title='Address',message=row[0])
    else:
        tkinter.messagebox.showinfo(title='Address',message='Address not found')

def add_employee():
    window_add_emp = tk.Toplevel()
    window_add_emp.grab_set()
    window_add_emp.attributes('-topmost', True)
    window_add_emp.title('ADD NEW EMPLOYEE PORTAL')
    window_add_emp.geometry('400x700+200+20')
    window_add_emp.columnconfigure((0,1),weight=1)
    window_add_emp.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)

    label_add_emp_fname = ttk.Label(master=window_add_emp,text='Enter first name: ',foreground='blue')
    entry_add_emp_fname_str = tk.StringVar(value=None)
    entry_add_emp_fname = ttk.Entry(master=window_add_emp,text='',textvariable=entry_add_emp_fname_str)

    label_add_emp_mname = ttk.Label(master=window_add_emp,text='Enter middle name: ',foreground='blue')
    entry_add_emp_mname_str = tk.StringVar(value=None)
    entry_add_emp_mname = ttk.Entry(master=window_add_emp,text='',textvariable=entry_add_emp_mname_str)

    label_add_emp_lname = ttk.Label(master=window_add_emp, text='Enter last name: ', foreground='blue')
    entry_add_emp_lname_str = tk.StringVar(value=None)
    entry_add_emp_lname = ttk.Entry(master=window_add_emp, text='', textvariable=entry_add_emp_lname_str)

    label_add_emp_dob = ttk.Label(master=window_add_emp, text='Date of Birth(YYYY/MM/DD: ', foreground='blue')
    entry_add_emp_dob_str = tk.StringVar(value=None)
    entry_add_emp_dob = ttk.Entry(master=window_add_emp, text='', textvariable=entry_add_emp_dob_str)

    label_add_emp_edu = ttk.Label(master=window_add_emp, text='Highest Education: ', foreground='blue')
    combo_add_emp_edu_str = tk.StringVar(value=None)
    highest_edu = ['BTECH','MTECH','HIGH SCHOOL']
    combo_add_emp_edu = ttk.Combobox(master=window_add_emp, textvariable=combo_add_emp_edu_str)
    combo_add_emp_edu.configure(values=highest_edu)

    label_add_emp_mob = ttk.Label(master=window_add_emp, text='Mobile number(10 digits): ', foreground='blue')
    entry_add_emp_mob_str = tk.StringVar(value=None)
    entry_add_emp_mob = ttk.Entry(master=window_add_emp, text='', textvariable=entry_add_emp_mob_str)

    label_add_emp_email = ttk.Label(master=window_add_emp, text='Email Address: ', foreground='blue')
    entry_add_emp_email_str = tk.StringVar(value=None)
    entry_add_emp_email = ttk.Entry(master=window_add_emp, text='', textvariable=entry_add_emp_email_str)

    label_add_emp_gen = ttk.Label(master=window_add_emp, text='Gender: ', foreground='blue')
    gender_list = ['MALE','FEMALE']
    combo_add_emp_gen_str = tk.StringVar(value=None)
    combo_add_emp_gen = ttk.Combobox(master=window_add_emp,textvariable=combo_add_emp_gen_str)
    combo_add_emp_gen.configure(values=gender_list)

    label_add_emp_addr = ttk.Label(master=window_add_emp, text='Address(100 chars): ', foreground='blue')
    entry_add_emp_addr_str = tk.StringVar(value=None)
    entry_add_emp_addr = ttk.Entry(master=window_add_emp, text='', textvariable=entry_add_emp_addr_str)
    button_add_emp_save = ttk.Button(master=window_add_emp,text='Submit',
                                     command=lambda : insert_employee(entry_add_emp_fname_str.get(),
                                                                      entry_add_emp_mname_str.get(),
                                                                      entry_add_emp_lname_str.get(),
                                                                      entry_add_emp_dob_str.get(),
                                                                      combo_add_emp_edu_str.get(),
                                                                      entry_add_emp_mob_str.get(),
                                                                      entry_add_emp_email_str.get(),
                                                                      combo_add_emp_gen_str.get(),
                                                                      entry_add_emp_addr_str.get()))

    label_add_emp_fname.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)
    entry_add_emp_fname.grid(row=0,column=1,sticky='ew',padx=10,pady=10)

    label_add_emp_mname.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
    entry_add_emp_mname.grid(row=1, column=1, sticky='ew', padx=10, pady=10)

    label_add_emp_lname.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
    entry_add_emp_lname.grid(row=2, column=1, sticky='ew', padx=10, pady=10)

    label_add_emp_dob.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
    entry_add_emp_dob.grid(row=3, column=1, sticky='ew', padx=10, pady=10)

    label_add_emp_edu.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
    combo_add_emp_edu.grid(row=4, column=1, sticky='ew', padx=10, pady=10)

    label_add_emp_mob.grid(row=5, column=0, sticky='nsew', padx=10, pady=10)
    entry_add_emp_mob.grid(row=5, column=1, sticky='ew', padx=10, pady=10)

    label_add_emp_email.grid(row=6, column=0, sticky='nsew', padx=10, pady=10)
    entry_add_emp_email.grid(row=6, column=1, sticky='ew', padx=10, pady=10)

    label_add_emp_gen.grid(row=7, column=0, sticky='nsew', padx=10, pady=10)
    combo_add_emp_gen.grid(row=7, column=1, sticky='ew', padx=10, pady=10)

    label_add_emp_addr.grid(row=8, column=0, sticky='nsew', padx=10, pady=10)
    entry_add_emp_addr.grid(row=8, column=1, sticky='ew', padx=10, pady=10)

    button_add_emp_save.grid(row=9, column=1, sticky='nsew', padx=10, pady=10)

    def insert_employee(emp_fname,emp_mname,emp_lname,emp_dob,emp_edu,emp_mob,emp_email,emp_gen,emp_addr):

        if (len(emp_fname) > 0 and len(emp_mname) > 0 and len(emp_lname) > 0 and len(emp_dob) > 0 and len(emp_edu) > 0
            and len(emp_mob) > 0 and len(emp_email) > 0 and len(emp_gen) > 0 and len(emp_addr) > 0):
            try:
                emp_id = emp_fname[0] + emp_lname[0] + str(randint(1000,9999))
                curr_tmsp = datetime.now()
                upd_by = 'Admin'
                mydb = mysql.connector.connect(host='localhost', user='root', passwd='vicky', database='rbov',
                                               auth_plugin='mysql_native_password')
                my_cur = mydb.cursor()
                my_cur.execute('insert into employee (emp_id, emp_fname, emp_mname, emp_lname,start_date_tmsp,per_hour_rate,'
                               'email_id,last_upd_by,dob,highest_edu,mobile_no,gender,address) values '
                               '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (emp_id,emp_fname,emp_mname,emp_lname,curr_tmsp,18.9,emp_email,
                                                                          upd_by,emp_dob,emp_edu,emp_mob,emp_gen,emp_addr))
                mydb.commit()
                mydb.close()
                tkinter.messagebox.showinfo(title='SUCCESS',message=f'Employee {emp_id} added successfully')
                entry_add_emp_fname_str.set('')
                entry_add_emp_mname_str.set('')
                entry_add_emp_lname_str.set('')
                entry_add_emp_email_str.set('')
                entry_add_emp_dob_str.set('')
                combo_add_emp_edu_str.set('')
                entry_add_emp_mob_str.set('')
                combo_add_emp_gen_str.set('')
                entry_add_emp_addr_str.set('')

            except:
                tkinter.messagebox.showinfo(title='FATAL ERROR',message='Unable to add details, try again')
        else:
            window_add_emp.attributes('-topmost', False)
            tkinter.messagebox.showinfo(title='Error', message='Please fill all values before submitting')
            window_add_emp.attributes('-topmost', True)


window = tk.Tk()
window.title('Employee portal')
screen_width = int(window.winfo_screenwidth())
screen_height = int(window.winfo_screenheight())
window.geometry(('%dx%d'%(screen_width,screen_height)))
window.minsize(width=600,height=700)
#window.maxsize(width=600,height=700)
window.bind('<Escape>',lambda event: window.quit())
window.iconbitmap('window_icon.ico')

style_frame_choice = ttk.Style()
style_frame_choice.configure("frame_choice.TFrame",foreground="green", relief="raise")

# WINDOW GRID CREATION--------------------------------------------------------------------------
window.columnconfigure(0,weight=1)
window.rowconfigure((0,1,2),weight=1)
window.rowconfigure(3,weight=10)
# WIDGETS FOR TOP FRAME-------------------------------------------------------------------------
frame_choice = ttk.Frame(master=window,style="frame_choice.TFrame")
# TOP FRAME GRID CREATION-----------------------------------------------------------------------
frame_choice.columnconfigure((0,1,2,3),weight=1)
frame_choice.rowconfigure((0,1,2),weight=1)

label_emp_enquiry = ttk.Label(master=frame_choice,text='ENQUIRE EMPLOYEE',foreground='blue')
entry_emp_enquiry_str = tk.StringVar(value='Enter employee id')
entry_emp_enquiry = ttk.Entry(master=frame_choice,textvariable=entry_emp_enquiry_str)
button_emp_enquiry = ttk.Button(master = frame_choice,text='Click here',command= lambda :get_employee_det(entry_emp_enquiry_str.get()))

label_emp_update = ttk.Label(master=frame_choice,text='UPDATE EMPLOYEE DETAILS',foreground='orange')
entry_emp_update_str = tk.StringVar(value='Enter employee id')
entry_emp_update = ttk.Entry(master=frame_choice,textvariable=entry_emp_update_str)
button_emp_update = ttk.Button(master = frame_choice,text='Click here')

label_emp_add = ttk.Label(master=frame_choice,text='ADD NEW EMPLOYEE',foreground='green')
button_emp_add = ttk.Button(master = frame_choice,text='Click here',command=add_employee)

label_emp_del = ttk.Label(master=frame_choice,text='DELETE EMPLOYEE',foreground='red')
entry_emp_del_str = tk.StringVar(value='Enter employee id')
entry_emp_del = ttk.Entry(master=frame_choice,textvariable=entry_emp_del_str)
button_emp_del = ttk.Button(master = frame_choice,text='Click here')
# TOP FRAME WIDGET POSITION-----------------------------------------------------------
label_emp_enquiry.grid(row=0,column=0,padx=20,pady=10)
entry_emp_enquiry.grid(row=1,column=0,padx=5,pady=5)
button_emp_enquiry.grid(row=2,column=0,padx=5,pady=5)

label_emp_update.grid(row=0,column=1,padx=20,pady=10)
entry_emp_update.grid(row=1,column=1,padx=5,pady=5)
button_emp_update.grid(row=2,column=1,padx=5,pady=5)

label_emp_add.grid(row=0,column=2,padx=20,pady=10)
button_emp_add.grid(row=2,column=2,padx=5,pady=5)

label_emp_del.grid(row=0,column=3,padx=20,pady=10)
entry_emp_del.grid(row=1,column=3,padx=5,pady=5)
button_emp_del.grid(row=2,column=3,padx=5,pady=5)

frame_choice.grid(row=0,column=0,sticky='ews')
# WIDGETS FOR SECOND FRAME (Bottom of TOP FRAME) ---------------------------------------
style_frame_employee_per_det = Style()
style_frame_employee_per_det.configure("style_frame_employee_per_det.TFrame",foreground="green", relief="sunken")
frame_employee_per_det = ttk.Frame(master=window,style="style_frame_employee_per_det.TFrame")

label_emp_fname = ttk.Label(master=frame_employee_per_det,text='FIRST NAME: ',foreground='blue')

label_emp_fname_val_str = tk.StringVar(value=None)
label_emp_fname_val = ttk.Label(master=frame_employee_per_det,text='',textvariable=label_emp_fname_val_str,foreground='green')

label_emp_mname = ttk.Label(master=frame_employee_per_det,text='MIDDLE NAME: ',foreground='blue')
label_emp_mname_val_str = tk.StringVar(value=None)
label_emp_mname_val = ttk.Label(master=frame_employee_per_det,text='',textvariable=label_emp_mname_val_str,foreground='green')

label_emp_lname = ttk.Label(master=frame_employee_per_det,text='LAST NAME: ',foreground='blue')
label_emp_lname_val_str = tk.StringVar(value=None)
label_emp_lname_val = ttk.Label(master=frame_employee_per_det,text='',textvariable=label_emp_lname_val_str,foreground='green')

label_emp_dob = ttk.Label(master=frame_employee_per_det,text='DATE OF BIRTH: ',foreground='blue')
label_emp_dob_val_str = tk.StringVar(value=None)
label_emp_dob_val = ttk.Label(master=frame_employee_per_det,text='',textvariable=label_emp_dob_val_str,foreground='green')

label_emp_edu = ttk.Label(master=frame_employee_per_det,text='HIGHEST EDUCATION: ',foreground='blue')
label_emp_edu_val_str = tk.StringVar(value=None)
label_emp_edu_val = ttk.Label(master=frame_employee_per_det,text='',textvariable=label_emp_edu_val_str,foreground='green')

label_emp_mob = ttk.Label(master=frame_employee_per_det,text='MOBILE NUMBER: ',foreground='blue')
label_emp_mob_val_str = tk.StringVar(value=None)
label_emp_mob_val = ttk.Label(master=frame_employee_per_det,text='',textvariable=label_emp_mob_val_str,foreground='green')

# SECOND FRAME GRID CREATION-----------------------------------------------------------------------
frame_employee_per_det.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11),weight=1)
frame_employee_per_det.rowconfigure(0,weight=1)
# SECOND FRAME WIDGET POSITION---------------------------------------------------------------------
label_emp_fname.grid(row=0,column=0,padx=10,pady=10,sticky='we')
label_emp_fname_val.grid(row=0,column=1,padx=10,pady=10,sticky='we')

label_emp_mname.grid(row=0,column=2,padx=10,pady=10,sticky='we')
label_emp_mname_val.grid(row=0,column=3,padx=10,pady=10,sticky='we')

label_emp_lname.grid(row=0,column=4,padx=10,pady=10,sticky='we')
label_emp_lname_val.grid(row=0,column=5,padx=10,pady=10,sticky='we')

label_emp_dob.grid(row=0,column=6,padx=10,pady=10,sticky='we')
label_emp_dob_val.grid(row=0,column=7,padx=10,pady=10,sticky='we')

label_emp_edu.grid(row=0,column=8,padx=10,pady=10,sticky='we')
label_emp_edu_val.grid(row=0,column=9,padx=10,pady=10,sticky='we')

label_emp_mob.grid(row=0,column=10,padx=10,pady=10,sticky='we')
label_emp_mob_val.grid(row=0,column=11,padx=10,pady=10,sticky='we')

frame_employee_per_det.grid(row=1,column=0,sticky='nsew')
#************
# WIDGETS FOR THIRD FRAME (Bottom of SECOND FRAME) ---------------------------------------
style_frame_employee_per_det2 = Style()
style_frame_employee_per_det2.configure("style_frame_employee_per_det2.TFrame",foreground="green", relief="sunken")
frame_employee_per_det2 = ttk.Frame(master=window,style="style_frame_employee_per_det2.TFrame")

label_start_date = ttk.Label(master=frame_employee_per_det2,text='START DATE: ',foreground='blue')
label_start_date_val_str = tk.StringVar(value=None)
label_start_date_val = ttk.Label(master=frame_employee_per_det2,text='',textvariable=label_start_date_val_str,foreground='green')

label_end_date = ttk.Label(master=frame_employee_per_det2,text='END DATE: ',foreground='blue')
label_end_date_val_str = tk.StringVar(value=None)
label_end_date_val = ttk.Label(master=frame_employee_per_det2,text='',textvariable=label_end_date_val_str,foreground='green')

label_per_hr_rate = ttk.Label(master=frame_employee_per_det2,text='BILL RATE/HOUR: ',foreground='blue')
label_per_hr_rate_val_str = tk.DoubleVar(value=None)
label_per_hr_rate_val = ttk.Label(master=frame_employee_per_det2,text='',textvariable=label_per_hr_rate_val_str,foreground='green')

label_emp_email = ttk.Label(master=frame_employee_per_det2,text='EMAIL ID: ',foreground='blue')
label_emp_email_val_str = tk.DoubleVar(value=None)
label_emp_email_val = ttk.Label(master=frame_employee_per_det2,text='',textvariable=label_emp_email_val_str,foreground='green')

label_emp_gen = ttk.Label(master=frame_employee_per_det2,text='GENDER: ',foreground='blue')
label_emp_gen_val_str = tk.StringVar(value=None)
label_emp_gen_val = ttk.Label(master=frame_employee_per_det2,text='',textvariable=label_emp_gen_val_str,foreground='green')

label_emp_addr = ttk.Label(master=frame_employee_per_det2,text='ADDRESS: ',foreground='blue')
button_emp_addr = ttk.Button(master=frame_employee_per_det2,text='Click here',state='disabled',
                             command=lambda : get_emp_address(entry_emp_enquiry_str.get()))
# THIRD FRAME GRID CREATION-----------------------------------------------------------------------
frame_employee_per_det2.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11),weight=1)
frame_employee_per_det2.rowconfigure((0),weight=1)
# THIRD FRAME WIDGET POSITION---------------------------------------------------------------------
label_start_date.grid(row=0,column=0,padx=10,pady=10,sticky='we')
label_start_date_val.grid(row=0,column=1,padx=10,pady=10,sticky='we')

label_end_date.grid(row=0,column=2,padx=10,pady=10,sticky='we')
label_end_date_val.grid(row=0,column=3,padx=10,pady=10,sticky='we')

label_per_hr_rate.grid(row=0,column=4,padx=10,pady=10,sticky='we')
label_per_hr_rate_val.grid(row=0,column=5,padx=10,pady=10,sticky='we')

label_emp_email.grid(row=0,column=6,padx=10,pady=10,sticky='we')
label_emp_email_val.grid(row=0,column=7,padx=10,pady=10,sticky='we')

label_emp_gen.grid(row=0,column=8,padx=10,pady=10,sticky='we')
label_emp_gen_val.grid(row=0,column=9,padx=10,pady=10,sticky='we')

label_emp_addr.grid(row=0,column=10,padx=10,pady=10,sticky='we')
button_emp_addr.grid(row=0,column=11,padx=10,pady=10,sticky='we')

frame_employee_per_det2.grid(row=2,column=0,sticky='nsew')
window.mainloop()