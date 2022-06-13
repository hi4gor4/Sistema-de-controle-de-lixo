from pickle import TRUE
from pyclbr import Class
from unicodedata import name
import paho.mqtt.client as mqtt
from flask import Flask
import json
import requests
from time import sleep

class Setor:
    ip = "25.81.85.89"
    name = ""
    message = ""
    lixeiras = []

    def __init__(self, name):
        self.name = name
        #self.lixeiras = [{"nome": name}]

    def writeJson(self):
        with open(self.name + ".json", "w") as write_file:
            json.dump(self.lixeiras, write_file, default= lambda o: o.__dict__)

    def addLixeira(self, Lixeira):
        if sum(map(lambda x: x.localizacao == Lixeira.localizacao, self.lixeiras)) == 0:
            self.lixeiras.append(Lixeira)
            self.lixeiras.sort(key=lambda x: x.ocupacao,  reverse= True)
            return 1
        else:
            return -1
        

    def esvazia(self):
       resposta = requests("http://" + self.ip + ":5000/setor/" + self.name)        

    

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

    def on_connect(client, userdata, flags, rc):
        print("Conectou MQTT")
        client.subscribe(setor.name + "/#", 1)
    

    def on_message(client, userdata, message):
        info = ""
        msg = message.payload
        msg = msg.decode()
        info = msg.split(" ")
        lixeira = Lixeira(info[0], info[1], info[2])
        lixeira.localizacao
        if setor.addLixeira(lixeira) != 1:
            for x in setor.lixeiras:
                if lixeira.localizacao == x.localizacao:
                    x.ocupacao = lixeira.ocupacao
            setor.lixeiras.sort(key=lambda x: x.ocupacao,  reverse= True)
        setor.writeJson()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("mqtt", password="2314")
    client.connect("localhost")
    client.loop_forever()
    while(True):     
       setor.esvazia()
       sleep(1)
