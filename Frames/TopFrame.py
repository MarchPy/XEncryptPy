from tkinter.ttk import Frame, Label, Entry, Button, LabelFrame
from tkinter import END
from CoreProgram.CoreProgram import Core
from Frames.BottomFrame import BottomFrame


class TopFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.__create_widgets()
        
    def __create_widgets(self):
        def set_path():
            path_file = Core(open_dialog=True)
            path_box.delete(0, END)
            path_box.insert(0, path_file.return_path())

            BottomFrame.PATH = path_box.get()
            
        lbf_select_file = LabelFrame(self, text="Selecione o arquivo")
        lbf_select_file.grid(
            row=0, 
            column=0,
            padx=5,
            pady=5,
        )
        
        Label(lbf_select_file, text="Caminho do arquivo: ").grid(row=0, column=0)
        path_box = Entry(lbf_select_file, width=35)
        path_box.grid(
            row=0,
            column=1,
        )
        
        button_select = Button(lbf_select_file, text="Selecionar", command=set_path)
        button_select.grid(
            row=0,
            column=2,
        )
