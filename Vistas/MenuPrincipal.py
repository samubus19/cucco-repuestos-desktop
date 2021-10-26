import tkinter
from Controladores.ProductoController import *
from Vistas.ListaProductos import *
from Vistas.ListaVentas import *
from Vistas.ListaClientes import *
from Vistas.ListaUsuarios import *
from Vistas.FormProducto import *
import Definiciones
from Singleton import *
class MenuPrincipal():


    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title("Cucco Repuestos")
        self.root.columnconfigure(0, weight=1)
        self.root.geometry("350x215+0+0")
        # self.root.resizable(tkinter.FALSE, tkinter.FALSE)
        self.root.config(bg=Definiciones.COLOR_2)
        Definiciones.estiloBotonNormal(self.root)#Inicializamos el estilo de los botones
        Definiciones.estiloBotonCancelar(self.root)#Inicializamos el estilo de los botones
        Definiciones.estiloLabel1(self.root)#Inicializamos el estilo de las etiquetas

        #ACCESO RAPIDO USUARIOS
        self.btnUsuarios = ttk.Button(
            self.root, 
            style='botonNormal.TButton',
            text='Usuarios',
            command=self.abrirVentanaUsuarios
        )
        self.btnUsuarios.grid(row=0, column=0, sticky="ew", pady=2)

        #ACCESO RAPIDO CLIENTES
        self.btnClientes = ttk.Button(
            self.root, 
            style='botonNormal.TButton',
            text='Clientes',
            command  = self.abrirVentanaClientes
        )
        self.btnClientes.grid(row=1, column=0, sticky="ew", pady=2)
        
        #ACCESO RAPIDO,PRODUCTOS
        self.btnProductos = ttk.Button(
            self.root, 
            style='botonNormal.TButton',
            text     = "Productos", 
            command  = self.abrirVentanaProductos
        )
        self.btnProductos.grid(row=2, column=0, sticky="ew", pady=2)

        #ACCESO RAPIDO,VENTAS   
        self.btnFormProducto = ttk.Button(
            self.root, 
            style='botonNormal.TButton',
            text     = "Nuevo Producto", 
            command  = self.abrirVentanaFormProducto
        )
        self.btnFormProducto.grid(row=3, column=0, sticky="ew", pady=2)


        #ACCESO RAPIDO,VENTAS
        self.btnVentas = ttk.Button(
            self.root, 
            style='botonNormal.TButton',
            text     = "Ventas", 
            command  = self.abrirVentanaVentas
        )
        self.btnVentas.grid(row=4, column=0, sticky="ew", pady=2)

        borde = tkinter.LabelFrame(self.root, bd=2, bg=Definiciones.COLOR_1)
        borde.columnconfigure(0, weight=1)
        borde.grid(row=5, column=0, sticky='ew', pady=2)

        #ACCESO RAPIDO,VENTAS
        self.btnSalir = ttk.Button(
            borde, 
            style    = 'botonCancelar.TButton',
            text     = "Salir", 
            command  = self.root.destroy
        )
        self.btnSalir.grid(row=0 ,column=0, sticky='ew')

        self.root.mainloop()

    def abrirVentanaProductos(self):
        ventanaProductos = ListaProductos()

    def abrirVentanaVentas(self):
        ventanaVentas    = ListaVentas()

    def abrirVentanaUsuarios(self):
        ventanaUsuarios  = ListaUsuarios()
    
    def abrirVentanaClientes(self):
        ventanaClientes  = ListaClientes()

    def abrirVentanaFormProducto(self):
        ventanaFormProducto = FormProducto(0)


    