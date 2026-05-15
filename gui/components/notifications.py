import customtkinter as ctk
from gui.styles.colors import ACCENT_MAIN


class NotificationToast(ctk.CTkFrame):
    def __init__(self, parent, text, is_success=True):
        # Si es éxito usamos cian/azul, si es error podemos usar un tono rojizo o el texto de alerta
        bg_color = "#2b2b2b"
        border_color = ACCENT_MAIN if is_success else "#ff5555"

        super().__init__(parent, fg_color=bg_color, border_color=border_color, border_width=2, corner_radius=10)

        # Icono o prefijo visual
        prefix = "✅ " if is_success else "❌ "

        self.label = ctk.CTkLabel(
            self,
            text=prefix + text,
            text_color="#ffffff",
            font=("Segoe UI", 12, "bold")
        )
        self.label.pack(padx=20, pady=10)