from distutils.log import debug
from ensurepip import version
from turtle import title
from flask import Flask
from flask_restful import Api

class ServerApi():

    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['JSON_AS_ASCII']= False

        self.api = Api(self.app)
    def run(self,):
        self.app.run(
            debug = True
        )

serverApi = ServerApi()