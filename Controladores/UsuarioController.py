import requests
import json
import os
from Vistas import MenuPrincipal
import LectorToken
class UsuarioController():

    def iniciarSesion(self, usuario, contrasenia, email):
        body = {'usuario' : usuario, 'contrasenia' : contrasenia, 'email' : email}
        req  = requests.post('http://localhost:4000/user/login', data=body)

        if(req.status_code == 200):
            with open(os.path.join(os.getcwd(), 'token.json'), 'w') as archivo:
                json.dump(json.loads(req.text), archivo , indent=4)
            # print(os.getcwd())

            menu = MenuPrincipal.MenuPrincipal()
        else:
            print('Datos incorrectos')        

    def obtenerUsuarios(self):
        headers = {
            'Authorization' : LectorToken.obtenerToken()
        }
        req           = requests.get('http://localhost:4000/user/all', headers=headers)

        usuariosJson  = json.loads(req.text)
        return usuariosJson