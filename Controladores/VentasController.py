import LectorToken
import requests
import json 

class VentasController():

    def __init__(self) -> None:
        pass

    def obtenerVentas(self):
        headers = { 'Authorization' : LectorToken.obtenerToken()}
        req     = requests.get('http://localhost:4000/sales/all', headers=headers)

        ventas  = json.loads(req.text)
        return ventas


    
