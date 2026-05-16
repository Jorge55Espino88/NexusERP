import customtkinter as ctk

# --- STYLES ---
from gui.styles.colors import BG_CARD,TEXT_HIGH,TEXT_LOW

class Topbar(ctk.CTkFrame):
    def __init__(self, parent=None,username=None,role=None):
        super().__init__(parent,fg_color=BG_CARD,corner_radius=0,width=60)
        self.pack_propagate(False)

        # Saludo al operador en el lado izquierdo
        self.welcome_label=ctk.CTkLabel(self,
                                        text=f"Account: {username.upper()}",
                                        text_color=TEXT_HIGH,
                                        font=("Segoe UI", 14, "bold"))
        self.welcome_label.pack(side="left", pady=20, padx=15)

        # Rol o Rango estilizado en el extremo derecho
        self.role_label = ctk.CTkLabel(
            self, text=f"Access: {role.upper()}", text_color=TEXT_LOW,
            font=("Segoe UI", 12, "italic")
        )
        self.role_label.pack(side="right", pady=20, padx=15)



