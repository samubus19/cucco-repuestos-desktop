import tkinter
from Controladores.ProductoController import *
from Vistas.ListaProductos import *
from Vistas.ListaVentas import *
from Vistas.ListaClientes import *
from Vistas.ListaUsuarios import *
import Definiciones
class MenuPrincipal():
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.resizable(tkinter.FALSE, tkinter.FALSE)
        self.root.title("Cucco Repuestos")
        self.root.config(bg=Definiciones.COLOR_1)
        self.root.geometry("+0+0")

        #ACCESO RAPIDO USUARIOS
        self.btnUsuarios = tkinter.Button(
            self.root, 
            compound = "top", 
            bd       = 1, 
            font     = (Definiciones.FUENTE_1,Definiciones.TAMAÑO_FUENTE_M,Definiciones.ESTILO_FUENTE_1), 
            fg       = Definiciones.COLOR_NEGRO, 
            bg       = Definiciones.COLOR_BLANCO, 
            text     = "Usuarios\n\n",
            command=self.abrirVentanaUsuarios
        )
        self.btnUsuarios.grid(row=0, column=1, sticky="w")

        #ACCESO RAPIDO CLIENTES
        self.btnClientes = tkinter.Button(
            self.root,
            compound = "top", 
            bd       = 1, 
            font     =(Definiciones.FUENTE_1, Definiciones.TAMAÑO_FUENTE_M , Definiciones.ESTILO_FUENTE_1),
            fg       = Definiciones.COLOR_NEGRO, 
            bg       = Definiciones.COLOR_BLANCO, 
            text     = "Clientes\n\n",
            command  = self.abrirVentanaClientes
        )
        self.btnClientes.grid(row=0, column=2, sticky="w")
        
        #ACCESO RAPIDO,PRODUCTOS
        self.btnProductos = tkinter.Button(
            self.root, 
            bd       = 1, 
            compound = "top",
            font     = (Definiciones.FUENTE_1, Definiciones.TAMAÑO_FUENTE_M, Definiciones.ESTILO_FUENTE_1),
            fg       = Definiciones.COLOR_NEGRO, 
            bg       = Definiciones.COLOR_BLANCO, 
            text     = "Productos\n\n", 
            command  = self.abrirVentanaProductos
        )
        self.btnProductos.grid(row=0, column=3, sticky="w", columnspan=1)

        #ACCESO RAPIDO,VENTAS
        self.btnVentas = tkinter.Button(self.root, 
            bd       = 1, 
            compound = "top",
            font     = (Definiciones.FUENTE_1, Definiciones.TAMAÑO_FUENTE_M, Definiciones.ESTILO_FUENTE_1),
            fg       = Definiciones.COLOR_NEGRO, 
            bg       = Definiciones.COLOR_BLANCO, 
            text     = "Ventas\n\n", 
            command  = self.abrirVentanaVentas
        )
        self.btnVentas.grid(row=0, column=4, sticky="w", columnspan=1)

        self.root.mainloop()

    def abrirVentanaProductos(self):
        ventanaProductos = ListaProductos()

    def abrirVentanaVentas(self):
        ventanaVentas    = ListaVentas()

    def abrirVentanaUsuarios(self):
        ventanaUsuarios  = ListaUsuarios()
    
    def abrirVentanaClientes(self):
        ventanaClientes  = ListaClientes()