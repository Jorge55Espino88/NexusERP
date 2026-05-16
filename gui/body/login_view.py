# gui/body/login_view.py
import customtkinter as ctk

from gui.components.notifications import NotificationToast
from gui.styles.colors import BG_CARD, ACCENT_MAIN, TEXT_HIGH, TEXT_LOW, BG_DARK
from gui.components.buttons import PrimaryButton
# 🛡️ TRUCO MAESTRO: Importación condicional para evitar el bucle circular
# Esto solo lo lee PyCharm para el autocompletado, Python lo ignora en ejecución.
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import NexusApp


class LoginView(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        # Usamos los colores de nuestra Fase 0
        super().__init__(parent, fg_color=BG_CARD, corner_radius=15)
        self.controller = controller  # Guardamos el enlace al cerebro (BackController)
        self.master:"NexusApp" = parent

        # --- Interfaz Visual ---
        self.title_label = ctk.CTkLabel(
            self, text="NEXUS ERP", text_color=ACCENT_MAIN,
            font=("Segoe UI", 24, "bold")
        )
        self.title_label.pack(pady=(30, 10))

        self.subtitle_label = ctk.CTkLabel(
            self, text="Seguridad de Acceso", text_color=TEXT_LOW,
            font=("Segoe UI", 12)
        )
        self.subtitle_label.pack(pady=(0, 30))

        # Campos de entrada
        self.username_entry = ctk.CTkEntry(
            self, placeholder_text="Usuario", width=280, height=40, border_color=ACCENT_MAIN
        )
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self, placeholder_text="Contraseña", show="*", width=280, height=40, border_color=ACCENT_MAIN
        )
        self.password_entry.pack(pady=10)

        # Nuestro botón personalizado de la Fase 0
        self.login_button = PrimaryButton(
            self, text="ENTRAR", width=280, command=self._on_login_click
        )
        self.login_button.pack(pady=(30, 40))

    def _on_login_click(self):
        """Misión: Extraer datos y enviarlos al controlador"""
        user = self.username_entry.get()
        password = self.password_entry.get()

        # Le pedimos al controlador que valide
        respuesta = self.controller.handle_login(user, password)

        if respuesta["success"]:
            print(f"✅ [SISTEMA]: Acceso concedido para {user}. Rol: {respuesta['role']}")
            self.master.login_system(user,respuesta["role"])
        else:
            print(f"❌ [ALERTA]: {respuesta['message']}")
            alerta = NotificationToast(self, text=respuesta["message"], is_success=False)
            alerta.place(relx=0.5, rely=0.85, anchor="center")

# cuando veas algo con on al principio, es como un listener. es como la bala que se dispara cuando el gatillo se aprieta