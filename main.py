import customtkinter as ctk

from gui import dashboard
from gui.body.login_view import LoginView
from gui.dashboard.main_dashboard import MainDashboard
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
        "Misión: Registrar sesión, destruir login y levantar el Dashboard de Gala"
        self.current_user = user
        self.current_role = role

        # 1. Destruimos el login
        self.login_screen.destroy()

        # 2. Configuramos dimensiones profesionales
        self.geometry("1024x600")
        self.title(f"Nexus ERP - Panel Principal [{self.current_user.upper()}]")

        # 3. Lanzamos el Dashboard Maestro pasándole los datos del operador
        self.dashboard = MainDashboard(self, self.current_user, self.current_role)
        self.dashboard.pack(fill="both", expand=True)

        print(f"🚀 [SISTEMA]: Dashboard principal desplegado con éxito.")

        # === SIMULACRO DE OPERACIONES DE RED (TEMPORAL) ===
        from network.api_client import APIClient
        from core.data_mapper import DataMapper

        # 1. Instanciamos el cliente y traemos los datos de tu GitHub
        client = APIClient()
        response = client.fetch_records()

        # 2. Pasamos los datos por la aduana del Mapper
        console_data = DataMapper.map_employees(response)
        # Inyectamos la lista limpia en el panel central
        self.dashboard.center_panel.populate_table(console_data)

if __name__ == '__main__':
    app = NexusApp()
    app.mainloop()