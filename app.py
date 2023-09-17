import customtkinter as ctk
from PIL import Image
from notepad import Note


class NoteBook:
    def __init__(self):
        '''initially create button -> add note & add label'''
        img = ctk.CTkImage(light_image=Image.open(
            "Images/add.png"), size=(30, 30))
        btn = ctk.CTkButton(navFrame, image=img, text="New Note", fg_color="#222", hover_color="#333", font=(
            "Arial", 18, "bold"), width=200, height=50, text_color="#aaa", corner_radius=50, command=self.newNote)
        btn.pack(pady=5)

        # label
        ctk.CTkLabel(navFrame, text="Labels", text_color="#aaa").pack()
        img_lbl = ctk.CTkImage(light_image=Image.open(
            "Images/add2.png"), size=(20, 20))
        btn = ctk.CTkButton(navFrame, image=img_lbl, text="Add Label", fg_color="#222", hover_color="#333", font=(
            "Arial", 14, "bold"), text_color="#aaa", height=50, width=200, corner_radius=50, command=self.labelTitle)
        btn.pack()
        
    def button(self, path: str,name: str, cmd):
        img = ctk.CTkImage(light_image=Image.open(path), size=(30,30))
        btn = ctk.CTkButton(navFrame, image=img, text=name, fg_color="#222", hover_color="#333", font=(
            "Arial", 18, "bold"), width=200,height=50, text_color="#aaa", corner_radius=50, command=cmd)
        btn.pack(pady=5)
        

    def newNote(self):
        note = Note()
        note.mainloop()

    def labelTitle(self):
        '''this method call the addLabel method and give title of label'''
        dialog = ctk.CTkInputDialog(text="Label Name...", title='New Label', )
        title = dialog.get_input()

        if title == '':
            title = "New-1"

        self.addLabel(title)

    def addLabel(self, title):
        img = ctk.CTkImage(light_image=Image.open(
            "Images/label.png"), size=(40, 30))
        btn = ctk.CTkButton(navFrame, image=img, fg_color="#222", hover_color="#444", corner_radius=50, text=title,
                            command=self.labelTitle, height=25, width=200, font=("Arial", 16, "italic"), text_color="#aaa")
        btn.pack()

    


root = ctk.CTk()
root._set_appearance_mode('dark')
root.geometry('900x400')
root.title("MyNotes")


# Sidebar nav frame
navFrame = ctk.CTkScrollableFrame(
    root, fg_color='#222', scrollbar_button_color="#444")
navFrame.pack(side="left", fill="y")


if __name__ == '__main__':
    NoteBook()
    root.mainloop()
