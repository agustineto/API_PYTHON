from flask import Flask, request
from flask_cors import CORS
from usuario import Usuario
from Solicitud import Solicitud
from base import Base
from threading import Timer
from validacion import Validacion
import random
app = Flask(__name__)

main = CORS(app)
bs = None
@app.route('/api/Solicitud', methods=["POST"])
def setSolicitud():
    usr = Solicitud()
    usr.constructor(
        request.json['cve_usuario'],
        request.json['ingreso'],
        request.json['gasto'],
        request.json['ine_inverso'],
        request.json['ine_anverso']
    )
    v = Validacion()
    count = random.randint(20, 60)
    status = 2
    if (usr.ingreso-usr.gasto) > 1999:
        status = 3
    print(status)
    r = Timer(count, v.validaCredito, (usr.cve_usuario, status))
    print('timer ')
    print(count)
    r.start()
    bs = Base()
    res = bs.setSolicitud(usr)
    return res

@app.route('/api/setUser', methods=["POST"])
def setUsers():
    usr = Usuario()
    usr.constructor(
        request.json['nombre'],
        request.json['apellidop'],
        request.json['apellidom'],
        request.json['fec_nacimiento'],
        request.json['edo_nacimiento'],
        request.json['nvl_estudio'],
        request.json['genero'],
        request.json['correo'],
        request.json['password'],
        request.json['movil'],
        request.json['foto_perfil']
    )
    print(usr)
    bs = Base()
    res = bs.setNewUser(usr)
    return res

@app.route('/api/getUser', methods=["GET"])
def getUser():
    usr = Usuario()
    usr.login(
        request.json['correo'],
        request.json['password']
    )
    bs = Base()
    res = bs.getUser(usr)
    return res

@app.route('/api/getStatus/<cve_usuario>', methods=["GET"])
def getStatus(cve_usuario):
    bs = Base()
    res = bs.getStatus(cve_usuario)
    return res

@app.route('/api/solicitudes', methods=['GET', 'POST'])
def get_solicitudes():
    if request.method == 'GET':
        bs = Base()
        respuesta = bs.get_solicitudes()
    return respuesta


@app.route('/api/solicitudes/<id>', methods=['PUT'])
def aprobar_solicitud(id):

    if request.method == 'PUT':
        respuesta = 'solicitud put' + id
        id = request.json['id']
        aprobacion = request.json['aprobacion']
        bs = Base()
        bs.aprobar_solicitudes(id, aprobacion)

    return respuesta

@app.route('/api/solicitudes/<id>', methods=['PUT'])
def solicitud_rechazada(id):

    if request.method == 'PUT':
        respuesta = 'solicitud put' + id
        id = request.json['id']
        aprobacion = request.json['aprobacion']
        bs = Base()
        bs.rechazar_solicitudes(id, aprobacion)

    return respuesta



if __name__ == '__main__':
    app.run('0.0.0.0', 1515, True)