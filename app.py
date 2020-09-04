# Importing Tokens
from tkinter import *
import sqlite3
from db import *
from create_label import *
# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def index():
#     db = DB()
#     #db.Insert()
#     #db.Update()
#     #db.Delete()
#     db.CreateProfile("Confidence", "James", "15-06-1989", "Lekki", "Lekki", "Abuja", "0809883232")
#     results = db.GetAll()
#     print(results)

#     return str(results)


# Defining Root Layout
root = Tk()
# root.geometry("400x400")
root.title("To Do List")
root.iconbitmap("Papirus-Team-Papirus-Apps-Python.ico")
root['bg'] = '#666'
# Defining Button Commands

def submit():
    # Insert Into Tables
    db = DB()

    first_name_prof = first_name.getvalue()
    last_name_prof = last_name.getvalue()
    dob_prof = dob.getvalue()
    address_prof = address.getvalue()
    city_prof = city.getvalue()
    state_prof = state.getvalue()
    phone_no_prof = phone_no.getvalue()

    db.CreateProfile(first_name_prof, last_name_prof, dob_prof, address_prof, city_prof, state_prof, phone_no_prof)

    # Close Connection
    db.Close()

    first_name.deletevalue()
    last_name.deletevalue()
    dob.deletevalue()
    address.deletevalue()
    city.deletevalue()
    state.deletevalue()
    phone_no.deletevalue()


def query():
    #Open New Window
    master = Toplevel()

    # Create Connection
    db = DB()

    rf = db.GetAll()
    
    for records in rf:
        CreateLabel(master, records, None, None, 3, 0)

    # Close Connection
    db.Close()

def delete_by_id():
    global entry1
    #Open New Window
    master = Toplevel()

    # Create Connection
    db = DB()

    CreateLabel(master, 'ID: ', 0, 0)

    entry1 = EntryBox(master, 0, 1)

    CreateButton(master, 'Delete', delete_prof_id, 1, 0, 2, 1, 1, 0, 0)

    # Close Connection
    db.Close()

def delete_prof_id():
    # Create Connection
    db = DB()

    # Delete From Profile
    db.DeleteProfileByID(entry1.getvalue())

    # Close Connection
    db.Close()

    entry1.deletevalue()

def delete_by_name():
    global entry1
    global entry2
    #Open New Window
    master = Toplevel()

    # Create Connection
    db = DB()

    CreateLabel(master, 'First Name: ', 0, 0)
    CreateLabel(master, 'Last Name', 1, 0)

    entry1 = EntryBox(master, 0, 1)
    entry2 = EntryBox(master, 1, 1)

    CreateButton(master, 'Delete', delete_prof_name, 2, 0, 2, 1, 1, 0, 0)

    # Close Connection
    db.Close()

def delete_prof_name():
    # Create Connection
    db = DB()

    # Delete From Profile
    db.DeleteProfileByName(entry1.getvalue(), entry2.getvalue())

    # Close Connection
    db.Close()

    entry1.deletevalue()

def update_by_id():
    global user_id
    master = Toplevel()

    CreateLabel(master, 'ID:      ', 0, 0)
    user_id = EntryBox(master, 0, 1)

    CreateButton(master, 'Update', update_prof_id, 1, 0, 2, 1, 1, 0, 0)

def update_fn():
    db = DB()

    db.Update('first_name', user_id.getvalue(), first_name1.getvalue())
    
    first_name1.deletevalue()

    db.Close()

def update_ln():
    db = DB()

    db.Update('last_name', user_id.getvalue(), last_name1.getvalue())
    
    last_name1.deletevalue()

    db.Close()

def update_dob():
    db = DB()

    db.Update('dob', user_id.getvalue(), dob1.getvalue())

    dob1.deletevalue()

    db.Close()

def update_addr():
    db = DB()

    db.Update('address', user_id.getvalue(), address1.getvalue())
    
    address1.deletevalue()

    db.Close()

def update_city():
    db = DB()

    db.Update('city', user_id.getvalue(), city1.getvalue())
    
    city1.deletevalue()

    db.Close()

def update_sta():
    db = DB()

    db.Update('state', user_id.getvalue(), state1.getvalue())

    state1.deletevalue()

    db.Close()

def update_phon():
    db = DB()

    db.Update('phone_number', user_id.getvalue(), phone_no1.getvalue())
    
    phone_no1.deletevalue()

    db.Close()

def update_all():
    db = DB()

    db.UpdateAll(user_id.getvalue(), first_name1.getvalue(), last_name1.getvalue(), dob1.getvalue(), address1.getvalue(), city1.getvalue(), state1.getvalue(), phone_no1.getvalue())

    first_name.deletevalue()
    last_name.deletevalue()
    dob.deletevalue()
    address.deletevalue()
    city.deletevalue()
    state.deletevalue()
    phone_no.deletevalue()

    db.Close()

def update_prof_id():
    global first_name1
    global last_name1
    global dob1
    global address1
    global city1
    global state1
    global phone_no1
    master = Toplevel()

    CreateLabel(master, 'First Name', 0, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
    CreateLabel(master, 'Last Name', 1, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
    CreateLabel(master, 'Date of Birth', 2, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
    CreateLabel(master, 'Address', 3, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
    CreateLabel(master, 'City', 4, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
    CreateLabel(master, 'State', 5, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
    CreateLabel(master, 'Phone Number', 6, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)

    first_name1 = EntryBox(master, 0, 1, 0, 30, 'e', 1, 0, 'sunken')
    last_name1 = EntryBox(master, 1, 1, 0, 30, 'e', 1, 0, 'sunken')
    dob1 = EntryBox(master, 2, 1, 0, 30, 'e', 1, 0, 'sunken')
    address1 = EntryBox(master, 3, 1, 0, 30, 'e', 1, 0, 'sunken')
    city1 = EntryBox(master, 4, 1, 0, 30, 'e', 1, 0, 'sunken')
    state1 = EntryBox(master, 5, 1, 0, 30, 'e', 1, 0, 'sunken')
    phone_no1 = EntryBox(master, 6, 1, 0, 30, 'e', 1, 0, 'sunken')

    CreateButton(master, "EDIT", update_fn, 0, 2, 1, 0, 0, 1, 1, 7, '#66ccff', '#666', 'nwes', 'flat')
    CreateButton(master, "EDIT", update_ln, 1, 2, 1, 1, 1, 1, 1, 7)
    CreateButton(master, "EDIT", update_dob, 2, 2, 1, 1, 1, 1, 1, 7)
    CreateButton(master, "EDIT", update_addr, 3, 2, 1, 1, 1, 1, 1, 7)
    CreateButton(master, "EDIT", update_city, 4, 2, 1, 1, 1, 1, 1, 7)
    CreateButton(master, "EDIT", update_sta, 5, 2, 1, 1, 1, 1, 1, 7)
    CreateButton(master, "EDIT", update_phon, 6, 2, 1, 1, 1, 1, 1, 7)
    CreateButton(master, "EDIT ALL", update_all, 7, 0, 3, 1, 1, 1, 1)

# CreateLabel(root)
first_name_label = CreateLabel(root, 'First Name', 0, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
last_name_label = CreateLabel(root, 'Last Name', 1, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
dob_label = CreateLabel(root, 'Date of Birth', 2, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
address_label = CreateLabel(root, 'Address', 3, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
city_label = CreateLabel(root, 'City', 4, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
state_label = CreateLabel(root, 'State', 5, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)
phone_no_label = CreateLabel(root, 'Phone Number', 6, 0, 0, 30, '#66ccff', '#666', 'e', 1, 1)

# Creating Entry Boxes
first_name = EntryBox(root, 0, 1, 0, 30, 'e', 1, 0, 'sunken')
last_name = EntryBox(root, 1, 1, 0, 30, 'e', 1, 0, 'sunken')
dob = EntryBox(root, 2, 1, 0, 30, 'e', 1, 0, 'sunken')
address = EntryBox(root, 3, 1, 0, 30, 'e', 1, 0, 'sunken')
city = EntryBox(root, 4, 1, 0, 30, 'e', 1, 0, 'sunken')
state = EntryBox(root, 5, 1, 0, 30, 'e', 1, 0, 'sunken')
phone_no = EntryBox(root, 6, 1, 0, 30, 'e', 1, 0, 'sunken')

# Creating Buttons
CreateButton(root, "Save Records", submit, 7, 0, 2, 1, 1, 90, 1)
CreateButton(root, "Print Records", query, 8, 0, 2, 1, 1, 90, 1)
CreateButton(root, 'Delete Profile By ID', delete_by_id, 9, 0, 1, 1, 1, 1, 1, 0)
CreateButton(root, 'Delete Profile By Name', delete_by_name, 9, 1, 1, 1, 1, 1, 1, 0)
CreateButton(root, 'Update Profile By ID', update_by_id, 10, 0, 2, 2, 1, 1, 1)

# Running the program
root.mainloop()
