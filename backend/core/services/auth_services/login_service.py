class LoginService:
    def __init__(self):
        # Base de datos temporal para pruebas
        self._users = {"admin": "1234","jorge":"nexus2026"}

    def validate_credentials(self,user,password):
        if user in self._users and password == self._users[user]:
            return {"success":True,"role":"superadmin"}
        return {"success":False,"message":"Denied Access"}
