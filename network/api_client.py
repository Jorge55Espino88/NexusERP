# network/api_client.py
import urllib.request
import json


class APIClient:
    def __init__(self):
        # URL de pruebas remota con datos simulados de personal y ERP
        self.base_url = "https://raw.githubusercontent.com/Jorge55Espino88/NexusERP/main/mock_data.json"

    def fetch_records(self):
        """Misión: Salir a internet, descargar el JSON y reportar los datos crudos"""
        print("📡 [RED]: Iniciando petición al servidor central...")
        try:
            # Intentamos abrir la conexión con la URL externa
            with urllib.request.urlopen(self.base_url, timeout=5) as response:
                if response.status == 200:
                    # Leemos los bytes crudos y los transformamos en un diccionario de Python
                    data_cruda = json.loads(response.read().decode())
                    print("✅ [RED]: Datos descargados con éxito.")
                    return {"success": True, "data": data_cruda}

                return {"success": False, "message": f"Error de servidor: Código {response.status}"}

        except Exception as e:
            # Si no hay internet o la URL falla, capturamos el error para que el sistema no explote
            print(f"❌ [RED ERROR]: Fallo en la conexión. Motivo: {e}")
            return {"success": False, "message": "No se pudo conectar al servidor. Verifique su red."}