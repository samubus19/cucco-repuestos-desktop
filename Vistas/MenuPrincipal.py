import tkinter
from Controladores.ProductoController import *
from Vistas.ListaProductos import *
from Vistas.ListaVentas import *

fuente      = 'Helvetica'
negrita     = 'bold'
colorNegro  = '#000'
colorBlanco = '#fff'

class MenuPrincipal():
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.resizable(tkinter.FALSE, tkinter.FALSE)
        self.root.title("Cucco Repuestos")
        self.root.config(bg='#000')
        self.root.geometry("+0+0")

        #ACCESO RAPIDO USUARIOS
        self.btnUsuarios = tkinter.Button(self.root, compound="top", bd=1, relief="ridge",font=(fuente,8,negrita),fg=colorNegro, bg=colorBlanco, text="Usuarios\n\n")
        self.btnUsuarios.grid(row=0, column=1, sticky="w")

        #ACCESO RAPIDO CLIENTES
        self.btnClientes = tkinter.Button(self.root, compound="top", bd=1, relief="ridge",font=(fuente,8,negrita),fg=colorNegro, bg=colorBlanco, text="Clientes\n\n")
        self.btnClientes.grid(row=0, column=2, sticky="w")
        
        #ACCESO RAPIDO,PRODUCTOS
        self.btnProductos = tkinter.Button(self.root, bd=1, relief="ridge", compound="top",font=(fuente,8,negrita),fg=colorNegro, bg=colorBlanco, text="Productos\n\n", command=self.abrirVentanaProductos)
        self.btnProductos.grid(row=0, column=3, sticky="w", columnspan=1)

        #ACCESO RAPIDO,VENTAS
        self.btnVentas = tkinter.Button(self.root, bd=1, relief="ridge", compound="top",font=(fuente,8,negrita),fg=colorNegro, bg=colorBlanco, text="Ventas\n\n", command=self.abrirVentanaVentas)
        self.btnVentas.grid(row=0, column=4, sticky="w", columnspan=1)

        #ACCESO RAPIDO, CONFIGURACIONES
        self.btnConfiguraciones = tkinter.Button(self.root, bd=1, relief="ridge",font=(fuente,8,negrita),compound="top", fg=colorNegro, bg=colorBlanco, text="Config\n\n")
        self.btnConfiguraciones.grid(row=0, column=5, sticky="w", columnspan=1)


        self.root.mainloop()

    def abrirVentanaProductos(self):
        ventanaProductos = ListaProductos()

    def abrirVentanaVentas(self):
        ventanaVentas    = ListaVentas()