import requests
import json
import os
import LectorToken

class ClienteController():

    def obtenerClientes(self):
        headers = {
            'Authorization' : LectorToken.obtenerToken()
        }
        req           = requests.get('http://localhost:4000/customer/all', headers=headers)

        clientesJson  = json.loads(req.text)
        return clientesJson