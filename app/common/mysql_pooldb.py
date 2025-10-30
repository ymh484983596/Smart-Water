#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023-11-20 18:06
# @Author : Ther
import  random
import  threading
from DBUtils.PooledDB import PooledDB
# from dbutils.persistent_db import PersistentDB
import time
import pymysql
from config.config import db_config


class MysqlHelper(object):
    def __init__(self,db_config):
        self._pool=PooledDB(creator=pymysql,
                            mincached=1,
                            maxcached=5,
                            maxshared=5,
                            maxconnections=5,
                            maxusage=5,
                            blocking=True,
                            user=db_config.get('user'),
                            password=db_config.get('password'),
                            db=db_config.get('database'),
                            host=db_config.get('host'),
                            port=db_config.get('port'),
                            charset=db_config.get('charset'),)

    def getConn(self):
        conn=self._pool.connection()#从连接池获取一个连接
        cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
        return  conn,cursor

    @staticmethod
    def dispose(cursor,conn):
        cursor.close()
        conn.close()

    def getOne(self,sql):
        conn,cursor=self.getConn()
        th_name=threading.current_thread().getName()
        cursor.execute(sql)
        rows=cursor.fetchone()
        # print(f" start{sql}")
        self.dispose(cursor,conn)
        return rows

    def getAll(self,sql):
        conn,cursor=self.getConn()
        th_name=threading.current_thread().getName()
        cursor.execute(sql)
        rows=cursor.fetchall()
        # print(f"start{sql}")
        self.dispose(cursor,conn)
        return rows

    def queryOne(self,sql):
        # system_logger.info('-----------sql start-----------')
        # system_logger.info(sql)
        try:
            conn,cursor=self.getConn()
            res=cursor.execute(sql)
            json_data=self.sql_fetch_json(cursor)
            #将连接返回
            self.dispose(cursor,conn)
            # print().info('-----------queryByKey result:{result} '+str(json_data))
            if len(json_data)==1:
                return json_data[0]
            return None

        except Exception as e:
            # system_logger.info('-----------predict exception line :  '+str(e.__traceback__.tb_lineno)+'of'+
            # e.__traceback__.tb_frame.f_globals['__file__'])
            # system_logger.info(e)
            return None

    @staticmethod
    def sql_fetch_json(cursor: pymysql.cursors.Cursor):
        keys=[]
        for column in cursor.description:
            keys.append(column[0])
        key_number=len(keys)

        json_data=[]
        for row in cursor.fetchall():
            item=dict()
            for q in range(key_number):
                item[keys[q]]=row[q]
            json_data.append(item)
        return json_data

db = MysqlHelper(db_config)
