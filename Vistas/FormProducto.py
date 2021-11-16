import tkinter
from tkinter import IntVar, StringVar, ttk, filedialog
from LectorToken import obtenerToken
from Singleton import *
import Definiciones
from Controladores.ProductoController import *
import Vistas.MenuPrincipal

class FormProducto():
    def __init__(self, bandera = 0) -> None:

        self.root           = tkinter.Toplevel()
        self.root.config(bg = Definiciones.COLOR_2)
        # self.root.columnconfigure(0, weight=1)
        # self.root.geometry("400x350")
        #!Inicializacion de las variables que ingresa el usuario
        self.bandera            = bandera
        self.productoController = ProductoController() 
  
        #Inicializacion de los estilos
        Definiciones.estiloBotonNormal(self.root)#Inicializamos el estilo de los botones
        Definiciones.estiloLabel1(self.root)#Inicializamos el estilo de las etiquetas
        Definiciones.estiloLabelTitulo(self.root)#Inicializamos el estilo de las etiquetas
        Definiciones.estiloBotonCancelar(self.root)#Inicializamos el estilo de las etiquetas
        Definiciones.estiloCombobox(self.root)

        self.lblTitulo        = ttk.Label(self.root, text="Nuevo producto", style='titulo.TLabel')
        self.lblTitulo.grid(row=0, column=0, columnspan=2)

        self.lblNombre       = ttk.Label(self.root, text='Nombre', style='etiqueta.TLabel')
        self.lblNombre.grid(row=1, column=0, padx = 16, pady = 8, sticky='e')
        self.tbNombre        = ttk.Entry(self.root)
        self.tbNombre.grid(row=1, column=1, padx = 16, pady = 8)       
        
        self.lblDescripcion  = ttk.Label(self.root, text='Descripcion', style='etiqueta.TLabel')
        self.lblDescripcion.grid(row=2, column=0, padx = 16, pady = 8, sticky='e')
        self.tbDescripcion   = ttk.Entry(self.root )
        self.tbDescripcion.grid(row=2, column=1, padx = 16, pady = 8)
        
        self.lblMarca        = ttk.Label(self.root, text='Marca', style='etiqueta.TLabel')
        self.lblMarca.grid(row=3, column=0, padx = 16, pady = 8, sticky='e')
        self.tbMarca         = ttk.Entry(self.root )
        self.tbMarca.grid(row=3, column=1, padx = 16, pady = 8)
        
        self.lblCategoria  = ttk.Label(self.root, text='Categoría', style='etiqueta.TLabel')
        self.lblCategoria.grid(row=4, column=0, padx = 16, pady = 8, sticky='e')
        self.cbCategorias  = ttk.Combobox(self.root, state='readonly', style='TCombobox')
        self.cbCategorias.grid(row=4, column=1, padx = 16, pady = 8)
        
        self.lblPrecioCompra  = ttk.Label(self.root, text='Precio de compra', style='etiqueta.TLabel')
        self.lblPrecioCompra.grid(row=5, column=0, padx = 16, pady = 8, sticky='e')
        self.tbPrecioCompra   = ttk.Entry(self.root )
        self.tbPrecioCompra.grid(row=5, column=1, padx = 16, pady = 8)

        self.lblPrecioVenta  = ttk.Label(self.root, text='Precio de venta', style='etiqueta.TLabel')
        self.lblPrecioVenta.grid(row=6, column=0, padx = 16, pady = 8, sticky='e')
        self.tbPrecioVenta   = ttk.Entry(self.root )
        self.tbPrecioVenta.grid(row=6, column=1, padx = 16, pady = 8)

        self.lblStock        = ttk.Label(self.root, text='Stock', style='etiqueta.TLabel')
        self.lblStock.grid(row=7, column=0, padx = 16, pady = 8, sticky='e')
        self.tbStock         = ttk.Entry(self.root )
        self.tbStock.grid(row=7, column=1, padx = 16, pady = 8)

        #Boton Ingresar
        self.btnImagen       = ttk.Button(self.root, text="Seleccionar Imagen", command=self.seleccionarImagen)
        self.btnImagen.grid(row=8, column=1, padx = 16, pady = 8, sticky='we')

        #Boton Ingresar
        self.btnGuardar      = ttk.Button(self.root, text="Guardar", style='botonNormal.TButton', command=self.agregarProducto)
        self.btnGuardar.grid(row=9, column=1, padx = 16, pady = 8, sticky='ew')

        borde = tkinter.LabelFrame(self.root, bd=2, bg=Definiciones.COLOR_1)
        borde.columnconfigure(0, weight=1)
        borde.grid(row=9, column=0, sticky='ew', padx = 16, pady = 8)

        #Boton Cancelar
        self.btnCancelar      = ttk.Button(borde, text="Cancelar", style='botonCancelar.TButton', command = self.destruirVentana)
        self.btnCancelar.grid(row=0, column=0, sticky='ew')

        self.llenarComboCategorias()
        self.tbNombre.focus() #Hacemos focus en el campo de usuario apenas se abra la ventana

    def seleccionarImagen(self):
        self.archivoImagen   = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=(('Images', ('*.jpg', '*.png', '*.jpeg')), ))

    def agregarProducto(self):
        if(self.bandera == 0):
            self.productoController.agregarProducto(
                nombre        = self.tbNombre.get(),
                stock         = int(self.tbStock.get()),
                descripcion   = self.tbDescripcion.get(),
                precio_venta  = float(self.tbPrecioVenta.get()),
                precio_compra = float(self.tbPrecioCompra.get()),
                marca         = self.tbMarca.get(),
                categoria     = self.cbCategorias.get(),
                imagen        = self.archivoImagen
            )
            self.root.destroy()
        else:
            print("Aca iria para editar el producto")

    def llenarComboCategorias(self):
        categorias                  = self.productoController.obtenerCategorias()
        listaCategorias = []
        for categoria in categorias:
            listaCategorias.append(categoria['nombre'])
        # print(listaCategorias)
        self.cbCategorias['values'] = listaCategorias

    def destruirVentana(self):
        self.root.destroy()