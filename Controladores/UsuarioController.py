import requests
import json
import os
from Vistas import MenuPrincipal

class UsuarioController():

    def __init__(self, usuario, contrasenia, email) -> None:
        self.usuario     = usuario
        self.contrasenia = contrasenia
        self.email       = email

    def iniciarSesion(self):
        body = {'usuario' : self.usuario, 'contrasenia' : self.contrasenia, 'email' : self.email}
        req  = requests.post('http://localhost:4000/user/login', data=body)

        if(req.status_code == 200):
            with open(os.path.join(os.getcwd(), 'token.json'), 'w') as archivo:
                json.dump(json.loads(req.text), archivo , indent=4)
            # print(os.getcwd())

            menu = MenuPrincipal.MenuPrincipal()
        else:
            print('Datos incorrectos')        

    def registrarUsuario(self):
        pass