from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Database")

# create the database or connect to database
conn = sqlite3.connect("data.db")

# create cursor
c = conn.cursor()

# create a table to store the data
c.execute("""CREATE TABLE shubham (
         first_name text,
         last_name text,
         address text,
         city text,
         state text,
         pincode integer
         )""")

# commit changes
conn.commit()

# close connection
conn.close()
mainloop()
