import json

from connection import Connection


query = ''
class Base:
    def setNewUser(self, usr):
        try:
            res = []
            msg = {}
            cur = Connection()
            data = [usr.nombre[:2] + usr.apellidop[:2] + usr.correo[:2],
                usr.nombre, usr.apellidop, usr.apellidom, usr.fec_nacimiento, usr.edo_nacimiento,
                usr.nvl_estudios, usr.genero, usr.correo, usr.password, usr.movil]
            query = 'insert into usuario ' \
                    '(cve_usuario, nombre, apellidop, apellidom, fec_nacimiento, edo_nacimiento, nvl_estudio,' \
                    'genero, correo, password, movil, status)' \
                    'values(' \
                    ':1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, 1)'
            operacion = cur.executeQuery(query, data)
        except Exception as ex:
            print('Error en base')
            print(ex)
            msg = {
                'operacion': False,
                'msg': 'Error en Base de Datos'
            }
        finally:
            res.append(msg)
            print(res)
        return res

    def getUser(self, usr):
        res = []
        msg = {}
        try:
            cur = Connection()
            query = 'select cve_usuario, nombre,' \
                    'apellidop, apellidom, fec_nacimiento, edo_nacimiento, nvl_estudio,' \
                    ' correo, movil, genero,  ' \
                    ' password, foto_perfil ' \
                    ' from C##DATAADAM.usuario where correo = :1 and password = :2'
            data = [usr.correo, usr.password]
            dataBD = cur.executeSelect(query, data)
            for row in dataBD:
                obj = {
                        "cve_usuario": row[0],
                        "nombre": row[1],
                        "apellidop": row[2],
                        "apellidom": row[3],
                        "fec_nacimiento": row[4],
                        "edo_nacimiento": row[5],
                        "nvl_estudio": row[6],
                        "correo": row[7],
                        "movil": row[8],
                        "genero": row[9],
                        "password": row[10],
                        "foto_perfil": row[11]
                    }
                res.append(obj)
        except Exception as ex:
            print('Error en base')
            print(ex)
            msg = {
                'operacion': False,
                'msg': 'Error en Base de Datos'
            }
            res.append(msg)
        finally:
            print(res)
        return res

    def getStatus(self, cve_usuario):
        res = []
        msg = {}
        try:
            cur = Connection()
            query = 'select status ' \
                    ' from C##DATAADAM.solicitudes ' \
                    'where cve_usuario = :1 and fecha = (select max(fecha) from solicitudes)'
            data = [cve_usuario]
            dataBD = cur.executeSelect(query, data)
            for row in dataBD:
                status = False
                descStatus = ''
                switcher = {
                    1: 'Tu solicitud sigue en proceso de validación',
                    2: 'Lo sentimos, la solicitud ingresada fue rechazada',
                    3: '¡Felicidades tu solicitud ha sido aprobada!'
                }
                descStatus = switcher.get(row[0])
                obj = {
                    'status': row[0] == 3 if True else False,
                    'descripcion': descStatus
                }
                res.append(obj)
        except Exception as ex:
            print('Error en base')
            print(ex)
            msg = {
                'operacion': False,
                'msg': 'Error en Base de Datos'
            }
            res.append(msg)
        finally:
            print(res)
        return res
    def setSolicitud(self, usr):
        try:
            res = []
            msg = {}
            operacion = False
            cur = Connection()
            data = [ usr.cve_usuario, usr.ingreso, usr.gasto,
                usr.ine_inverso, usr.ine_anverso
            ]
            query = 'insert into C##DATAADAM.solicitudes ' \
                    '(cve_solicitud, cve_usuario, ingreso, gasto_mensual, ine_inverso, ine_anverso, status, fecha)' \
                    'values(' \
                    '(select max (cve_solicitud+1) from C##DATAADAM.solicitudes), :1, :2, :3, :4, :5, 1, sysdate)'
            operacion = cur.executeQuery(query, data)
            msg = {
                "operacion": operacion,
                'msg': '¡Felicidades! Tu información fue recibida, en breve daremos respuesta a tu solicitud'
            }
        except Exception as ex:
            print('Error en base')
            print(ex)
            msg = {
                'operacion': operacion,
                'msg': 'Error en Base de Datos'
            }
        finally:
            res.append(msg)
            print(res)
        return res


    def get_solicitudes(self):
        try:
            res = []
            cur = Connection()
            query = 'select us.nombre, us.apellidop, us.apellidom, us.correo, soli.fecha, soli.ingreso, soli.gasto_mensual, soli.status, us.cve_usuario, soli.cve_solicitud, soli.cve_producto from C##DATAADAM.usuario  us, C##DATAADAM.solicitudes  soli WHERE us.cve_usuario = soli.cve_usuario'

            res = cur.executeSelectAll(query)
        except Exception as ex:
            print('Error en base')
            print(ex)
            msg = {
                'operacion': False,
                'msg': 'Error en Base de Datos'
            }
            res.append(msg)
        finally:
            print(res)
        return res

    def aprobar_solicitudes(self, id, aprobacion):
        res = []
        msg = {}
        try:
            cur = Connection()
            query = 'update C##DATAADAM.solicitudes set status = :1 where cve_solicitud = :2 '
            data = [aprobacion, id]
            respuesta = cur.executeQuery(query, data)
        except Exception as ex:
            print('Error en base')
            print(ex)
            msg = {
                'operacion': False,
                'msg': 'Error en Base de Datos'
            }
            respuesta.append(msg)
        finally:
            print(respuesta)
        return respuesta

    def rechazar_solicitudes(self, id, aprobacion):
        res = []
        msg = {}
        try:
            cur = Connection()
            query = 'update C##DATAADAM.solicitudes set status = :1 where cve_solicitud = :2 '
            data = [aprobacion, id]
            respuesta = cur.executeQuery(query, data)
        except Exception as ex:
            print('Error en base')
            print(ex)
            msg = {
                'operacion': False,
                'msg': 'Error en Base de Datos'
            }
            respuesta.append(msg)
        finally:
            print(respuesta)
        return respuesta

