# gui/dashboard/main_dashboard.py
import customtkinter as ctk
from gui.dashboard.sidebar import SideBar
from gui.dashboard.topbar import Topbar
from gui.styles.colors import BG_DARK, BG_CARD


class MainDashboard(ctk.CTkFrame):
    def __init__(self, parent, username, role):
        # El contenedor maestro ocupa toda la ventana gigante
        super().__init__(parent, fg_color=BG_DARK, corner_radius=0)

        # 1. Montamos la Barra Lateral (Sidebar) - Izquierda
        self.sidebar = SideBar(self)
        self.sidebar.pack(side="left", fill="y")

        # 2. Contenedor Derecho (Alojará la Topbar y el Contenido Dinámico)
        self.right_container = ctk.CTkFrame(self, fg_color=BG_DARK, corner_radius=0)
        self.right_container.pack(side="right", fill="both", expand=True)

        # 3. Montamos la Barra Superior (Topbar) dentro del contenedor derecho
        self.topbar = Topbar(self.right_container, username, role)
        self.topbar.pack(side="top", fill="x")

        # 4. El Lienzo Central Dinámico (Main Content) - Aquí caerán las tablas modernas
        self.main_content = ctk.CTkFrame(
            self.right_container, fg_color=BG_DARK, corner_radius=0
        )
        self.main_content.pack(side="bottom", fill="both", expand=True, padx=20, pady=20)

        # Mensaje temporal de diseño en el lienzo central
        self.temp_label = ctk.CTkLabel(
            self.main_content,
            text="🚀 Centro de Operaciones Operativo\nEsperando despliegue de datos de la API...",
            text_color="#666666", font=("Segoe UI", 16, "italic")
        )
        self.temp_label.place(relx=0.5, rely=0.5, anchor="center")