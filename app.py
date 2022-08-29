from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import json
import requests

app = Flask(__name__)

@app.route('/resultado/<resposta>')
def resultado(resposta):
    return render_template('index.html',resposta=resposta)

@app.route('/')
def index(resposta=None):
    return render_template('index.html',resposta=resposta)


@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method == 'POST':
        af = float(request.form['acidez-fixa'])
        av = float(request.form['acidez-volatil'])
        ac = float(request.form['acidez-citrica'])
        ar = float(request.form['acucar-residual'])
        clo =float(request.form['cloretos'])
        ld = float(request.form['livre-dioxido'])
        td = float(request.form['total-dioxido'])
        den = float(request.form['density'])
        ph = float(request.form['ph'])
        su = float(request.form['sulfato'])
        alc = float(request.form['alcohol'])

        data = np.array([[af,av,ac,ar,clo,ld,td,den,ph,su,alc]],np.float64).tolist()
        json_data = json.dumps({"index":['af','av','ac','ar','clo','ld','td','den','ph','su','alc']
                                ,"data":data})
        resposta = requests.post(url='http://localhost:2345/invocations', 
                                 headers={'Content-Type':'application/json'}, 
                                 data=json_data)
        #resposta = str(data)
        return resposta.text


if __name__=='__main__':
    app.run(debug=True)
