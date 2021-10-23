import tkinter
from tkinter import ttk
from Controladores.ProductoController import *

class ListaProductos():
    def __init__(self) -> None:
        #CREACION VENTANA
        self.root = tkinter.Toplevel()
        self.root.resizable(tkinter.FALSE, tkinter.FALSE)

        self.lblTitulo = ttk.Label(self.root, text='Productos')
        self.lblTitulo.grid(row=0, column=0, columnspan=2)

        #CREACION TABLA
        self.tablaProductos = ttk.Treeview(self.root, selectmode = 'browse')
        self.tablaProductos.grid(
            row        = 1, 
            column     = 0, 
            sticky     = "nsew", 
            padx       = 5, 
            pady       = 10
        )

        #BARRASCROLL
        self.scrollbarTabla = ttk.Scrollbar(self.root, orient = "vertical", command=self.tablaProductos.yview)
        self.scrollbarTabla.grid(
            row    = 1, 
            column = 1, 
            sticky = "nsew",
            pady=10)

        #CONFIG TABLA
        self.tablaProductos.configure(xscrollcommand=self.scrollbarTabla.set)

        #NUMERO DE COLUMNAS
        self.tablaProductos["columns"] = ("nombre", "descripcion", "marca", "stock", "precio_venta", "precio_compra")

        #DEFINIENDO HEADING
        self.tablaProductos['show'] = 'headings'

        #AGREGAR COLUMNAS
        self.tablaProductos.column("nombre",        width = 120, anchor='s')
        self.tablaProductos.column("descripcion",   width = 260, anchor='s')
        self.tablaProductos.column("marca",         width = 120, anchor='s')
        self.tablaProductos.column("stock",         width = 120, anchor='s')
        self.tablaProductos.column("precio_venta",  width = 120, anchor='s')
        self.tablaProductos.column("precio_compra", width = 120, anchor='s')

        #HEADINGS COLUMNAS
        self.tablaProductos.heading("nombre",        text="Nombre")
        self.tablaProductos.heading("descripcion",   text="Descripcion")
        self.tablaProductos.heading("marca",         text="Marca")
        self.tablaProductos.heading("stock",         text="Stock")
        self.tablaProductos.heading("precio_venta",  text="Precio Venta")
        self.tablaProductos.heading("precio_compra", text="Precio Compra")


        #!LLeno la tabla de productos
        self.llenarTablaProductos()


    def llenarTablaProductos(self):
        productoController = ProductoController()
        productos          = productoController.obtenerProductos()
        for producto in productos:
            self.tablaProductos.insert("",
            0,
            text   = producto['_id'],
            values = (
            producto['nombre'], 
            producto['descripcion'],
            producto['marca'],
            producto['stock'],
            producto['precio_venta'],
            producto['precio_compra'],
            )
            )