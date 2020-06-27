class Operador():
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.sub_estacion = None
class SubEstacion():
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.ciudades = []
    def addCiudad(self, ciudad):
        self.ciudades.append(ciudad)
class Ciudad():
    def __init__(self, id, ciudad_id, hora, consumo):
        self.id = id
        self.ciudad_id = ciudad_id
        self.hora = hora
        self.consumo = consumo