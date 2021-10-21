import tkinter

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
        self.btnProductos = tkinter.Button(self.root, bd=1, relief="ridge", compound="top",font=(fuente,8,negrita),fg=colorNegro, bg=colorBlanco, text="Productos\n\n")
        self.btnProductos.grid(row=0, column=4, sticky="w", columnspan=1)

        #ACCESO RAPIDO, BUSCAR PRODUCTOS
        self.btnBuscarProducto = tkinter.Button(self.root, bd=1, relief="ridge",font=(fuente,8,negrita),compound="top", fg=colorNegro, bg=colorBlanco, text="Buscar \nProducto\n")
        self.btnBuscarProducto.grid(row=0, column=5, sticky="w", columnspan=1)

        #ACCESO RAPIDO, BUSCAR REMITO
        self.btnBuscarRemito = tkinter.Button(self.root, bd=1, relief="ridge",font=(fuente,8,negrita), compound="top", fg=colorNegro, bg=colorBlanco, text="Buscar\nRemito\n")
        self.btnBuscarRemito.grid(row=0, column=9, sticky="ew")

        #ACCESO RAPIDO, REPORTES ORDENES TRABAJO
        self.btnReporte = tkinter.Button(self.root, bd=1, relief="ridge",font=(fuente,8,negrita), compound="top", fg=colorNegro, bg=colorBlanco, text="Reportes\nOrdenes\nde Trabajo")
        self.btnReporte.grid(row=0, column=10, sticky="ew")

        #ACCESO RAPIDO, CONFIGURACIONES
        self.btnConfiguraciones = tkinter.Button(self.root, bd=1, relief="ridge",font=(fuente,8,negrita),compound="top", fg=colorNegro, bg=colorBlanco, text="Config\n\n")
        self.btnConfiguraciones.grid(row=0, column=11, sticky="w", columnspan=1)
