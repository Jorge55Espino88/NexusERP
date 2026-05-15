import customtkinter as ctk
from gui.styles.colors import ACCENT_MAIN, ACCENT_HOVER, TEXT_HIGH, BG_DARK


class PrimaryButton(ctk.CTkButton):
    def __init__(self,master,text,command=None,**kwargs):
        super().__init__(
            master,  #Padre, en custom se le suele llamar asi
            text=text,
            command=command,
            fg_color=ACCENT_MAIN,
            hover_color=ACCENT_HOVER,
            text_color=BG_DARK,
            font=("Segoe UI",13,"bold"),
            corner_radius=8,
            height=35,
            **kwargs
        )