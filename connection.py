import cx_Oracle
constr = 'C##DATAADAM/C##DATAADAM@107.180.100.184:1553/cdocqac'

class Connection:
    def executeQuery(self, query, data):
        msg = False
        try:
            conn = cx_Oracle.connect(constr)
            cur = conn.cursor()
            cur.execute(query, data)
            conn.commit()
            msg = True
        except Exception as ex:
            print('Error al ejecutar query: ' + query)
            print(ex)
            error = ex
            msg = False
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
        return msg
    def executeSelect(self, query, data):
        try:
            res = []
            conn = cx_Oracle.connect(constr)
            cur = conn.cursor()
            cur.execute(query, data)
            data = cur.fetchall()
            print(data)
        except Exception as ex:
            print('Error al ejecutar query: ' + query)
            print(ex)
            msg = {
                'operacion': False,
                'msg': 'Error al ejecutar la consulta'
            }
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
        return data

    def executeSelectAll(self, query):
        try:
            res = []
            conn = cx_Oracle.connect(constr)
            cur = conn.cursor()
            cur.execute(query)
            data = cur.fetchall()
            print(data)
        except Exception as ex:
            print('Error al ejecutar query: ' + query)
            print(ex)
            msg = {
                'operacion': False,
                'msg': 'Error al ejecutar la consulta'
            }
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
        return data
