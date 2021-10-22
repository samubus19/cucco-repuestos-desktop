import os
import json

def obtenerToken():
        TOKEN_FILE_PATH = os.path.join(os.getcwd(), 'token.json')
        with open(TOKEN_FILE_PATH) as archivo:
                token = json.load(archivo)
                return token['token']