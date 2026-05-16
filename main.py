import customtkinter as ctk

from gui.body.login_view import LoginView
# --- Estilos ---
from gui.styles.colors import BG_DARK

# --- Controller ---
from backend.back_controller import BackController

class NexusApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Nexus ERP - Acceso de Seguridad")
        self.geometry("450x550")
        self.configure(fg_color=BG_DARK)

        # Inicializamos el controlador
        self.controller = BackController()

        # Datos de la sesión activa
        self.current_user = None
        self.current_role = None

        # Lanzamos el Inicio
        self.show_login()

    def show_login(self):
        "Despliega la pantalla de login"
        self.login_screen = LoginView(self,self.controller)
        self.login_screen.place(relx=0.5,rely=0.5,anchor="center")

    def login_system(self, user, role):
        "Misión: Registrar sesión, destruir login y expandir pantalla"
        self.current_user = user
        self.current_role = role

        # 1. Limpieza de pantalla: Eliminamos el contenedor de login
        self.login_screen.destroy()

        # 2. Reconfiguramos la ventana para el modo "Dashboard" (Más amplia)
        self.geometry("1024x600")

        # CORRECCIÓN AQUÍ: Usamos paréntesis () en lugar de =
        self.title(f"Nexus ERP - Panel Principal [{self.current_user.upper()}]")

        # 3. Alerta táctica de control
        print(f"🚀 [SESIÓN INICIADA]: {self.current_user} ha tomado el control con el rol: {self.current_role}")

if __name__ == '__main__':
    app = NexusApp()
    app.mainloop()