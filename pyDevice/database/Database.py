#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import sys
import warnings
warnings.filterwarnings("ignore", "Table '.*' already exists")
warnings.filterwarnings("ignore", "Can't create database '.*'; database exists")

class ConnectSQL(object):
    def __init__(self,db='Device'):
        self.connection = None
        self.cursor = None
        self.host='localhost'
        self.port=3306
        self.user='root'
        self.passwd='password'
        self.db=db
        self.connect()

    def __end__(self):
        self.cursor.close()
        self.connection.close()

    def connect(self):
        self.connection = pymysql.connect(host=self.host,
                                          port=self.port,
                                          user=self.user,
                                          passwd=self.passwd,
                                          db=self.db)
        self.cursor = self.connection.cursor()

    def _execute(self, cmd):
        return self.cursor.execute(cmd)

    def _description(self):
        return self.cursor.description

    def _cursor(self):
        return self.cursor

    def kill(self):
        self.__end__()