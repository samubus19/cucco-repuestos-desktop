import requests
import json
import os
import LectorToken

class EmpresaController():

    def obtenerDatosEmpresa(self):
        headers = {
            'Authorization' : LectorToken.obtenerToken()
        }
        req           = requests.get('http://localhost:4000/cucco-repuestos/all', headers=headers)

        datosEmpresaJson  = json.loads(req.text)
        return datosEmpresaJson
    
    def editarDatosEmpresa(self, nombre, direccion, telefono, email, sitio_web):
        headers = {
            'Authorization' : LectorToken.obtenerToken()
        }
        
        body = {
            'nombre'    : nombre,
            'direccion' : direccion,
            'telefono'  : telefono,
            'email'     : email,
            'sitio_web' : sitio_web
        }
        
        req           = requests.put(f'http://localhost:4000/cucco-repuestos', headers=headers, data=body)

        res  = json.loads(req.text)
        return res