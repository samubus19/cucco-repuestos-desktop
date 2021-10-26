from tkinter import ttk
import tkinter


FUENTE_1        = 'PT Sans'
COLOR_1         = '#F44336' #Anaranjado
COLOR_2         = '#F2F2F2' #Gris claro
COLOR_3         = '#E51E0F' #Anaranjado oscuro
COLOR_BLANCO    = '#FFFFFF'
COLOR_NEGRO     = '#000000'
ESTILO_FUENTE_1 = 'bold'
TAMAÑO_FUENTE_S = 10
TAMAÑO_FUENTE_M = 12
TAMAÑO_FUENTE_L = 14


def estiloBotonNormal(layout_padre):
    style = ttk.Style(layout_padre)
    style.configure(
        'botonNormal.TButton', 
        foreground  = COLOR_BLANCO, 
        background  = COLOR_1, 
        font        = (FUENTE_1, TAMAÑO_FUENTE_M),
        relief      = 'flat',
    )
    style.map('botonNormal.TButton', background=[('active','red')])

def estiloBotonCancelar(layout_padre):
    style = ttk.Style(layout_padre)
    style.configure(
        'botonCancelar.TButton', 
        foreground  = COLOR_1, 
        background  = COLOR_BLANCO, 
        font        = (FUENTE_1, TAMAÑO_FUENTE_M),
        borderwidth = 1,
        bordercolor = COLOR_1,
        relief      = 'flat'
    )
    style.map('botonCancelar.TButton', 
        background=[('active',COLOR_1)],
        foreground=[('active', COLOR_BLANCO)])

def estiloLabel1(layout_padre):
    style = ttk.Style(layout_padre)
    style.configure(
        'etiqueta.TLabel', 
        foreground = COLOR_NEGRO, 
        background = COLOR_2, 
        font = (FUENTE_1, TAMAÑO_FUENTE_M)
    )

def estiloLabelTitulo(layout_padre):
    style = ttk.Style(layout_padre)
    style.configure(
        'titulo.TLabel', 
        foreground = COLOR_1, 
        background = COLOR_2, 
        font = (FUENTE_1, TAMAÑO_FUENTE_L, ESTILO_FUENTE_1)
    )

def estiloEntries(layout_padre):
    pass

def estiloTablas(layout_padre):
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=(FUENTE_1, TAMAÑO_FUENTE_S), foreground=COLOR_NEGRO) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=(FUENTE_1, TAMAÑO_FUENTE_M, ESTILO_FUENTE_1), background=COLOR_1, foreground=COLOR_BLANCO) # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
    style.map("Treeview.Heading",
                background = [('active', COLOR_3)],
                foreground = [('active', COLOR_BLANCO)]
                )