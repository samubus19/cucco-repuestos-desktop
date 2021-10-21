from dataclasses import dataclass

@dataclass
class Producto():
    nombre        : str
    stock         : int
    descripcion   : str
    precio_venta  : float
    precio_compra : float
    marca         : str
