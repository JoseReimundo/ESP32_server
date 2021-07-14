import socket
import pymysql
import json

serverName = 'localhost'
serverPort = 9090
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = 'GET /clientes?KEVIN=5&JOSE=4 HTTP/1.0\r\n\r\n'
# sentence ='POST /clientes HTTP/1.0\r\n\r\n'
clientSocket.send(sentence.encode())
response = clientSocket.recv(2048)
print(response.decode())
clientSocket.close()

dataBase = 'clientes'
"""
class DataBase():
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'JRDMysql2021',
            db = dataBase
        )
        self.cursor = self.connection.cursor()

    def select_user(self):
        sql = 'SELECT * FROM clientes;'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            for u in users:
                print('Name: {}, DNI: {}, Age: {}'.format(u[0], u[1], u[2]))
            dic = {}
            for u in users:
                dic[u[0]] = u[1]
            response = json.dumps(dic)
            print(dic, response, type(response))
        except Exception as e:
            print(e)

    def query(self, query : str):
        try:
            self.cursor.execute(query)
            users = self.cursor.fetchall()
            for u in users:
                print('Name:', u)
        except Exception as e:
            print(e)

    def insert(self, data):
        try:
            sql = 'INSERT INTO clientes VALUES {}'.format(data)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(e)

    def close(self):
        self.connection.close()


database = DataBase()
database.query('SELECT * \
                FROM CLIENTES \
                WHERE age < 30;')
#database.insert(('ANA', '12349347R', 32))
database.select_user()
database.close()

b='v=1&f=3&b=7'
c=b.split('&')
print(b)
c=list(map(lambda x:x.split('=')[1], c))
print(c)

t = None
if not t:
    print('True')

import datetime, time
date = str(datetime.date.today())
t = time.time()
print(date)
print(t)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
tm = time.gmtime(time.time())
print(tm.tm_mon, tm.tm_wday)
print('Date: {}, {:02d} {} {} {}:{}:{} GMT\r\n'.format(days[tm.tm_wday], tm.tm_mday, months[tm.tm_mon-1], tm.tm_year,
                                                      tm.tm_hour, tm.tm_min, tm.tm_sec))

dictionary = {'r1':0, 'm6':0, 'r3':0, 'r0':0, 'm1':0 }
j=json.dumps(dictionary, sort_keys=True)
print(j) """
""" mess = b'\x16\x03\x01\x02\x00\x01\x00\x01\xfc\x03\x03\x9f\xd7\xe4\x93\xaf\x12\xd1D8\xd1\xfb\xfc\xe8\xe0\xe3\xadG\x91u\xda\xe4\xb2/\xb5\xeb<\x0e\x86\x0f;\xcf\xc7 \xc8\xc67\xb1\x7f\xd0\xfb\xd9q:q\xf9\xa2\x97\x08\xc5\x89\x10\xd3\xf2^\x15\x19\xd0\x9c\xe4S\x10$3\xbf4\x00"**\x13\x01\x13\x02\x13\x03\xc0+\xc0/\xc0,\xc00\xcc\xa9\xcc\xa8\xc0\x13\xc0\x14\x00\x9c\x00\x9d\x00/\x005\x00\n\x01\x00\x01\x91\xca\xca\x00\x00\x00\x00\x00\x0e\x00\x0c\x00\x00\tlocalhost\x00\x17\x00\x00\xff\x01\x00\x01\x00\x00\n\x00\n\x00\x08JJ\x00\x1d\x00\x17\x00\x18\x00\x0b\x00\x02\x01\x00\x00#\x00\x00\x00\x05\x00\x05\x01\x00\x00\x00\x00\x00\r\x00\x14\x00\x12\x04\x03\x08\x04\x04\x01\x05\x03\x08\x05\x05\x01\x08\x06\x06\x01\x02\x01\x00\x12\x00\x00\x003\x00+\x00)JJ\x00\x01\x00\x00\x1d\x00 [|\xf7"ig\xfe\x9a\x9d\xcd\x8a\x80`\x8b=y\xcd\xba_\x8a\xa3@\x9d\x14\x14\xf7\xc6\xa0u\xa5\xa0h\x00-\x00\x02\x01\x01\x00+\x00\x0b\n**\x03\x04\x03\x03\x03\x02\x03\x01\x00\x1b\x00\x03\x02\x00\x02\xea\xea\x00\x01\x00\x00\x15\x00\xe1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
args = mess.split(b'\xfc')
print(args, len(args))
print(args[0].decode('ascii'))
print(args[0].decode('utf-8'))
print(args[0].decode('utf-16'))
print(args[0].decode('latin1'))
print(args[0].decode('cp1252'))
print(args[0]+b'\xfc'.decode('utf-32'))
a = b'/'
print(a) """