import tkinter
from tkinter import ttk
import Controladores.UsuarioController
from Helpers.Format_fechas import *
from Singleton import singleton
import Definiciones

@singleton
class ListaUsuarios():
    def __init__(self) -> None:
        #CREACION VENTANA
        self.root = tkinter.Toplevel()
        self.root.resizable(tkinter.FALSE, tkinter.FALSE)
        self.root.configure(background=Definiciones.COLOR_2)


        Definiciones.estiloTablas(self.root)
        Definiciones.estiloLabelTitulo(self.root)

        self.lblTitulo = ttk.Label(self.root, text='Usuarios', style='titulo.TLabel')
        self.lblTitulo.grid(row=0, column=0, columnspan=2, pady=8)

        #CREACION TABLA
        self.tablaUsuarios = ttk.Treeview(self.root, selectmode = 'browse', style='mystyle.Treeview')
        self.tablaUsuarios.grid(
            row        = 1, 
            column     = 0, 
            sticky     = "nsew", 
            padx       = 5, 
            pady       = 10
        )

        #BARRASCROLL
        self.scrollbarTabla = ttk.Scrollbar(self.root, orient = "vertical", command=self.tablaUsuarios.yview)
        self.scrollbarTabla.grid(
            row    = 1, 
            column = 1, 
            sticky = "nsew",
            pady=10)

        #CONFIG TABLA
        self.tablaUsuarios.configure(xscrollcommand=self.scrollbarTabla.set)

        #NUMERO DE COLUMNAS
        self.tablaUsuarios["columns"] = ("usuario", "email", "fecha_alta")

        #DEFINIENDO HEADING
        self.tablaUsuarios['show'] = 'headings'

        #AGREGAR COLUMNAS
        self.tablaUsuarios.column("usuario",    width = 120, anchor='s')
        self.tablaUsuarios.column("email",      width = 120, anchor='s')
        self.tablaUsuarios.column("fecha_alta", width = 120, anchor='s')

        #HEADINGS COLUMNAS
        self.tablaUsuarios.heading("usuario",    text="Usuario")
        self.tablaUsuarios.heading("email",      text="Email")
        self.tablaUsuarios.heading("fecha_alta", text="Fecha de alta")


        #!LLeno la tabla de productos
        self.llenartablaUsuarios()


    def llenartablaUsuarios(self):
        usuarioController = Controladores.UsuarioController.UsuarioController()
        usuarios          = usuarioController.obtenerUsuarios()
        for usuario in usuarios:
            self.tablaUsuarios.insert("",
            0,
            text   = usuario['_id'],
            values = (
            usuario['usuario'], 
            usuario['email'], 
            formatearFecha(usuario['createdAt']),
            )
            )