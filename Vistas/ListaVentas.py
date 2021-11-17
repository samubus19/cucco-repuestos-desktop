import tkinter
from tkinter import ttk
from Controladores.VentasController import *
from Helpers.Format_fechas import *
import Definiciones
from Helpers import Imprimir_Reporte_Venta
from Controladores import ClienteController, UsuarioController
class ListaVentas():
    def __init__(self) -> None:
        #CREACION VENTANA
        self.root = tkinter.Toplevel()
        self.root.resizable(tkinter.FALSE, tkinter.FALSE)
        self.root.configure(background=Definiciones.COLOR_2)


        Definiciones.estiloTablas(self.root)
        Definiciones.estiloLabelTitulo(self.root)
        Definiciones.estiloBotonNormal(self.root)#Inicializamos el estilo de los botones

        self.lblTitulo = ttk.Label(self.root, text='Ventas', style='titulo.TLabel')
        self.lblTitulo.grid(row=0, column=0, columnspan=2, pady=8)

        #CREACION TABLA
        self.tablaVentas = ttk.Treeview(self.root, selectmode = 'browse', style='mystyle.Treeview')
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

       #Boton Ingresar
        self.btnImprimirPdf      = ttk.Button(self.root, text="Imprimir reporte", style='botonNormal.TButton', command=self.imprimirPdf)
        self.btnImprimirPdf.grid(row=2, column=0, sticky="ew", padx = 16, pady = 8)

        #!LLeno la tabla de productos
        self.llenartablaVentas()
        #Bindeo la tabla de ventas
        self.tablaVentas.bind("<1>", self.obtenerIdVenta)


    def llenartablaVentas(self):
        ventasController  = VentasController()
        ventas            = ventasController.obtenerVentas()
        clienteController = ClienteController.ClienteController()
        usuarioController = UsuarioController.UsuarioController()
        # print(ventas)
        for venta in ventas:
            cliente = clienteController.obtenerClientePorId(venta['id_cliente'])
            usuario = usuarioController.obtenerUsuarioPorId(venta['id_usuario'])
            
            self.tablaVentas.insert("",
                0,
                text   = venta['_id'],
                values = (
                cliente['nombre'] + " " + cliente['apellido'], 
                usuario['email'], 
                formatearFecha(venta['createdAt']),
                venta['precio_total'],
            )
            )
    
    def imprimirPdf(self):
        print(self.text)
        impresorPdf = Imprimir_Reporte_Venta.ImpresorPdf(self.text)
        impresorPdf.selectProducto()
        
    def obtenerIdVenta(self, event):
        item = event.widget.identify("item", event.x, event.y)
        self.text = event.widget.item(item, "text")