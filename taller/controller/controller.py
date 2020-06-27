from database.base_datos import BaseDatos
from model.modelo import *
from pathlib import Path
from os import system, name

class Controller:
    def __init__(self):
        self.bd = BaseDatos()
        self.inicio()
    def leer_archivo_insertar(self, sub_estacion):
        try:
            path = Path(__file__).parent / "../mediciones.csv"
            with open(path, 'r') as mediciones:
                lineas = mediciones.readlines()
                lineas = [x.strip() for x in lineas]
                for item in lineas:
                    arr = item.split(";")
                    ciudad = Ciudad(None,arr[1],arr[0],arr[2])
                    self.bd.insertar_new_row_ciudad(sub_estacion, ciudad)
                    sub_estacion.addCiudad(ciudad)
        except Exception as exc:
            print("Hubo un error", exc)
    def realizar_reporte(self, operador):
        print("Reporte del Operador",operador.nombre,":")
        print(operador.sub_estacion.nombre)
        resSum= self.bd.get_consumo_total_ciudad_por_sub_estacion(operador.sub_estacion.id)
        resPico= self.bd.get_pico_ciudad_por_sub_estacion(operador.sub_estacion.id)
        for numero in range(0,len(resSum)):
            print("Ciudad ",resSum[numero][0],". Total de consumo:",resSum[numero][1],". Hora pico:",resPico[numero][2])
    def inicio(self):
        print("Medidor del ICE:")
        print("-------- Bienvenido Operador. favor registrese:")
        operador_nombre = input("Ingrese el nombre del operador: ")
        objOperador = Operador(None,operador_nombre)
        self.bd.insertar_new_row_operador(objOperador)
        print("-------- Hola:",objOperador.nombre)
        sub_estacion_nombre = input("-------- Ingrese la Subestación que le corresponde:")
        objSubEstacion = SubEstacion(None, sub_estacion_nombre)
        self.bd.insertar_new_row_sub_estacion(objOperador, objSubEstacion)
        objOperador.sub_estacion= objSubEstacion
        self.leer_archivo_insertar(objSubEstacion)
        self.realizar_reporte(objOperador)
