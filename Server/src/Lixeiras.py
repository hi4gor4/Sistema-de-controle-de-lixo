
import json
from flask import Flask, request
from flask_restful import Api, Resource
from Server import serverApi

app = serverApi.app
api = serverApi.api
lixo = []
lixeiraVazia = {}
class Lixeira(Resource):
    
    @app.route("/setor/<setor>/esvazia", methods = ['GET'])
    def getEsvazia(setor):
        if(lixeiraVazia['Setor'] == setor ):
            return lixeiraVazia
        else:
            return {}

    @app.route("/setor/<setor>/esvazia", methods = ['POST'])
    def postEsvazia(setor):
        lixeiraVazia = request.get_json()
        return lixeiraVazia
    

    @app.route("/setor/<setor>", methods =['POST'])
    def getLixeira(setor):
        entrada = request.get_json()
        for j in range(0, len(entrada)):
            lixeira = entrada[j]
            existe = False
            for i in range(0, len(lixo)):
                cl = lixo[i]
                if (setor  == cl['setor']):
                    if(lixeira['localizacao'] == cl['localizacao']):
                        cl = {'setor': setor, 'localizacao': lixeira['localizacao'], 'capacidade': lixeira['capacidade'], 'ocupacao': lixeira['ocupacao']}
                        existe = True
            if(not existe):
                lixo.append( {'setor': setor, 'localizacao': lixeira['localizacao'], 'capacidade': lixeira['capacidade'], 'ocupacao': lixeira['ocupacao']})

    @app.route("/setor/caminhao", methods = ['GET'])
    def caminhaoSaida():
        lixo.sort(key=lambda x: x.ocupacao,  reverse= True)
        
        if(len(lixo)>=10):
            saida = []
            for j in range(0, len(lixo)):
                saida.append(lixo[j])
            return json.dumps(saida, default= lambda o: o.__dict__)
        else:
            return json.dumps(lixo, default= lambda o: o.__dict__)



