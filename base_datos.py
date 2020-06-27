import sqlite3 as dba_object 
from sqlite3 import Error
from modelo import *
from os import system, name
class BaseDatos():
    def sqlite_create_database(self):
        try:
            conexion = dba_object.connect("taller3.db")
            return conexion
        except Error as err:
            print(err)


    def create_table_operador(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS operador(_id INTEGER PRIMARY KEY, nombre TEXT NOT NULL)")
            connection.commit()
        except Error as err:
            print(Error, "Debio ser en el query!", err)
    def create_table_subestacion(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS sub_estacion(_id INTEGER PRIMARY KEY, operador_id INTEGER NOT NULL, nombre NOT NULL, FOREIGN KEY (operador_id) REFERENCES operador (_id))")
            connection.commit()
        except Error:
            print(Error, "Debio ser en el query!")
    def create_table_ciudad(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS ciudad(_id INTEGER PRIMARY KEY, ciudad_id INTEGER NOT NULL, sub_estacion_id INTEGER NOT NULL, hora INTEGER NOT NULL, consumo FLOAT NOT NULL, FOREIGN KEY (sub_estacion_id) REFERENCES sub_estacion (_id))")
            connection.commit()
        except Error:
            print(Error, "Debio ser en el query!")

    def insertar_new_row_operador(self, objOperador):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("INSERT INTO operador (nombre) VALUES(?);", [objOperador.nombre])
            self.objeto_conexion.commit()
            objOperador.id = cursor.lastrowid
            return objOperador
        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
            return None
    def insertar_new_row_sub_estacion(self, objOperador, objSubEstacion):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("INSERT INTO sub_estacion(operador_id,nombre) VALUES(?,?);", [objOperador.id, objSubEstacion.nombre])
            self.objeto_conexion.commit()
            objSubEstacion.id = cursor.lastrowid
            return objSubEstacion
        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
            return None

    def insertar_new_row_ciudad(self, objSubEstacion, objCiudad):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("INSERT INTO ciudad(ciudad_id,sub_estacion_id,hora,consumo) VALUES(?,?,?,?);", [objCiudad.ciudad_id,objSubEstacion.id, objCiudad.hora, objCiudad.consumo])
            self.objeto_conexion.commit()
            objCiudad.id = cursor.lastrowid
            return objCiudad
        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
            return None
    def __init__(self):
        self.objeto_conexion = self.sqlite_create_database()
        self.create_table_operador(self.objeto_conexion)
        self.create_table_subestacion(self.objeto_conexion)
        self.create_table_ciudad(self.objeto_conexion)

    def get_all_rows_operador(self):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("SELECT * FROM operador") 
            objeto_resultado = cursor.fetchall() 
            self.objeto_conexion.commit()

            return objeto_resultado

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
    def get_all_rows_sub_estacion(self):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("SELECT * FROM sub_estacion") 
            objeto_resultado = cursor.fetchall() 
            self.objeto_conexion.commit()

            return objeto_resultado

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
    def get_all_rows_ciudad(self):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("SELECT * FROM ciudad") 
            objeto_resultado = cursor.fetchall() 
            self.objeto_conexion.commit()

            return objeto_resultado

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
    def get_sub_estacion_por_operador(self, operador_id):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("SELECT * FROM sub_estacion WHERE operador_id = ?", [operador_id]) 
            objeto_resultado = cursor.fetchall() 
            self.objeto_conexion.commit()

            return objeto_resultado

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
    def get_all_rows_ciudad_por_sub_estacion(self, sub_estacion_id):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("SELECT * FROM ciudad WHERE sub_estacion_id = ?",[sub_estacion_id]) 
            objeto_resultado = cursor.fetchall() 
            self.objeto_conexion.commit()

            return objeto_resultado

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
    def get_consumo_total_ciudad_por_sub_estacion(self, sub_estacion_id):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("SELECT ciudad_id, SUM(consumo) FROM ciudad WHERE sub_estacion_id = ? group by ciudad_id order by ciudad_id",[sub_estacion_id]) 
            objeto_resultado = cursor.fetchall() 
            self.objeto_conexion.commit()

            return objeto_resultado

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)
    def get_pico_ciudad_por_sub_estacion(self, sub_estacion_id):
        try:
            cursor = self.objeto_conexion.cursor()
            cursor.execute("SELECT ciudad_id, Max(consumo), hora FROM ciudad WHERE sub_estacion_id = ? group by ciudad_id order by ciudad_id",[sub_estacion_id]) 
            objeto_resultado = cursor.fetchall() 
            self.objeto_conexion.commit()

            return objeto_resultado

        except Error as err:
            print(Error, "Debieron ser valores erroneos!", err)