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
    
    def obtenerVentaPorId(self, id_venta):
        headers = { 'Authorization' : LectorToken.obtenerToken()}
        req     = requests.get(f'http://localhost:4000/sales/{id_venta}', headers=headers)

        ventas  = json.loads(req.text)
        return ventas


    
