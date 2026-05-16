class DataMapper:
    @staticmethod
    def map_employees(api_response):
        """Misión: Tomar la respuesta cruda de la API, filtrar la grasa and retornar una lista limpia de diccionarios estandarizados."""

        # Si la petición falló, retornamos una lista vacía para no romper la app
        if not api_response.get("success"):
            return []

        raw_data = api_response.get("data",{})
        employees_list = raw_data.get("employees",[])

        clean_list = []
        for employee in employees_list:
            map_employee = {
                "id": employee.get("id","N/A"),
                "name": employee.get("name","Unknown"),
                "role": employee.get("role","No Role"),
                "department": employee.get("department","General"),
                "status": employee.get("status","Inactive")
            }
            clean_list.append(map_employee)

        print(f"📊 [MAPPER]: Procesados {len(clean_list)} registros de personal con éxito.")
        return clean_list
