from posixpath import commonpath
import tkinter
from tkinter import ttk
from Controladores import EmpresaController
import Definiciones

class VentanaConfig():
    
    def __init__(self):
        self.root           = tkinter.Toplevel()
        self.root.config(bg = Definiciones.COLOR_2)
        
        self.empresaController = EmpresaController.EmpresaController() 
        datosEmpresa = self.obtenerDatosEmpresa()
        
        # self.root.columnconfigure(0, weight=1)
        # self.root.geometry("400x350")
        #!Inicializacion de las variables que ingresa el usuario
  
        #Inicializacion de los estilos
        Definiciones.estiloBotonNormal(self.root)#Inicializamos el estilo de los botones
        Definiciones.estiloLabel1(self.root)#Inicializamos el estilo de las etiquetas
        Definiciones.estiloLabelTitulo(self.root)#Inicializamos el estilo de las etiquetas
        Definiciones.estiloBotonCancelar(self.root)#Inicializamos el estilo de las etiquetas
        Definiciones.estiloCombobox(self.root)
        

        self.lblTitulo        = ttk.Label(self.root, text="Configuraciones", style='titulo.TLabel')
        self.lblTitulo.grid(row=0, column=0, columnspan=3)

        self.lblNombre       = ttk.Label(self.root, text='Nombre de la empresa', style='etiqueta.TLabel')
        self.lblNombre.grid(row=1, column=0, padx = 16, pady = 8, sticky='e')
        self.tbNombre        = ttk.Entry(self.root)
        self.tbNombre.insert(0, datosEmpresa[0]['nombre'])
        self.tbNombre.configure(state='readonly')
        self.tbNombre.grid(row=1, column=1, padx = 16, pady = 8)  
        self.btnNombre       =  ttk.Button(self.root, text='Editar', command=self.habilitarCampoNombre)
        self.btnNombre.grid(row=1, column=2, padx = 16, pady = 8)
        
        self.lblDireccion  = ttk.Label(self.root, text='Direccion', style='etiqueta.TLabel')
        self.lblDireccion.grid(row=2, column=0, padx = 16, pady = 8, sticky='e')
        self.tbDireccion   = ttk.Entry(self.root)
        self.tbDireccion.insert(0, datosEmpresa[0]['direccion'])
        self.tbDireccion.configure(state='readonly')
        self.tbDireccion.grid(row=2, column=1, padx = 16, pady = 8)
        self.btnDireccion  =  ttk.Button(self.root, text='Editar', command=self.habilitarCampoDireccion)
        self.btnDireccion.grid(row=2, column=2, padx = 16, pady = 8)
        
        
        self.lblTelefono        = ttk.Label(self.root, text='Telefono', style='etiqueta.TLabel')
        self.lblTelefono.grid(row=3, column=0, padx = 16, pady = 8, sticky='e')
        self.tbTelefono         = ttk.Entry(self.root )
        self.tbTelefono.insert(0, datosEmpresa[0]['telefono'])
        self.tbTelefono.configure(state='readonly')
        self.tbTelefono.grid(row=3, column=1, padx = 16, pady = 8)
        self.btnTelefono        =  ttk.Button(self.root, text='Editar', command=self.habilitarCampoTelefono)
        self.btnTelefono.grid(row=3, column=2, padx = 16, pady = 8)
        
        self.lblCorreo = ttk.Label(self.root, text='Correo', style='etiqueta.TLabel')
        self.lblCorreo.grid(row=4, column=0, padx = 16, pady = 8, sticky='e')
        self.tbCorreo  = ttk.Entry(self.root)
        self.tbCorreo.insert(0, datosEmpresa[0]['email'])
        self.tbCorreo.configure(state='readonly')
        self.tbCorreo.grid(row=4, column=1, padx = 16, pady = 8)
        self.btnCorreo =  ttk.Button(self.root, text='Editar', command=self.habilitarCampoCorreo)
        self.btnCorreo.grid(row=4, column=2, padx = 16, pady = 8)
        
        self.lblSitioWeb  = ttk.Label(self.root, text='Sitio Web', style='etiqueta.TLabel')
        self.lblSitioWeb.grid(row=5, column=0, padx = 16, pady = 8, sticky='e')
        self.tbSitioWeb   = ttk.Entry(self.root)
        self.tbSitioWeb.insert(0, datosEmpresa[0]['sitio_web'])
        self.tbSitioWeb.configure(state='readonly')
        self.tbSitioWeb.grid(row=5, column=1, padx = 16, pady = 8)
        self.btnSitioWeb  =  ttk.Button(self.root, text='Editar', command=self.habilitarCampoSitioWeb)
        self.btnSitioWeb.grid(row=5, column=2, padx = 16, pady = 8)
       

        #Boton Ingresar
        self.btnGuardar      = ttk.Button(self.root, text="Guardar", style='botonNormal.TButton', command=self.editarDatosEmpresa)
        self.btnGuardar.grid(row=6, column=2, padx = 16, pady = 8, sticky='ew')

        borde = tkinter.LabelFrame(self.root, bd=2, bg=Definiciones.COLOR_1)
        borde.columnconfigure(0, weight=1)
        borde.grid(row=6, column=1, padx = 16, pady = 8, sticky='e')

        #Boton Cancelar
        self.btnCancelar      = ttk.Button(borde, text="Cancelar", style='botonCancelar.TButton', command=self.root.destroy)
        self.btnCancelar.grid(row=0, column=0, sticky='ew')
        
        
        
    def obtenerDatosEmpresa(self):
        return self.empresaController.obtenerDatosEmpresa()

    def habilitarCampoNombre(self):
        self.tbNombre.configure(state='normal')
    
    def habilitarCampoDireccion(self):
        self.tbDireccion.configure(state='normal')
    
    def habilitarCampoTelefono(self):
        self.tbTelefono.configure(state='normal')
        
    def habilitarCampoSitioWeb(self):
        self.tbSitioWeb.configure(state='normal')
        
    def habilitarCampoCorreo(self):
        self.tbCorreo.configure(state='normal')
        
    def editarDatosEmpresa(self):
        self.empresaController.editarDatosEmpresa(
            self.tbNombre.get(),
            self.tbDireccion.get(),
            self.tbTelefono.get(),
            self.tbCorreo.get(),
            self.tbSitioWeb.get()
        )
        self.root.destroy()