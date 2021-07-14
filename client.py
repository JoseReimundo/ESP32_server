import socket
import pymysql
import json

serverName = 'localhost'
serverPort = 9090
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = 'GET /clientes HTTP/1.0\r\n\
            \r\n'
clientSocket.send(sentence.encode('ascii'))
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
