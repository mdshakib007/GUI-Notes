import customtkinter as ctk 

class Note(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("New Note - 1")
        self.geometry('800x500')
        self._set_appearance_mode('dark')
        
        textArea = ctk.CTkTextbox(self, font=("Arial", 20))
        textArea.pack(fill='both', expand=True)
        
        mainMenu = ctk.CTkOptionMenu(self)
        
        fileMenu = ctk.CTkOptionMenu(mainMenu,)
        
        
        

if __name__=='__main__':
    n = Note()
    n.mainloop()