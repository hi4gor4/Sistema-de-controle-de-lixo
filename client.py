# PARA OUVIR UM TÓPICO

# Para instalar o paho-mqtt use o comando pip install paho-mqtt
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  
    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("hiago23rangel@gmail.com/luz1")
    
# Callback responável por receber uma mensagem publicada no tópico acima
def on_message(client, userdata, msg):
    print(msg.topic+" -  "+str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Seta um usuário e senha para o Broker, se não tem, não use esta linha
client.username_pw_set("hiago23rangel@gmail.com", password="2314")

# Conecta no MQTT Broker, no meu caso, o Maquiatto
client.connect("www.maqiatto.com", 1883, 60)

#client.publish("hiago23rangel@gmail.com/luz1", "Oi, aqui é um teste")

# Inicia o loop
client.loop()

client.publish("hiago23rangel@gmail.com/luz1", "Oi, aqui é um teste")