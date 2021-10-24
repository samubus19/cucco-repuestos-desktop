import tkinter
from tkinter import ttk
import sys
from Singleton import *
from Controladores.UsuarioController import *
import Definiciones

@singleton
class LoginView(object):
    def __init__(self) -> None:


        self.root             = tkinter.Tk()
        self.root.config(bg = Definiciones.COLOR_2)

        self.usuarioInput     = tkinter.StringVar()
        self.contraseniaInput = tkinter.StringVar() 
        self.emailInput       = tkinter.StringVar() 

        self.lblUsuario       = ttk.Label(self.root, text='Usuario', background=Definiciones.COLOR_2)
        self.lblUsuario.grid(row=0, column=0, columnspan=2)
        self.tbUsuario        = tkinter.Entry(self.root, bd=2, width=30, fg=Definiciones.COLOR_NEGRO, bg=Definiciones.COLOR_BLANCO, font=(Definiciones.FUENTE_1, 10), textvariable = self.usuarioInput)
        self.tbUsuario.grid(row=1, column=0, padx=10,pady=25, columnspan=1, sticky="ns")       
        
        self.lblContrasenia   = ttk.Label(self.root, text='Usuario', background=Definiciones.COLOR_2)
        self.lblContrasenia.grid(row=2, column=0, columnspan=2)
        self.tbContrasenia    = tkinter.Entry(self.root, width=30, fg=Definiciones.COLOR_NEGRO, bd=2, bg=Definiciones.COLOR_BLANCO, font=(Definiciones.FUENTE_1, 10), textvariable = self.contraseniaInput)
        self.tbContrasenia.grid(row="3", column="0", padx=10,pady=25, columnspan=1, sticky="ns")
        
        #Boton Ingresar
        self.btnIngresar = tkinter.Button(self.root, text="Ingresar", width=35, fg=Definiciones.COLOR_BLANCO, bg=Definiciones.COLOR_1, bd=3, relief="flat", font=(Definiciones.FUENTE_1, 12), command=self.iniciarSesion)
        self.btnIngresar.grid(row="4", column="0",pady=0.5, columnspan=1, sticky="nsew")

        #Boton Cancelar
        self.btnCancelar      = tkinter.Button(self.root, text="Salir", width=35, fg=Definiciones.COLOR_BLANCO, bg=Definiciones.COLOR_1, bd=3, relief="flat", font=(Definiciones.FUENTE_1, 12), command = self.root.destroy)
        self.btnCancelar.grid(row="5", column="0",pady=0, columnspan=1, sticky="nsew")



        self.root.mainloop()

    def iniciarSesion(self):
        datosLogin = UsuarioController(
            usuario     = self.usuarioInput.get(), 
            contrasenia = self.contraseniaInput.get(), 
            email       = self.emailInput.get()
        )
        self.root.destroy()
        datosLogin.iniciarSesion()
        