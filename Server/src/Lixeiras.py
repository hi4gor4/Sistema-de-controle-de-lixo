
import json
from flask import Flask, request
from flask_restful import Api, Resource
from Server import serverApi

app = serverApi.app
api = serverApi.api
lixo = []
setores = []
class Lixeira(Resource):
    
    @app.route("/setor/<nome>", methods = ['GET'])
    def root(nome):
        for i in range(0, len(lixo)):
            cl = lixo[i]
            print("---{}---".format(nome))
            if (nome == cl['Nome']):
                return lixo[i]["Json"]
        return "Vazio"

    @app.route("/setor/<nome>", methods =['POST'])
    def getLixeira(nome):
        body = {"Nome": nome, "Json": request.get_json()}
        for i in range(0, len(lixo)):
            cl = lixo[i]
            if (nome == cl['Nome']):
                lixo[i] = body
                return body
        lixo.append(body)
        return(body)
    @app.route("/setores/<nome>", methods = ['POST'])
    def addSetor(nome):
        for i in range(0, len(setores)):
            cl = setores[i]
            if (nome == cl['Nome']):
                return nome
        setores.append({"Nome": nome})
        return nome

    @app.route("/setores", methods = ['GET'])
    def getSetores():
        return json.dumps(setores, default= lambda o: o.__dict__)

