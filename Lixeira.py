from asyncio.windows_events import NULL
from hashlib import new
from http import client
from pydoc_data.topics import topics
from time import sleep
import paho.mqtt.client as mqtt

    
class Lixeira(object):
    capacidade = 0
    ocupacao = ''
    localizacao =''
    topico = ''
    client = mqtt.Client()
    def __init__(self, capacidade, localizacao):
        self.client.on_connect = on_connect
        self.client.on_message = on_message
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
        self.client.publish(self.topico,("{} {} {} ".format(self.localizacao, self.capacidade,self.ocupacao  )))
    
    
def main():
    Lixeira = Lixeira(200, "Rua A")
    Lixeira.changeState()


if __name__ == "__main__":
    main()
    
    #client.on_connect = on_connect
    #client.on_message = on_message
    #client.username_pw_set("hiago23rangel@gmail.com", password="2314")

    # Conecta no MQTT Broker, no meu caso, o Maquiatto
    #client.connect("www.maqiatto.com", 1883, 60)

    #client.publish("hiago23rangel@gmail.com/luz1", "Oi, aqui é um teste")

    # Inicia o loop
    

  

        
        
