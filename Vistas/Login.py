import tkinter
from tkinter import ttk
import sys
from Singleton import *
from Controladores.UsuarioController import *
import Definiciones
import PIL
from PIL import ImageTk
from PIL import Image

@singleton
class LoginView(object):
    def __init__(self) -> None:

        self.root           = tkinter.Tk()
        self.root.config(bg = Definiciones.COLOR_2)
        self.root.columnconfigure(0, weight=1)
        self.root.geometry("400x350")


        Definiciones.estiloBotonNormal(self.root)#Inicializamos el estilo de los botones
        Definiciones.estiloLabel1(self.root)#Inicializamos el estilo de las etiquetas

        self.usuarioInput     = tkinter.StringVar()
        self.contraseniaInput = tkinter.StringVar() 
        self.emailInput       = tkinter.StringVar() 

        #CREACION LOGO
        self.imgLogo = PIL.Image.open(os.path.join(os.getcwd(), 'Imagenes/logo_naranja.png'))
        # self.imgLogo = self.imgLogo.resize((100, 100), PIL.Image.ANTIALIAS)  # Redimension (Alto, Ancho)
        self.imgLogo = PIL.ImageTk.PhotoImage(self.imgLogo)
        self.lblLogo = ttk.Label(self.root, image=self.imgLogo)
        self.lblLogo.grid(row=0, column=0, pady=8)

        self.lblUsuario       = ttk.Label(self.root, text='Usuario', style='etiqueta.TLabel')
        self.lblUsuario.grid(row=1, column=0)
        self.tbUsuario        = ttk.Entry(self.root, textvariable = self.usuarioInput)
        self.tbUsuario.grid(row=2, column=0, sticky="nswe", padx = 16, pady = 8)       
        
        self.lblContrasenia   = ttk.Label(self.root, text='Contraseña', style='etiqueta.TLabel')
        self.lblContrasenia.grid(row=3, column=0, columnspan=2)
        self.tbContrasenia    = ttk.Entry(self.root, show='*' ,textvariable = self.contraseniaInput)
        self.tbContrasenia.grid(row=4, column=0, sticky="nsew", padx = 16, pady = 8)
        
        #Boton Ingresar
        self.btnIngresar      = ttk.Button(self.root, text="Iniciar Sesión", style='botonNormal.TButton', command=self.iniciarSesion)
        self.btnIngresar.grid(row=5, column=0, sticky="ew", padx = 16, pady = 8)

        #Boton Cancelar
        self.btnCancelar      = ttk.Button(self.root, text="Salir", style='botonNormal.TButton', command = self.root.destroy)
        self.btnCancelar.grid(row=6, column=0, sticky="ew", padx = 16, pady = 8)

        self.tbUsuario.focus() #Hacemos focus en el campo de usuario apenas se abra la ventana

        self.root.mainloop()

    def iniciarSesion(self):
        datosLogin = UsuarioController(
            usuario     = self.usuarioInput.get(), 
            contrasenia = self.contraseniaInput.get(), 
            email       = self.emailInput.get()
        )
        self.root.destroy()
        datosLogin.iniciarSesion()
        