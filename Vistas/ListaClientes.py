import tkinter
from tkinter import ttk
import Controladores.ClienteController
from Helpers.Format_fechas import *
from Singleton import singleton
import Definiciones

class ListaClientes():
    def __init__(self) -> None:
        #CREACION VENTANA
        self.root = tkinter.Toplevel()
        self.root.resizable(tkinter.FALSE, tkinter.FALSE)
        self.root.configure(background=Definiciones.COLOR_2)


        Definiciones.estiloTablas(self.root)
        Definiciones.estiloLabelTitulo(self.root)

        self.lblTitulo = ttk.Label(self.root, text='Clientes', style='titulo.TLabel')
        self.lblTitulo.grid(row=0, column=0, columnspan=2, pady=8)

        #CREACION TABLA
        self.tablaClientes = ttk.Treeview(self.root, selectmode = 'browse', style='mystyle.Treeview')
        self.tablaClientes.grid(
            row        = 1, 
            column     = 0, 
            sticky     = "nsew", 
            padx       = 5, 
            pady       = 10
        )

        #BARRASCROLL
        self.scrollbarTabla = ttk.Scrollbar(self.root, orient = "vertical", command=self.tablaClientes.yview)
        self.scrollbarTabla.grid(
            row    = 1, 
            column = 1, 
            sticky = "nsew",
            pady=10)

        #CONFIG TABLA
        self.tablaClientes.configure(xscrollcommand=self.scrollbarTabla.set)

        #NUMERO DE COLUMNAS
        self.tablaClientes["columns"] = ("nombre", "apellido", "tipo_dni", "documento", "fecha_nacimiento", "nro_telefono")

        #DEFINIENDO HEADING
        self.tablaClientes['show'] = 'headings'

        #AGREGAR COLUMNAS
        self.tablaClientes.column("nombre",           width = 120, anchor='s')
        self.tablaClientes.column("apellido",         width = 120, anchor='s')
        self.tablaClientes.column("tipo_dni",         width = 150, anchor='s')
        self.tablaClientes.column("documento",        width = 120, anchor='s')
        self.tablaClientes.column("fecha_nacimiento", width = 150, anchor='s')
        self.tablaClientes.column("nro_telefono",     width = 150, anchor='s')

        #HEADINGS COLUMNAS
        self.tablaClientes.heading("nombre",           text="Nombre")
        self.tablaClientes.heading("apellido",         text="Apellido")
        self.tablaClientes.heading("tipo_dni",         text="Tipo documento")
        self.tablaClientes.heading("documento",        text="Documento")
        self.tablaClientes.heading("fecha_nacimiento", text="Fecha de nacimiento")
        self.tablaClientes.heading("nro_telefono",     text="Telefono")


        #!LLeno la tabla de productos
        self.llenartablaClientes()


    def llenartablaClientes(self):
        clienteController = Controladores.ClienteController.ClienteController()
        clientes          = clienteController.obtenerClientes()
        for cliente in clientes:
            self.tablaClientes.insert("",
            0,
            text   = cliente['_id'],
            values = (
            cliente['nombre'], 
            cliente['apellido'], 
            cliente['tipo_dni'], 
            cliente['documento'], 
            cliente['fecha_nacimiento'], 
            cliente['nro_telefono'], 
            )
            )