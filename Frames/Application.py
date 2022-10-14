from tkinter import Tk, PhotoImage
from Frames.TopFrame import TopFrame
from Frames.BottomFrame import BottomFrame


class Application(Tk):
    def __init__(self, name_program, version):
        super().__init__()
        self.iconphoto(False, PhotoImage(file="images/icone.png"))
        self.title(f"{name_program} {version}")
        self.resizable(False, False)
        self.__create_widgets()

    def __create_widgets(self):
        main_frame = TopFrame(self)
        main_frame.grid(
            row=0,
            column=0,
            sticky="W",
        )
        
        main_config = BottomFrame(self)
        main_config.grid(
            row=1,
            column=0,
            sticky="N",
        )
    