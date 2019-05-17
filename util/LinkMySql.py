#coding:utf-8
#author:ppliang
#=======================
import pymysql

def Link_mysql3():
    try:
        db = pymysql.connect(host="192.168.1.22",
                             user="tluser",
                             passwd="tongli!@#123",
                             db="tl_b2b_test",
                             charset='utf8')
        return db
    except:
        print("could not connect to mysql server")

