from asyncio.windows_events import NULL
from hashlib import new
from http import client
from pydoc_data.topics import topics
from random import random
from time import sleep
import paho.mqtt.client as mqtt
import random
    
class Lixeira(object):
    capacidade = 0
    ocupacao = 0
    localizacao =''
    topico = ''
    client = mqtt.Client()
    
    def __init__(self, capacidade, localizacao):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.topico = self.getTopico()
        self.capacidade = capacidade
        self.ocupacao = 0
        self.localizacao = localizacao

    def on_connect(client, userdata, flags, rc):
        
        # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
        # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
        client.subscribe("hiago23rangel@gmail.com/luz1")

    def on_message(client, userdata, msg):
        #print(msg.topic+" -  "+str(msg.payload))
        return msg.payload

    def  getTopico(self):
        self.client.connect("www.maqiatto.com", 1883, 60)
        client.publish("hiago23rangel@gmail.com/luz1", self.localizacao)
        sleep(2)
        return self.client.subscribe("hiago23rangel@gmail.com/luz2").on_message()
    
    def changeState(self):
        self.client.publish(self.topico,("{} {} {}".format(self.localizacao, self.capacidade,self.ocupacao  )))
    
    #Metodo para encher a lixeira aleatoriamente com o tempo, Testar tempo para encher e se o espaço dado entre os valores é suficiente
    def encher(self):
        value = random.randint(0, 100000)
        if value >= 500 and value <= 600:
            if self.ocupacao >= self.capacidade:
                self.ocupacao += 10
                self.changeState()
    
def main():
    capacidade = input("Digite a capacidade da lixeira \n")
    rua = input("Digite a Rua Dessa lixeira")

    Lixeira = Lixeira(capacidade, rua)

    while(True):
        Lixeira.encher()

if __name__ == "__main__":
    main()
    
    #client.on_connect = on_connect
    #client.on_message = on_message
    #client.username_pw_set("hiago23rangel@gmail.com", password="2314")

    # Conecta no MQTT Broker, no meu caso, o Maquiatto
    #client.connect("www.maqiatto.com", 1883, 60)

    #client.publish("hiago23rangel@gmail.com/luz1", "Oi, aqui é um teste")

    # Inicia o loop
    

  