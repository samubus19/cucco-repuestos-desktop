import itertools 
import os
import os.path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.units import cm
from tkinter import messagebox 
from reportlab.lib.units import inch 
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from Controladores import ClienteController, VentasController, EmpresaController
from Helpers.Format_fechas import formatearFecha
from LectorToken import obtenerToken


fontRemito	= "Helvetica"
data  		= []
data1 		= [("Nombre", "Descripcion", "Marca", "Cantidad")]

class ImpresorPdf:
	def __init__(self, id_venta):
		self.idVenta 	  = id_venta
		self.datosEmpresa = self.obtenerDatosEmpresa()
		self.datosVenta   = self.obtenerDatosVenta() 
		self.datosCliente = self.obtenerDatosCliente()
  
	def grouper(self,iterable, n):
		args = [iter(iterable)] * n
		return itertools.zip_longest(*args)

	def export_to_pdf(self):
			now 	   = datetime.now()
			dt_string  = now.strftime("%d%m%Y%H%M%S")
			nombrePdf  = "Factura_"+str(self.datosVenta['_id']).zfill(15)+"_"+dt_string+".pdf"
			# nombrePdf  = "Remito_"+str(resultOrdenTrabajo[7]).zfill(15)+".pdf"
			# nombrePdf  	= 'archivoPdf.pdf'
			print(os.path.join(os.getcwd(), 'Facturas_pdf/'))
			rutaPdf    = os.path.join(os.getcwd(), 'Facturas_pdf/')

			c 	       = canvas.Canvas(rutaPdf+nombrePdf, pagesize=A4)

			w, h 	   = A4
			max_rows_per_page = 29
			xEmpresa   = 10
			xCliente   = 350
			
			#c.rect(10, h - 810, 575, 570)

			for rows in self.grouper(data, max_rows_per_page):

				c.drawImage(os.path.join(os.getcwd(), 'Imagenes/logo_naranja.png'), 30, h - 205, width=190, height=190)
				# print(os.path.join(os.getcwd(), 'Imagenes/logo_naranja.png'))
	
	
				text = c.beginText(xCliente, h - 30)
				text.setFont(fontRemito, 18)
				text.textLine("FACTURA")
				c.drawText(text)

				text = c.beginText(xCliente, h - 50)
				text.setFont(fontRemito, 9)
				text.textLine("N°: "+str(self.datosVenta['_id']))
				c.drawText(text)

				text = c.beginText(xCliente, h - 68)
				text.textLine("Empresa: "+ str(self.datosEmpresa[0]['nombre']))		
				c.drawText(text)

				text = c.beginText(xCliente, h - 86)
				text.textLine("Direccion: "+str(self.datosEmpresa[0]['direccion']))
				c.drawText(text)

				text = c.beginText(xCliente, h - 104)
				text.textLine("Telefono: "+str(self.datosEmpresa[0]['telefono']))
				c.drawText(text)

				text = c.beginText(xCliente, h - 122)
				text.textLine("Correo Electronico: "+str(self.datosEmpresa[0]['email']))
				c.drawText(text)

				text = c.beginText(xCliente, h - 140)
				text.textLine("Sitio Web: "+str(self.datosEmpresa[0]['sitio_web']))
				c.drawText(text)
				
				text = c.beginText(xCliente, h - 158)
				text.textLine("Cliente: "+self.datosCliente['nombre'] + " " + self.datosCliente['apellido'])
				c.drawText(text)

				text = c.beginText(xCliente, h - 176)
				text.textLine('Documento: ' + self.datosCliente['documento'])
				c.drawText(text)

				text = c.beginText(xCliente, h - 194)
				text.textLine("Fecha de venta: "+ formatearFecha(str(self.datosVenta['createdAt'])))
				c.drawText(text)

				c.rect(10, h - 216, 575, 205)
				c.rect(270, h - 55, 40, 40)

				text = c.beginText(272, h - 55)
				text.setFont(fontRemito, 55)
				text.textLine("X")
				c.drawText(text)

				c.line(290,625,290,787)
    
				#TOTAL DE LA VENTA
				c.line(10,h - 800,570, h - 800)
				text = c.beginText(10, h - 820)
				text.setFont(fontRemito, 14)
				text.textLine("TOTAL")
				c.drawText(text)
				
				text = c.beginText(500, h - 820)
				text.setFont(fontRemito, 14)
				text.textLine(str(self.datosVenta['precio_total']))
				c.drawText(text)
    
				rows1 = data1
				rows  = tuple(filter(bool, rows))
				rows1 = tuple(filter(bool, rows1))

				x_offset  = 10
				y_offset  = 240
				padding   = 15
				xlist = [x + x_offset for x in [0, 170, 340, 460, 575]]
				ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
				
				c.grid(xlist, ylist[:len(rows1) + 1])

				for y1, row1 in zip(ylist[:-1], rows1):	
					for x1, cell1 in zip(xlist, row1):					
						c.setFont(fontRemito, 6.5)	
						c.drawString(x1 + 2, y1 - padding + 3, str(cell1))

				y_offset  = 255
				xlist = [x + x_offset for x in [0, 170, 340, 460, 575]]
				ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]

				for y, row in zip(ylist[:-1], rows):				
					for x, cell in zip(xlist, row):					
						c.setFont(fontRemito, 6.5)	
						c.drawString(x + 2, y - padding + 4, str(cell))
				c.showPage()
    
    
			c.save()


	def obtenerDatosVenta(self):
		ventasController  = VentasController.VentasController()
		return ventasController.obtenerVentaPorId(self.idVenta)
		
	def obtenerDatosEmpresa(self):
		empresaController = EmpresaController.EmpresaController()
		return empresaController.obtenerDatosEmpresa()

	def obtenerDatosCliente(self):
		clienteController = ClienteController.ClienteController()
		return clienteController.obtenerClientePorId(self.datosVenta['id_cliente'])
	

	def selectProducto(self):
		data.clear()
		# print(self.datosVenta['productos'])
		for row in self.datosVenta['productos']:
			nombre      = row['producto']['nombre']
			descripcion = row['producto']['descripcion']
			marca 	    = row['producto']['marca']
			cantidad	= row['cantidad']
			data.append((nombre, descripcion,marca,cantidad))
		self.export_to_pdf()
