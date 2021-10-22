import tkinter
import sys
from Singleton import *
from Controladores.UsuarioController import *

@singleton
class LoginView(object):
    def __init__(self) -> None:


        self.root             = tkinter.Tk()

        self.usuarioInput     = tkinter.StringVar()
        self.contraseniaInput = tkinter.StringVar() 
        self.emailInput       = tkinter.StringVar() 

        self.tbUsuario        = tkinter.Entry(self.root, bd=2, width=30, fg='#000000',bg='#ffffff', font=('Helvetica', 10), textvariable = self.usuarioInput)
        self.tbUsuario.grid(row="1", column="0", padx=10,pady=25, columnspan=1, sticky="ns")       
        
        self.tbContrasenia    = tkinter.Entry(self.root, width=30, fg='#000000', bd=2, bg='#ffffff', font=('Helvetica', 10), textvariable = self.contraseniaInput)
        self.tbContrasenia.grid(row="2", column="0", padx=10,pady=25, columnspan=1, sticky="ns")
        
        self.tbEmail       = tkinter.Entry(self.root, width=30, fg='#000000', bd=2, bg='#ffffff', font=('Helvetica', 10), textvariable = self.emailInput)
        self.tbEmail.grid(row="3", column="0", padx=10,pady=25, columnspan=1, sticky="ns")

        #Boton Ingresar
        self.btnIngresar = tkinter.Button(self.root, text="Ingresar", width=35, fg='#ffffff',bg='#2222cc', bd=3, relief="flat", font=('Helvetica', 12), command=self.iniciarSesion)
        self.btnIngresar.grid(row="4", column="0",pady=0.5, columnspan=1, sticky="nsew")

        #Boton Cancelar
        self.btnCancelar      = tkinter.Button(self.root, text="Salir", width=35, fg='#ffffff', bg='#2222cc', bd=3, relief="flat", font=('Helvetica', 12), command = self.root.destroy)
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
        