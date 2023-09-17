import customtkinter as ctk 

class Note(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("New Note - 1")
        self.geometry('800x500')
        self._set_appearance_mode('dark')
        
        mainMenu = ctk.CTkOptionMenu(self, values=['one', 'two', 'three', 'four'])
        mainMenu.pack()
        
        textArea = ctk.CTkTextbox(self, font=("Arial", 20))
        textArea.pack(fill='both', expand=True)
        
        
        
        
        

if __name__=='__main__':
    n = Note()
    n.mainloop()