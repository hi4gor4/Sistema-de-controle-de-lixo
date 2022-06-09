from pickle import TRUE
from pyclbr import Class
from unicodedata import name
import paho.mqtt.client as mqtt
from flask import Flask
import json
import requests
from time import sleep

class Setor:
    ip = ""
    name = ""   
    clientMqtt = mqtt.Client();
    clientMqtt.on_connect = ''
    clientMqtt.on_message = ''
    message = ""
    lixeiras = []

    def __init__(self, name):
        self.name = name
        #self.lixeiras = [{"nome": name}]
        self.clientMqtt.on_message = self.onMessage
        self.on_connect = self.onConnect
        self.clientMqtt.connect = ("",00,00)

    def writeJson(self):
        with open(self.name + ".json", "w") as write_file:
            json.dump(self.lixeiras, write_file, default= lambda o: o.__dict__)

    def addLixeira(self, Lixeira):
        if self.lixeiras.count(Lixeira.localizacao) == 0:
            self.lixeiras.append(Lixeira)
            self.lixeiras.sort(key=lambda x: x.ocupacao,  reverse= True)
            return 1
        else:
            return -1

    def onMessage(clientMqtt, userdata, msg, self):
        message = msg.playload
        info = message.split(" ")
        lixeira = Lixeira(info[0], info[1], info[2])
        if self.addLixeira(lixeira) != 1:
            value = self.lixeiras.index(lixeira.localizacao)
            self.lixeiras[value].ocupacao = lixeira.ocupacao
            self.lixeiras.sort(key=lambda x: x.ocupacao,  reverse= True)
        self.writeJson()
        print(info[0], info[1], info[2] + "\n")

    def esvazia(self):
        resposta = requests(self.ip + ":5000/setor/" + self.name)        

    
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

if __name__ == "__main__":
    nome = input("Digite o nome do setor: \n")
    setor = Setor(nome)
    setor.clientMqtt.loop()
    while(True):
        setor.esvazia()
        sleep(1)
