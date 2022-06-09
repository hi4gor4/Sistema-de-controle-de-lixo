import json
from time import sleep
from types import SimpleNamespace
import asyncio
import requests

class caminhao():
    lixeiras = []
    ip = "" 
    
    def __init__(self, ip):
        self.ip = ip
        print("Caminhao inicializado")
        
    #Criar rota de caminhao
    def readJson(self):
        resposta = requests.get(self.ip + ":5000/setor/a")
        self.lixeiras = resposta.json
    
    #Criar rota de caminhao
    def esvaziar(self):
        lixeira = []
        if self.lixeiras.__len__ <= 1:
            return 0
        sleep(5)
        lixeira = self.lixeiras.pop(0)
        lixeira['ocupacao'] = 0
        resposta = requests.post(self.ip + "5000/setor/a", lixeira)
        return resposta.status_code

if __name__ == '__main__':
    ip = input("Digite o ip: \n")
    caminhao = caminhao()
    
    while(True):
        print(caminhao.readJson())
        caminhao.esvaziar()
    
        

