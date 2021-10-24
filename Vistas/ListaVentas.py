import tkinter
from tkinter import ttk
from Controladores.VentasController import *
from Helpers.Format_fechas import *
from Singleton import singleton

@singleton
class ListaVentas():
    def __init__(self) -> None:
        #CREACION VENTANA
        self.root = tkinter.Toplevel()
        self.root.resizable(tkinter.FALSE, tkinter.FALSE)

        self.lblTitulo = ttk.Label(self.root, text='Ventas')
        self.lblTitulo.grid(row=0, column=0, columnspan=2)

        #CREACION TABLA
        self.tablaVentas = ttk.Treeview(self.root, selectmode = 'browse')
        self.tablaVentas.grid(
            row        = 1, 
            column     = 0, 
            sticky     = "nsew", 
            padx       = 5, 
            pady       = 10
        )

        #BARRASCROLL
        self.scrollbarTabla = ttk.Scrollbar(self.root, orient = "vertical", command=self.tablaVentas.yview)
        self.scrollbarTabla.grid(
            row    = 1, 
            column = 1, 
            sticky = "nsew",
            pady=10)

        #CONFIG TABLA
        self.tablaVentas.configure(xscrollcommand=self.scrollbarTabla.set)

        #NUMERO DE COLUMNAS
        self.tablaVentas["columns"] = ("cliente", "email_cliente", "fecha_venta", "precio_total")

        #DEFINIENDO HEADING
        self.tablaVentas['show'] = 'headings'

        #AGREGAR COLUMNAS
        self.tablaVentas.column("cliente",       width = 120, anchor='s')
        self.tablaVentas.column("email_cliente", width = 120, anchor='s')
        self.tablaVentas.column("fecha_venta",   width = 120, anchor='s')
        self.tablaVentas.column("precio_total",  width = 120, anchor='s')

        #HEADINGS COLUMNAS
        self.tablaVentas.heading("cliente",        text="Cliente")
        self.tablaVentas.heading("email_cliente",  text="Email")
        self.tablaVentas.heading("fecha_venta",    text="Fecha de venta")
        self.tablaVentas.heading("precio_total",   text="Precio total")


        #!LLeno la tabla de productos
        self.llenartablaVentas()


    def llenartablaVentas(self):
        ventasController = VentasController()
        ventas           = ventasController.obtenerVentas()
        for venta in ventas:
            self.tablaVentas.insert("",
            0,
            text   = venta['_id'],
            values = (
            venta['cliente']['usuario'], 
            venta['cliente']['email'], 
            formatearFecha(venta['createdAt']),
            venta['precio_total'],
            )
            )