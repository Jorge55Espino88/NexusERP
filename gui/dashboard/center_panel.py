import customtkinter as ctk

# --- ESTILOS ---
from gui.styles.colors import BG_DARK, BG_CARD, TEXT_HIGH, TEXT_LOW, SUCCESS, WARNING


class CenterPanel(ctk.CTkFrame):
    def __init__(self, parent=None, ):
        super().__init__(parent, fg_color=BG_DARK, corner_radius=0)

        # Estructura base para el panel de datos
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # 1. Encabezado de la sección
        self.header_label = ctk.CTkLabel(
            self,
            text="EMPLOYEE REGISTRATION",
            text_color=TEXT_HIGH,
            font=("Segoe UI", 16, "bold")
        )
        self.header_label.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 10))

        # 2. Contenedor de la Tabla
        self.table_container = ctk.CTkFrame(self, fg_color=BG_CARD, corner_radius=0)
        self.table_container.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))

        # Columna única para que las filas se estiren a lo ancho
        self.table_container.grid_columnconfigure(0, weight=1)

    def populate_table(self, employees_data):
        """Limpiar el contenedor e inyectar las filas de personal de manera estilizada usando la paleta oficial de Nexus ERP."""

        # Limpiamos cualquier residuo
        for widget in self.table_container.winfo_children():
            widget.destroy()

        if not employees_data:
            # Sin datos, la api falló
            no_data_label = ctk.CTkLabel(self.table_container, text="No records available or connection failed.",
                                         text_color=TEXT_LOW, font=("Segoe UI", 13, "italic"))
            no_data_label.grid(row=0, column=0, pady=50)
            return

        # Cabeceras de las columnas
        headers = ["ID", "NAME", "DEPARTMENT", "ROLE", "STATUS"]
        header_frame = ctk.CTkFrame(self.table_container, fg_color="transparent")
        header_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=10)

        for col_idx, text in enumerate(headers):
            header_frame.grid_columnconfigure(col_idx, weight=1)
            lbl = ctk.CTkLabel(header_frame, text=text, font=("Segoe UI", 11, "bold"), text_color=TEXT_LOW)
            lbl.grid(row=0, column=col_idx, sticky="w")

        # Inyección de las filas dinámicas
        for row_idx, emp in enumerate(employees_data, start=1):
            # Filas con el fondo de la ventana para generar un contraste elegante sobre la tarjeta
            row_frame = ctk.CTkFrame(self.table_container, fg_color=BG_DARK, height=38, corner_radius=6)
            row_frame.grid(row=row_idx, column=0, sticky="ew", padx=10, pady=4)
            row_frame.grid_propagate(False)  # Forzar el alto estricto

            # Configuramos 5 columnas con pesos idénticos para alineación matemática
            for c in range(5):
                row_frame.grid_columnconfigure(c, weight=1)

                # Celdas de datos inyectadas de forma milimétrica por columna
                ctk.CTkLabel(row_frame, text=emp["id"], font=("Segoe UI", 12), text_color=TEXT_LOW).grid(row=0,column=0,sticky="w",padx=15,pady=5)
                ctk.CTkLabel(row_frame, text=emp["name"], font=("Segoe UI", 12, "bold"), text_color=TEXT_HIGH).grid(row=0, column=1, sticky="w", pady=5)
                ctk.CTkLabel(row_frame, text=emp["department"].upper(), font=("Segoe UI", 11),text_color=TEXT_LOW).grid(row=0, column=2, sticky="w", pady=5)
                ctk.CTkLabel(row_frame, text=emp["role"].upper(), font=("Segoe UI", 11), text_color=TEXT_LOW).grid(row=0, column=3, sticky="w", pady=5)

                # Badge de estado
                status_color = SUCCESS if emp["status"] == "Active" else WARNING
                lbl_status = ctk.CTkLabel(row_frame, text=emp["status"].upper(), font=("Segoe UI", 10, "bold"),text_color=status_color)
                lbl_status.grid(row=0, column=4, sticky="w", pady=5)
