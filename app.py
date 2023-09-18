import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os

# global variables
file_content = None
label_path = None
note_path = None
lbl_data = ".data/.labelList.txt"
note_data = ".data/.noteList.txt"


class NoteBook:
    def __init__(self):
        '''initially create button -> add note & add label'''
        self.mkdir(lbl_data) # to make initial files and dirs
        self.mkdir(note_data) # to make initial files and dirs
        
        self.button(navFrame, "Images/add.png", "New Note",
                    (30, 30), self.noteTitle)  # Add note
        self.button(navFrame, "Images/archive.png", "Archive\t",
                    (30, 30), self.archive)  # archive
        self.button(navFrame, "Images/delete.png",
                    "Trash\t", (30, 30), self.trash)  # trash
        self.button(navFrame, "Images/setting.png", "Settings\t",
                    (30, 30), self.settings)  # settings
        ctk.CTkLabel(navFrame, text="Labels",
                     text_color="#aaa", height=40).pack()  # label heading
        self.button(navFrame, "Images/add2.png", "Add Label",
                    (20, 20), self.labelTitle)  # label Button
        
    def mkdir(self, data_path):
        '''will make necesarry files and dirs'''
        if not os.path.exists(".data"):
            os.mkdir(".data")
            os.mkdir(".data/.notes")
        if not os.path.exists(data_path):
            with open(data_path, "w") as f:
                pass

    def button(self, window, path: str, name: str, imgSize: tuple, cmd):
        '''this is default button template'''
        img = ctk.CTkImage(light_image=Image.open(path), size=imgSize)
        btn = ctk.CTkButton(master=window, image=img, text=name, fg_color="#222", hover_color="#333", font=(
            "Arial", 18, "bold"), width=200, height=50, text_color="#aaa", corner_radius=50, command=cmd)
        btn.pack(pady=2)

    def labelTitle(self):
        '''this method call the addLabel method and give title of label'''
        dialog = ctk.CTkInputDialog(text="Label Name...", title='New Label', )
        title = dialog.get_input()

        if title == '':
            title = "New-1"

        self.addLabel(title, title, self.label)

    def addLabel(self, title, btnName, command):
        '''this function add the new label(directory) and make a file as name of directory'''
        global label_path

        # to make title like dir and txt file
        if not os.path.exists(f".data/.{title}"):
            os.mkdir(f".data/.{title}")
            with open(f".data/.{title}/.{title}.txt", "w") as f1:
                label_path = f".data/.{title}/.{title}.txt"
                f1.close()

            # labelList.txt for write all title to track next time
            with open(lbl_data, "r+") as f2:
                data = f2.read().split(",")
                if title in data:
                    pass
                else:
                    f2.write(f"{title},")
                    f2.close()


            self.button(navFrame, "Images/label.png",
                        btnName, (40, 30), command)

        else:
            label_path = f".data/.{title}/.{title}.txt"
            messagebox.showerror("error", "Label Alrady Exists.")
            

    def noteTitle(self):
        dialog = ctk.CTkInputDialog(text="Note Name...", title='New Note', )
        ttl = dialog.get_input()

        if ttl == '':
            ttl = "New Note - 1"
        
        self.addNote(ttl)
        
        # call the Note class to get top-label
        new_note = Note(ttl, note_path)
        

        
    def addNote(self, title):
        '''this function add the new label(directory) and make a file as name of directory'''
        global note_path, file_content
        # to make title like dir and txt file
        if not os.path.exists(f".data/.notes/.{title}.txt"):
            with open(f".data/.notes/.{title}.txt", "w") as f1:
                note_path = f".data/.notes/.{title}.txt"
                f1.close()

            # labelList.txt for write all title to track next time
            with open(note_data, "r+") as f2:
                data = f2.read().split(",")
                if title in data:
                    pass
                else:
                    f2.write(f"{title},")
                    f2.close()
            file_content = None

        else:
            note_path = f".data/.notes/.{title}.txt"
            
            # if note alrady exists, then we need file content and write in top-label
            with open(note_path, "r") as f3:
                file_content = f3.read()
                f3.close()
        
    
    def displayNotes(self):
        pass


    def settings(self):
        pass

    def trash(self):
        pass

    def archive(self):
        pass

    def label(self):
        '''This is universal Label function'''
        global label_path
        print('label called')
        
        
    


class Note(ctk.CTkToplevel):
    def __init__(self, ttl, filePath):
        super().__init__()
        self.filePath = filePath
        self.title(f"{ttl} - MyNotes")
        self.geometry('800x500')
        self._set_appearance_mode('dark')
        

        self.noteFrame = ctk.CTkFrame(self, fg_color="#222")
        self.noteFrame.pack(fill='y', side='left')

        self.font_size = 18
        self.textArea = ctk.CTkTextbox(
            self, font=("Arial", self.font_size), undo=True)
        self.textArea.pack(fill='both', expand=True)
        
        # add content in text area, if the file exists and any content exists
        if file_content is not None:
            self.textArea.insert(1.0, text=file_content)

        # make save and delete button
        undoBtn = self.button(
            self.noteFrame, "Images/undo.png", "Undo\t", (40, 40), self.undo)
        redoBtn = self.button(
            self.noteFrame, "Images/redo.png", "Redo\t", (40, 40), self.redo)
        saveBtn = self.button(
            self.noteFrame, "Images/add2.png", "Save\t", (30, 30), self.save)
        clrBtn = self.button(
            self.noteFrame, "Images/eraser.png", "Clear\t", (30, 30), self.clear)
        zoomIn = self.button(
            self.noteFrame, "Images/zoom-in.png", "Zoom In\t", (20, 20), self.zoomIn)
        zoomIn = self.button(
            self.noteFrame, "Images/zoom-out.png", "Zoom Out", (20, 20), self.zoomOut)
        helpBtn = self.button(
            self.noteFrame, "Images/help.png", "Help\t", (30, 30), self.help)
        closeBtn = self.button(
            self.noteFrame, "Images/close.png", "Close\t", (30, 30), self.exit)

    def button(self, window, path: str, name: str, imgSize: tuple, cmd):
        '''this is default button template'''
        img = ctk.CTkImage(light_image=Image.open(path), size=imgSize)
        btn = ctk.CTkButton(master=window, image=img, text=name, fg_color="#222", hover_color="#333", font=(
            "Arial", 18, "bold"), width=200, height=50, text_color="#aaa", corner_radius=50, command=cmd)
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
        '''simply open a file and save the file as txt file'''
        with open(self.filePath, "a+") as f:
            content = self.textArea.get(1.0, 'end')
            f.write(content)
            f.close()
            
            self.lift()
            messagebox.showinfo("Saved", "Successfully Saved Changes.", parent=self)

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

    def exit(self):
        self.lift()
        msg = messagebox.askokcancel(
            "Exit", "Confirm to Exit?", parent=self)
        if msg is True:
            self.destroy()
        else:
            pass


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
