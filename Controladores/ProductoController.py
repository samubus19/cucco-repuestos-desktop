import LectorToken
import requests
import json 

token = LectorToken.obtenerToken()
class ProductoController():

    def __init__(self) -> None:
        pass

    def obtenerProductos(self):
        headers = { 'Authorization' : token}
        req     = requests.get('http://localhost:4000/products/all', headers=headers)

        productosJson = json.loads(req.text)
        return productosJson

    def agregarProducto(self, nombre, stock, descripcion, precio_venta, precio_compra, marca, imagen):
        my_headers = {
            'Authorization' : token
        }
        body       = {
            'nombre'        : nombre,
            'stock'         : stock,
            'descripcion'   : descripcion,
            'precio_venta'  : precio_venta,
            'precio_compra' : precio_compra,
            'marca'         : marca,
        }
        files = {
            'imagen' : open(imagen, 'rb'),
        }
        requests.post('http://localhost:4000/products/new', headers=my_headers, data=body, files=files)

    def editarProducto(self):
        pass

    def borrarProducto(self):
        pass
