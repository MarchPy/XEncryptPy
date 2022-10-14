from tkinter.ttk import Frame, Radiobutton, Button, LabelFrame
from tkinter import Entry, IntVar, END, messagebox
from CoreProgram.CoreProgram import Core


class BottomFrame(Frame):
    PATH = ""

    def __init__(self, root):
        super().__init__(root)
        self.__create_widgets()
        
    def __create_widgets(self):
        def use_key():
            if option.get() == 1:
                entry_key.grid(row=1, columnspan=3, padx=5)
                button_select_keyfile.grid(row=1, column=4)
                entry_key.delete(0, END)
                entry_key.insert(0, "<Selecione o arquivo key>")
            
            elif option.get() == 0:
                entry_key.grid_forget()
                button_select_keyfile.grid_forget()
        
        def run_program():
            core = Core(open_dialog=False)
            if self.PATH == "":
                messagebox.showerror("Erro", "Caminho para o arquivo inválido.")
            else:
                if option.get() == 0:
                    core.encrypt_file(path_file=self.PATH)

                elif option.get() == 1:
                    core.decrypt_file(path_file=self.PATH, private_key=entry_key.get())

        def set_keyfile():
            core = Core(open_dialog=True)
            entry_key.delete(0, END)
            entry_key.insert(0, core.return_path())

        lbf_config = LabelFrame(self, text="Configuração")
        lbf_config.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )
        
        option = IntVar()
        radio_button_encrypt = Radiobutton(lbf_config, text="Encriptar", value=0, variable=option, command=use_key)
        radio_button_encrypt.grid(
            row=0,
            column=0,
            sticky="W",
        )
        
        radio_button_decrypt = Radiobutton(lbf_config, text="Desencriptar", value=1, variable=option, command=use_key)
        radio_button_decrypt.grid(
            row=0,
            column=1,
            sticky="W",
        )

        entry_key = Entry(lbf_config, width=40)
        button_select_keyfile = Button(lbf_config, text="Selecionar", command=set_keyfile)
        
        button_execute = Button(lbf_config, text="Execute", width=30, command=run_program)
        button_execute.grid(
            row=2,
            columnspan=4,
            sticky="E"
        )
        
