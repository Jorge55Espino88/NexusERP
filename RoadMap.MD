🗺️ Roadmap de Nexus ERP
Filosofía: Simplicidad, Estructura y Modularidad.

📍 Fase 0: El ADN del Sistema (Cimientos)
Objetivo: Definir la estética y las piezas básicas.

[ ] Configuración Global: Crear carpeta NexusERP/ y archivos main.py.

[ ] CSS Python: Archivo gui/styles/colors.py con la paleta oficial.

[ ] Átomos UI: Creación de componentes base (PrimaryButton, CustomEntry).

[ ] Sistema de Alertas: Componente visual para notificaciones (NotificationToast).

🔑 Fase 1: Control de Acceso (Login & Seguridad)
Objetivo: Crear la "puerta de entrada" segura.

[ ] Vista de Login: Interfaz limpia con customtkinter.

[ ] Servicio de Autenticación: Lógica para validar usuarios (usando un JSON local inicial).

[ ] Gestión de Sesión: El sistema debe "recordar" quién entró.

[ ] Alertas de Seguridad: Notificaciones de "Acceso Denegado" o "Bienvenido".

🌐 Fase 2: Conexión al Mundo (API & Datos)
Objetivo: Consumir datos reales de internet.

[ ] API Client: Crear el motor que se conecta al JSON en línea.

[ ] Data Mapper: Limpiar y transformar los datos de la API (nombres, salarios, etc.).

[ ] Tabla de Personas: Implementar la visualización usando el DataTable heredado.

[ ] Integración de Alertas: Notificar cuando los datos se están cargando o si falló el internet.

🛠️ Fase 3: Gestión y Roles (CRUD de Personas)
Objetivo: Manipular la información según el usuario.

[ ] Lógica CRUD: Crear funciones para Agregar, Editar y Eliminar personas.

[ ] Sistema de Roles: Diferenciar qué puede hacer un "Admin" vs un "Usuario".

[ ] Buscador Reactivo: Filtrar la tabla en tiempo real mientras escribes.

📊 Fase 4: Reportes y Exportación
Objetivo: Darle valor a los datos.

[ ] Motor de Excel: Conectar el excel_engine.py para exportar la lista de personas.

[ ] Motor de PDF: Generar reportes visuales con formato profesional.

[ ] Footer de Acciones: Conectar los botones del footer con la lógica de la tabla.

🚦 ¿Cómo leer este mapa?
Nunca saltamos de fase si la anterior tiene cuadros [ ] sin marcar.

Si un archivo se vuelve muy largo, se divide inmediatamente.

Cada vez que terminemos una sesión, marcamos nuestro progreso con una [x].