from backend.core.services.auth_services.login_service import LoginService
class BackController:
    def __init__(self):
        self.login_svc=LoginService()

    def handle_login(self, username, password):
        return self.login_svc.validate_credentials(username,password)
