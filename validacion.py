import time
from connection import Connection
class Validacion:
    def validaCredito(self, cve_usuario, status):
        try:
            res = []
            operacion = False
            msg = 'No se pudo actualizar el registro'
            cur = Connection()
            data = [status, cve_usuario]
            query = 'update solicitudes ' \
                        'set status = :1 ' \
                        'where cve_usuario = :2 and fecha = (select max(fecha) from solicitudes)'
            operacion = cur.executeQuery(query, data)
            if operacion:
                msg = 'Se ha dado respuesta de la solicitud'

        except Exception as ex:
            print('Error en base')
            print(ex)
        finally:
            res.append({
                'operacion': operacion,
                'msg': msg
            })
            print(res)
        return res
