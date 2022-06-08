
import json
from flask import Flask, request



app = Flask(__name__)
app.config['JSON_AS_ASCII']= False
app.jsonlixeiras = {}
        
@app.route("/")
def root():
    return app.jsonlixeiras

@app.route("/lixo", methods =['POST'])
def getLixeira():
    body = request.get_json()
    app.jsonlixeiras = body
    return "Informações recebidas"
    
app.run(debug = True)
    