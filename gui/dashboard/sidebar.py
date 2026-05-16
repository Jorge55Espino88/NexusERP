import customtkinter as ctk

# --- STYLES ---
from gui.styles.colors import BG_CARD, ACCENT_MAIN


class SideBar(ctk.CTkFrame):
    def __init__(self, parent=None):
        # Frame vertical, pegado a la izquierda
        super().__init__(parent, fg_color=BG_CARD, corner_radius=0, width=200)
        self.pack_propagate(False)  # Evita que el frame se encoja al meterle botones

        # Etiquetas de la selección
        self.label = ctk.CTkLabel(self,
                                  text="Modules",
                                  text_color=ACCENT_MAIN,
                                  font=("Segoe UI", 14, "bold"))
        self.label.pack(padx=10, pady=20, anchor="w")

        # Aquí meteremos los botones tácticos en el siguiente movimiento...
