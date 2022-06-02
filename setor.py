from pyclbr import Class
import paho.mqtt.client as mqtt
from http import client

class setor:    
    clientMqtt = mqtt.Client();
    clientMqtt.on_connect = ''
    clientMqtt.on_message = ''
    message = ""

    def __init__(self) -> None:
        self.clientMqtt.on_message = self.onMessage
        self.on_connect = self.onConnect
        self.clientMqtt.connect = ("",00,00)
        pass
    
    def onMessage(clientMqtt, userdata, msg):
        message = msg
    
    def onConnect(clientMqtt, userdata, flags, rc):
        clientMqtt.subscribe("")