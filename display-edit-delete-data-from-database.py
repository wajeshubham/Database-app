"""CUI for database app using tkinter and sqlite3
using this you can store and display the data
in/from the database and you can delete/edit the
data present in the database as well, refer
"create-the-table.py" to create the table for your database"""

from tkinter import *
import sqlite3

# create the window
root = Tk()
root.title("Database")
root.iconbitmap("database.png")
root.geometry("370x600")

# create the database or connect to database
conn = sqlite3.connect("data.db")

# create cursor
c = conn.cursor()

# create a table, reffer "create-the-table.py" file
'''
c.execute("""CREATE TABLE shubham (
         first_name text,
         last_name text,
         address text,
         city text,
         state text,
         pincode integer
         )""")

'''


# function to save edited data
def update():
    # create the database or connect to database
    conn = sqlite3.connect("data.db")

    # create cursor
    c = conn.cursor()

    # update the data by following method
    c.execute("""UPDATE shubham SET
             first_name = :first,
             last_name =:last,
             address = :address,
             city =:city,
             state = :state,
             pincode = :pincode
             WHERE oid=:oid""",
              {'first': first_name_editor.get(),
               'last': last_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               'pincode': pincode_editor.get(),
               'oid': manage_ID.get()}
              )

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # create confirmation label
    lbl = Label(editor, text="OPERATION DONE!")
    lbl.grid(row=8, column=0, columnspan=2, pady=10)


# function to edit records
def edit():
    global editor
    editor = Toplevel()
    editor.title("Edit Database")
    editor.geometry("370x300")

    # create the database or connect to database
    conn = sqlite3.connect("data.db")

    # create cursor
    c = conn.cursor()

    global first_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global state_editor
    global pincode_editor

    # create user editors
    first_name_editor = Entry(editor, width=50, borderwidth=3)
    first_name_editor.grid(row=0, column=1, pady=(10, 0))

    last_name_editor = Entry(editor, width=50, borderwidth=3)
    last_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=50, borderwidth=3)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=50, borderwidth=3)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=50, borderwidth=3)
    state_editor.grid(row=4, column=1)

    pincode_editor = Entry(editor, width=50, borderwidth=3)
    pincode_editor.grid(row=5, column=1)

    record_ID = manage_ID.get()
    c.execute("SELECT * FROM shubham WHERE oid=" + record_ID)
    record = c.fetchall()

    # loop throught selected record to insert values in editor window
    for rec in record:
        first_name_editor.insert(0, rec[0])
        last_name_editor.insert(0, rec[1])
        address_editor.insert(0, rec[2])
        city_editor.insert(0, rec[3])
        state_editor.insert(0, rec[4])
        pincode_editor.insert(0, rec[5])

    # create labels
    lbl1 = Label(editor, text="First name")
    lbl1.grid(row=0, column=0, pady=(10, 0))

    lbl2 = Label(editor, text="Last name")
    lbl2.grid(row=1, column=0)

    lbl3 = Label(editor, text="Address")
    lbl3.grid(row=2, column=0)

    lbl4 = Label(editor, text="City")
    lbl4.grid(row=3, column=0)

    lbl5 = Label(editor, text="State")
    lbl5.grid(row=4, column=0)

    lbl6 = Label(editor, text="Pincode")
    lbl6.grid(row=5, column=0)

    save_btn = Button(editor, text="Save changes", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, ipadx=140, pady=10)

    # create exit button
    done_btn = Button(editor, text="Exit", command=editor.destroy)
    done_btn.grid(row=7, column=0, columnspan=2, ipadx=162)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# fuction to delete the id
def delete():
    # create the database or connect to database
    conn = sqlite3.connect("data.db")

    # create cursor
    c = conn.cursor()

    c.execute("DELETE from shubham WHERE oid=" + manage_ID.get())
    manage_ID.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# function to store the data
def submit():
    # create the database or connect to database
    conn = sqlite3.connect("data.db")

    # create cursor
    c = conn.cursor()

    # insert the record in table
    c.execute("INSERT INTO shubham VALUES (:f_name,:l_name,:address,:city,:state,:pincode)",
              {'f_name': first_name.get(),
               'l_name': last_name.get(),
               'address': address.get(),
               'city': city.get(),
               'state': state.get(),
               'pincode': pincode.get()
               })

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear the text boxes for next record
    last_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)
    pincode.delete(0, END)
    first_name.delete(0, END)


# function to display the data
def query():
    # create the database or connect to database
    conn = sqlite3.connect("data.db")

    # create cursor
    c = conn.cursor()

    # fetch all data from the file after adding it
    c.execute("SELECT *,oid FROM shubham")
    record = c.fetchall()

    '''to see the saved data use 
    "print(record) statement"'''

    print_record = " "

    # logic to display the saved data
    for i in record:
        print_record += str(i[0]) + " " + str(i[1]) + "\t" + str(i[6]) + "\n"
    lbl = Label(root, text=print_record)
    lbl.grid(row=11, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create user editors
first_name = Entry(root, width=50, borderwidth=3)
first_name.grid(row=0, column=1, pady=(10, 0))

last_name = Entry(root, width=50, borderwidth=3)
last_name.grid(row=1, column=1)

address = Entry(root, width=50, borderwidth=3)
address.grid(row=2, column=1)

city = Entry(root, width=50, borderwidth=3)
city.grid(row=3, column=1)

state = Entry(root, width=50, borderwidth=3)
state.grid(row=4, column=1)

pincode = Entry(root, width=50, borderwidth=3)
pincode.grid(row=5, column=1)

manage_ID = Entry(root, width=50, borderwidth=3)
manage_ID.grid(row=7, column=1)

# create labels
lbl1 = Label(root, text="First name")
lbl1.grid(row=0, column=0, pady=(10, 0))

lbl2 = Label(root, text="Last name")
lbl2.grid(row=1, column=0)

lbl3 = Label(root, text="Address")
lbl3.grid(row=2, column=0)

lbl4 = Label(root, text="City")
lbl4.grid(row=3, column=0)

lbl5 = Label(root, text="State")
lbl5.grid(row=4, column=0)

lbl6 = Label(root, text="Pincode")
lbl6.grid(row=5, column=0)

manage_lbl = Label(root, text="Manage ID")
manage_lbl.grid(row=7, column=0)

# create confirmation button
btn1 = Button(root, text="Add Record in Database", command=submit)
btn1.grid(row=6, column=0, columnspan=2, pady=10, ipadx=110)

btn2 = Button(root, text="Show records", command=query)
btn2.grid(row=10, column=0, columnspan=2, pady=10, ipadx=138)

del_btn = Button(root, text="Delete", command=delete)
del_btn.grid(row=9, column=0, columnspan=2, ipadx=157, pady=10)

edit_btn = Button(root, text="Edit record", command=edit)
edit_btn.grid(row=8, column=0, columnspan=2, pady=10, ipadx=145)

# commit changes
conn.commit()

# close connection
conn.close()

mainloop()
