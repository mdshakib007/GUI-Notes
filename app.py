from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk


class NewNote:
    def __init__(self):
        img = Image.open("Images/plus.png")
        img = img.resize((50, 50))
        img = ImageTk.PhotoImage(image=img)
        btn = ctk.CTkButton(navFrame, image=img, text="New Note", fg_color="#222", hover_color="#333", font=("Arial", 18, "bold"), width=200, text_color="#aaa", command=self.newNote)
        btn.pack(pady=5)
        
        # label 
        ctk.CTkLabel(navFrame, text="Labels", text_color="#aaa").pack(pady=10, side='left')
        img_lbl = Image.open("Images/plus2.png")
        img_lbl = img_lbl.resize((20, 20))
        img_lbl = ImageTk.PhotoImage(image=img_lbl)
        btn = ctk.CTkButton(navFrame, image=img_lbl, text="Add Label", fg_color="#222", hover_color="#333", font=("Arial", 14, "bold"), text_color="#aaa", height=40, command=self.addLabel)
        btn.pack(pady=10, side='right')
        
    
    def newNote(self):
        print('note addee')

    def clk(self):
        print('success')
        
    def addLabel(self):
        img = Image.open("Images/label.png")
        img = img.resize((30, 30))
        img = ImageTk.PhotoImage(image=img)
        btn = ctk.CTkButton(navFrame,image=img, fg_color="#222", hover_color="#444", corner_radius=50, text="Label", command=root.destroy, height=35, width=200, font=("Arial", 18, "italic"), text_color="#aaa")
        btn.pack(padx=10, pady=20)
        
    


root = ctk.CTk()
root._set_appearance_mode('dark')
root.geometry('900x400')
root.title("MyNotes")


# Sidebar nav frame
navFrame = ctk.CTkScrollableFrame(root, fg_color='#222', scrollbar_button_color="#444")
navFrame.pack(side="left", fill="y")


nn = NewNote()


root.mainloop()
