from flask import Flask, make_response, render_template, request, jsonify
from gestor import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultaMaterias', methods=['POST'])
def consultaMaterias():
    unAlumno = Alumno()
    estados_plan2018 = request.json['estados']
    cargarBD(unAlumno)
    cargarEstados2018(estados_plan2018)
    estados_plan2023 = actualizarEstados2023()
    
    # Crear la respuesta utilizando make_response
    response = make_response(jsonify(estados_plan2023))
    
    # Agregar encabezados de control de caché
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    
    # Devolver la respuesta
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)    
