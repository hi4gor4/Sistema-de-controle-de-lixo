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
    
    def exibir(self):
        print("Lixeiras: \n")
        print(self.lixeiras['setor'] + " " + self.lixeiras['localizacao'] + ":  " + self.lixeiras['ocupacao'] + "\n")

    #Criar rota de caminhao
    def readJson(self):
        resposta = requests.get(self.ip + ":5000/setor/caminhao")
        self.lixeiras = resposta.json
    
    #Criar rota de caminhao
    def esvaziar(self):
        lixeira = []
        if self.lixeiras.__len__ <= 1:
            return 0
        sleep(5)
        lixeira = self.lixeiras.pop(0)
        lixeira['ocupacao'] = 0
        resposta = requests.post(self.ip + ":5000/" + lixeira['setor'] + "/esvazia", lixeira)
        return resposta.status_code

if __name__ == '__main__':
    ip = input("Digite o ip: \n")
    caminhao = caminhao(ip)
    
    while(True):
        caminhao.readJson()
        caminhao.exibir()
        caminhao.esvaziar()

    
        

