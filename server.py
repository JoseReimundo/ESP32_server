import socket
import pymysql
import json
import time, sys

# Variables globales
listenPort = 9090
maxConnections = 2
maxSize = 2048
dataBase = ''

#
class DataBase():
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'JRDMysql2021',
            db = dataBase
        )
        self.cursor = self.connection.cursor()

    def selectAll(self):
        """ query = 'SELECT GPIO, Value \
                FROM {};'.format(dataBase) """
        query = 'SELECT GPIO, Value \
                FROM {};'.format(dataBase)
        try:
            self.cursor.execute(query)
            instances = self.cursor.fetchall()

            dic = {}
            for ins in instances:
                # dic[ins[0]] = int.from_bytes(ins[1], byteorder='big')
                dic[ins[0]] = ins[1]
            response = json.dumps(dic, sort_keys=True)
            # conType = 'application/json'
            conType = 'text/plain'
            length = sys.getsizeof(response)
        except:
            return None
        return response, conType, length

    """ def selectSome(self, elements):
        dic = {}
        try:
            for elem in elements:
                query = 'SELECT name, status \
                        FROM {} \
                        WHERE name=\'{}\';'.format(dataBase, elem)
                self.cursor.execute(query)
                ins = self.cursor.fetchone()
                dic[ins[0]] = ins[1]
            response = json.dumps(dic, sort_keys=True)
            #conType = 'application/json'
            conType = 'text/plain'
            length = sys.getsizeof(response)
        except:
            return None
        return response, conType, length
 """
    def update(self, attributes):
        try:
            for elem in attributes:
                query = 'UPDATE {} \
                        SET Value={} \
                        WHERE GPIO=\'{}\';'.format(dataBase, elem[1], elem[0])
                """ query = 'UPDATE {} \
                        SET active={} \
                        WHERE name=\'{}\';'.format(dataBase, elem[1], elem[0]) """
                self.cursor.execute(query)
                self.connection.commit()
            conType = 'text/plain'
        except:
            return None
        return str(len(attributes)), conType, sys.getsizeof(attributes)

    def close(self):
        self.connection.close()


# Funciones
def httpCheck(requestMess : str):
    """
    * Decripcion : Verifica el formato de la peticion, es decir si el metodo es correcto
    y ademas extrae los posibles atributos y valores para actualizar la BBDD
    * Args:
            - requestMess : El mensaje de petición HTTP recibido del cliente
    * Retorno:
            - ret : variable booleana que indica si la peticion sigue el formato adecuado
            - method : Método HTTP que ha solicitado el cliente
            - attributes : Lista de atributos (necesarios en el caso de POST y del GET no general)
    """
    global dataBase
    ret = True
    headers = {}
    param = requestMess.split('\r\n')
    body = param[-1]
    request = param[0].split()
    method = request[0]
    dataBase = request[1][1:]
    version = request[2]

    if request[0] == 'GET':
        args = request[1].split('?')
        if len(args) == 2:
            dataBase, attributes = args[0][1:], args[1].split('&')
            attributes = list(map(lambda x:x.split('='), attributes))
            print(dataBase, attributes)
        else:
            attributes = None
    elif request[0] == 'POST':
        if body != '':
            body = body.split('&')
            attributes = list(map(lambda x:x.split('='), body))
        else:
            attributes = None
    else:
        ret = False

    return ret, method, attributes, version


def createResponse(responseInfo : str, conType : str, conLength : float):
    """[summary]

    Args:
        responseInfo (str): [description]
        conType (str): [description]
        conLength (float): [description]

    Returns:
        bytes: [description]
    """
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    tm = time.gmtime(time.time())

    response = 'Date: {}, {:02d} {} {} {}:{}:{} GMT\r\n'.format(days[tm.tm_wday], tm.tm_mday, months[tm.tm_mon-1],
                                                                tm.tm_year, tm.tm_hour, tm.tm_min, tm.tm_sec)
    if conType is not None and conType is not None:
        # response += 'Content-Length: {}\r\n'.format(conLength)
        response += 'Content-Type: {}\r\n'.format(conType)
    if responseInfo is not None:
        response += '\r\n' + responseInfo
    return response.encode()


if __name__ == '__main__':
    # Creacion del socket TCP/IP del servidor
    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listenSocket.bind(('', listenPort))
    listenSocket.listen(maxConnections)
    listenSocket.settimeout(2.0)

    while True:
        try:
            connSocket, adress = listenSocket.accept()
            requestMess = connSocket.recv(maxSize).decode()
            print('Conexion establecida con '+str(adress[0]))
            print(requestMess)
            if requestMess == '':
                raise ValueError
            ret, method, attributes, version = httpCheck(requestMess)
            if ret:
                # Nos conectamos con la base de datos
                db = DataBase()
                if method == 'GET':
                    if not attributes:
                        responseInfo, conType, conLength = db.selectAll()
                    else:
                        responseInfo, conType, conLength = db.update(attributes)
                else:
                    if attributes:
                        responseInfo, conType, conLength = db.update(attributes)
                db.close()

                if responseInfo is None:
                    response = '{} 400 Bad Request\r\n'.format(version).encode()
                    response += createResponse(responseInfo, None, None)
                else:
                    response = '{} 200 OK\r\n'.format(version).encode()
                    response += createResponse(responseInfo, conType, conLength)

            else:
                response = '{} 400 Bad Request\r\n'.format(version).encode()
                response += createResponse(responseInfo, None, None)
            print(response)
            connSocket.send(response)
            connSocket.close()
            print('Conexion cerrada')
        except pymysql.err.DatabaseError as e:
            code, msg = e.args
            if code == 1049:
                response = '{} 404 Not Found\r\n'.format(version).encode()
                responseInfo = '<html><body>Error 404: File not found</body></html>'
                response += createResponse(responseInfo, None, None)
                connSocket.send(response)
                connSocket.close()
            else:
                response = '{} 400 Bad Request\r\n'.format(version).encode()
                responseInfo = '<html><body>Error 400: Bad Request</body></html>'
                response += createResponse(responseInfo, None, None)
                connSocket.send(response)
                connSocket.close()
        except socket.error as err:
            pass
        except UnicodeDecodeError:
            response = '{} 400 Bad Request\r\n'.format(version).encode()
            response += 'Accept-Charset: utf-8\r\n'.encode()
            responseInfo = '<html><body>Error 400: Bad Request</body></html>'
            response += createResponse(responseInfo, None, None)
            connSocket.send(response)
            connSocket.close()
        except Exception:
            response = '{} 400 Bad Request\r\n'.format(version).encode()
            responseInfo = '<html><body>Error 400: Bad Request</body></html>'
            response += createResponse(responseInfo, None, None)
            connSocket.send(response)
            connSocket.close()
