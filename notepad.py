import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

class Note(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("New Note - 1")
        self.geometry('800x500')
        self._set_appearance_mode('dark')
        
        self.noteFrame = ctk.CTkFrame(self, fg_color="#222")
        self.noteFrame.pack(fill='y', side='left')
        
        self.font_size = 18
        self.textArea = ctk.CTkTextbox(self, font=("Arial", self.font_size), undo=True)
        self.textArea.pack(fill='both', expand=True)
        
        # make save and delete button
        undoBtn = self.button(self.noteFrame, "Images/undo.png", "Undo", (40, 40), self.undo)
        redoBtn = self.button(self.noteFrame, "Images/redo.png", "Redo", (40, 40), self.redo)
        saveBtn = self.button(self.noteFrame, "Images/add2.png", "Save", (30, 30), self.save)
        clrBtn = self.button(self.noteFrame, "Images/eraser.png", "Clear", (30, 30), self.clear)
        zoomIn = self.button(self.noteFrame, "Images/zoom-in.png", "Zoom In", (20, 20), self.zoomIn)
        zoomIn = self.button(self.noteFrame, "Images/zoom-out.png", "Zoom Out", (20, 20), self.zoomOut)
        helpBtn = self.button(self.noteFrame, "Images/help.png", "Help", (30, 30), self.help)
        closeBtn = self.button(self.noteFrame, "Images/close.png", "Close", (30, 30), self.destroy)
        
       
    def button(self,window, path: str,name: str, imgSize: tuple, cmd):
        '''this is default button template'''
        img = ctk.CTkImage(light_image=Image.open(path), size=imgSize)
        btn = ctk.CTkButton(master=window, image=img, text=name, fg_color="#222", hover_color="#333", font=(
            "Arial", 18, "bold"), width=200,height=50, text_color="#aaa", corner_radius=50, command=cmd)
        btn.pack(pady=5)
        
    
    def undo(self, *args):
        try:
            self.textArea.edit_undo()
        except:
            pass
    
    def redo(self, *args):
        try:
            self.textArea.edit_redo()
        except:
            pass
    
    def save(self):
        pass
    
    def clear(self):
        '''this function just erase all text from self.textArea'''
        content = self.textArea.get(1.0, "end")
        if content != '\n':
            self.lift()
            save_change = messagebox.askquestion(
                'Save Change', 'Do you want to save change?', parent=self)

            if save_change == 'yes':
                self.save()
            self.textArea.delete(1.0, "end")
    
    def help(self):
        pass
    
    def zoomIn(self):
        self.font_size = self.font_size + 2
        self.textArea.configure(font=("Arial", self.font_size))
    
    def zoomOut(self):
        self.font_size = self.font_size - 2
        self.textArea.configure(font=("Arial", self.font_size))
        


if __name__=='__main__':
    n = Note()
    n.mainloop()