from random import random
from time import sleep
import paho.mqtt.client as mqtt
import random
import requests

class Lixeira(object):
    capacidade = 0
    ocupacao = 0
    localizacao = ''
    topico = ''
    client = mqtt.Client()
    
    def __init__(self, capacidade, localizacao):
        #self.client.username_pw_set("mqtt", password = "2314")
        self.client.connect("localhost")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        #self.topico = self.getTopico()
        self.capacidade = capacidade
        self.ocupacao = 0
        self.localizacao = localizacao
        self.client.loop_start()

    def on_connect(client, userdata, flags, rc):
        
        # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
        # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
        client.subscribe("/setor")

    def on_message(client, userdata, msg):
        print(msg.topic+" -  "+str(msg.payload))
        return msg.payload

    def  getTopico(self):
      #  self.client.connect("25.81.87.101", 1883, 60)
        self.client.publish("setor", self.localizacao)
        sleep(2)
        
    
    def changeState(self):
        self.client.publish("/setor/",("{} {} {}".format(self.localizacao, self.capacidade, self.ocupacao)))
    
    #Metodo para encher a lixeira aleatoriamente com o tempo, Testar tempo para encher e se o espaço dado entre os valores é suficiente
    def encher(self):
        value = random.randint(0, 1000000000)
        if value >= 500 and value <= 600:
            if self.ocupacao < self.capacidade:
                self.ocupacao += 10
                self.changeState()
    
def main():
    capacidade = int(input("Digite a capacidade da lixeira \n"))
    rua = input("Digite a rua da lixeira \n")

    lixeira = Lixeira(capacidade, rua)
    while(True):
        lixeira.encher()

if __name__ == "__main__":
    main()
    
    #client.on_connect = on_connect
    #client.on_message = on_message
    #client.username_pw_set("hiago23rangel@gmail.com", password="2314")

    # Conecta no MQTT Broker, no meu caso, o Maquiatto
    #client.connect("www.maqiatto.com", 1883, 60)

    #client.publish("hiago23rangel@gmail.com/luz1", "Oi, aqui é um teste")

    # Inicia o loop
    

  