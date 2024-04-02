#for when entering the password. hashing will encrypt the password in the sql database
import hashlib

#for file paths
import os

#imports sqlite3, which will be used to create a sql database
import sqlite3

#imports all of the required tkinter libraries
from tkinter import *
root = Tk()
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

# creates the tk gui
root.geometry()
root.geometry("510x1020")
root.title("Choose")

#function that will open up the sign in page
def openSignUpPage():
  root.destroy()
  import signup


#function that will open up the log in page
def openLogInPage():
  root.destroy()
  import login

#creates a login button and sets up their location. The login button runs a function to open up the login screen.
login_button = Button(root, text="Login", command=openLogInPage)
login_button.grid(row=0,column=0)
#creates a signup button and sets up their location. The signup button runs a function to open up the signup screen.
signup_button = Button(root, text="Create Account", command=openSignUpPage)
signup_button.grid(row=1,column=0)
#creates an exit button that will destroy the gui. This will end the program.
enter_button = Button(root, text="Exit", command=root.destroy)
enter_button.grid(row=2,column=0)

# sets up the actual sqlite databse as login.db
database = sqlite3.connect('login.db')

# creates the cursor object which is importing in interacting with the database.
cursor = database.cursor()

# create the database with the different columns required. This is only if the database doesn't exist.
cursor.execute(''' CREATE TABLE IF NOT EXISTS logindata
       (userid     INTEGER PRIMARY KEY, 
       username TEXT,
       password TEXT,
       first_name TEXT,
       last_name TEXT)
       ''')

#applies all changes to the database
database.commit()

# keeps the gui from disappearing/keeps it on screen
root.mainloop()
