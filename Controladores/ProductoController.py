import LectorToken
import requests
import json 

class ProductoController():

    def __init__(self) -> None:
        pass

    def obtenerProductos(self):
        headers = { 'Authorization' : LectorToken.obtenerToken()}
        req     = requests.get('http://localhost:4000/products/all', headers=headers)

        productosJson = json.loads(req.text)
        return productosJson

    def agregarProducto(self):
        pass

    def editarProducto(self):
        pass

    def borrarProducto(self):
        pass
