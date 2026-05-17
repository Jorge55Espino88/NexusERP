# gui/dashboard/main_dashboard.py
import customtkinter as ctk

from gui.dashboard.center_panel import CenterPanel
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

        # Configuramos el contenedor derecho con GRID para control absoluto
        self.right_container.grid_columnconfigure(0, weight=1)
        self.right_container.grid_rowconfigure(1, weight=1)  # El lienzo de abajo se expande

        # 3. Montamos la Barra Superior (Topbar) - Fila 0
        self.topbar = Topbar(self.right_container, username, role)
        self.topbar.grid(row=0, column=0, sticky="ew")

        # 4. El Lienzo Central Dinámico (Main Content) - Fila 1
        self.main_content = ctk.CTkFrame(self.right_container, fg_color=BG_DARK, corner_radius=0)
        self.main_content.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        # 5. Acoplamos el panel de la tabla dentro del lienzo
        self.center_panel = CenterPanel(self.main_content)
        self.center_panel.pack(fill="both", expand=True)
