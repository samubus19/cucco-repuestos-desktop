import json

def getToken():
    with open('E:/SAMUEL-E/UNIVERSIDAD/4° AÑO/ING_DE_SOFTWARE/Trabajo-Final-Cucco-Repuestos/cucco-repuestos-desktop/token.json') as archivo:
        token = json.load(archivo)
        print(token['token'])
        return token['token']

getToken()