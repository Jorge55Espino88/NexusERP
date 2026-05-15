import customtkinter as ctk

from gui.body.login_view import LoginView
# --- Estilos ---
from gui.styles.colors import BG_DARK

# --- Controller ---
from backend.back_controller import BackController

class NexusApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title="Nexus ERP - Acceso de Seguridad"
        self.geometry("450x550")
        self.configure(fg_color=BG_DARK)

        # Inicializamos el controlador
        self.controller = BackController()

        # Cargamos la vista
        self.login_screen = LoginView(self,self.controller)
        self.login_screen.pack(fill="both", expand=True)

if __name__ == '__main__':
    app = NexusApp()
    app.mainloop()