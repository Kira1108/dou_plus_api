import pymongo
from pymongo import MongoClient
from datetime import datetime
import pymysql
from sqlalchemy import create_engine

# mongo db
HOST = "172.20.10.2"
PORT = 27017
DB_NAME = '抖Plus'

# mysql
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root123'
MYSQL_DB = 'chan'
MYSQL_PORT = 3306



class MongoQueries():
    def __init__(self, host, port, db_name):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.db = MongoClient(self.host, self.port)[self.db_name]


    def query(self, table = 'base_user_info', limit =100):
        lim = 0
        results = []
        for record in self.db[table].find():
            results.append(record)
            lim += 1
            if lim == limit :
                break
        return results


db = MongoQueries(HOST, PORT, DB_NAME)


def get_mysql_conn(engine = False):
    if not engine:
        return pymysql.connect(host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        port = MYSQL_PORT,
        db = MYSQL_DB)
    else:
        return create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}')


def execute_sql(sql):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()
