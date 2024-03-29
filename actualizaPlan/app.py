"""
Descripción de la web

"""

from flask import Flask, render_template, request, jsonify
from gestor import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultaMaterias', methods=['POST'])
def consultaMaterias():
    estados_plan2018 = request.json['estados']
    cargarBD()
    cargarEstados2018(estados_plan2018) 
    estados_plan2023 = actualizarEstados2023()
    
    return jsonify(estados_plan2023)

if __name__ == '__main__':
    app.run(debug=True)

