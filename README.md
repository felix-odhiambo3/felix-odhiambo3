from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("hospital management system")
        self.root.geometry("1540x800+0+0")
        
        
        lbbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbbltitle.pack(side=TOP, fill=X)
        
        
        #========================================Dataframe===============================================
        Dataframe=Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0,y=130, width=1530, height=400)
        
        DataframeLeft = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE,
                                                font=("arial", 12, "bold"), text="Patient Information")
        
        DataframeLeft.place(x=0, y=5, width=980, height=350)
        
        DataframeRight = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE,
                                                font=("arial", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)
        
       
         # =======================Button frame============================================================
        Detailsframe=Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0,y=530, width=1530, height=70)
        
        
        
        
        
        
         # =======================Details frame============================================================
        Buttonframe=Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0,y=530, width=1530, height=70)
        
        
        
        
        
        
root=Tk()
ob = Hospital(root)
root.mainloop()
