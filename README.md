# taller3
Taller 3 python
La aplicacion se encarga de registar un operador y una sub-estacion solicitando esos datos al usuario, y luego leyendo de un archivo csv obtendra los registros de ciudades, consumo y hora, para luego realizar un reporte de las ciudades, su consumo total y la hora pico de consumo
- modelo.py contiene las clases Operador, SubEstacion, Ciudad.
- basedatos.py contiene la clase BaseDatos que maneja la conexion a sqlite3, creacion de tablas y queries.
- controller.py contiene la logica del negocio(creacion de objetos, lectura de archivo, creacion reporte).
- main.py contiene el main que se encarga de llamar al controlador
