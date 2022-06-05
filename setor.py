from pyclbr import Class
from unicodedata import name
import paho.mqtt.client as mqtt
from http import client

class setor:
    name = ""   
    clientMqtt = mqtt.Client();
    clientMqtt.on_connect = ''
    clientMqtt.on_message = ''
    message = ""
    lixeiras = []

    def __init__(self, name) -> None:
        self.name = name
        self.clientMqtt.on_message = self.onMessage
        self.on_connect = self.onConnect
        self.clientMqtt.connect = ("",00,00)
        pass
    
    def addLixeira(self, Lixeira):
        if self.lixeiras.count(Lixeira.localizacao) == 0:
            self.lixeiras.append(Lixeira)
            self.lixeiras.sort(Lixeira.ocupacao)
            return 1
        else:
            return -1

    def onMessage(clientMqtt, userdata, msg, self):
        message = msg.playload
        info = message.split(" ")
        Lixeira = Lixeira(info[0], info[1], info[2])
        if self.addLixeira(Lixeira) != 1:
            value = self.lixeiras.index(Lixeira.localizacao)
            self.lixeiras[value].ocupacao = Lixeira.ocupacao
        print(info[0], info[1], info[2] + "\n")

    
    def onConnect(clientMqtt, userdata, flags, rc):
        clientMqtt.subscribe(name + "/#")

class Lixeira:
    capacidade = 0
    ocupacao = 0
    localizacao = ""

    def __init__(self, localizacao, capacidade, ocupacao):
        self.capacidade = capacidade
        self.ocupacao = ocupacao
        self.localizacao = localizacao
        pass

def main():
    nome = input("Digite o nome do setor")
    setor = setor(nome)

if __name__ == "__main__":
    main()