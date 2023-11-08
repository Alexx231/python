from bdd_clientes import *

def crear_clientes(clientes_a_guardar):
    try:
        conexion = conexion_clientes()
        cursor = conexion.cursor()
        query ="INSERT INTO clientes (nombre_cliente, telefono_cliente) VALUES (%s, %s)"
        valores = clientes_a_guardar
        cursor.execute(query,valores)
        conexion.commit()
        print("El proceso de añadir al cliente fue hecho correctamente")
        conexion.close()
    except mysql.connector.Error as error:
        print("El proceso de añadir al cliente fue cancelado",error)
        return None
    
def leer_clientes():
    try:
        conexion = conexion_clientes()
        cursor = conexion.cursor()
        query ="SELECT * FROM clientes"
        cursor.execute(query)
        for(id_cliente,nombre_cliente,telefono_cliente) in cursor:
            print("ID:{id_cliente} - Nombre:{nombre_cliente} - Telefono:{telefono_cliente}")
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as error:
        print("No se pudo leer a los clientes",error)
        return None

def actualizar_clientes(id_cliente,nombre_cliente,telefono_cliente):
    try:
        conexion = conexion_clientes()
        cursor = conexion.cursor()
        query ="UPDATE nombre_cliente,telefono_cliente SET nombre_cliente,telefono_cliente =%s WHERE id_cliente =%s"
        valores = (id_cliente,nombre_cliente,telefono_cliente)
        cursor.execute(query,valores)
        conexion.commit()
        print("El proceso de actualizar al cliente fue hecho correctamente")
        conexion.close()
    except mysql.connector.Error as error:
        print("El proceso de actualizar al cliente fue cancelado",error)
        return None

def borrar_clientes(id_cliente):
    try:
        conexion = conexion_clientes()
        cursor = conexion.cursor()
        query ="DELETE FROM nombre_cliente,telefono_cliente =%s WHERE id_cliente =%s"
        valores = (id_cliente)
        cursor.execute(query,valores)
        conexion.commit()
        print("El proceso de borrar al cliente fue hecho correctamente")
        conexion.close()
    except mysql.connector.Error as error:
        print("El proceso de borrar al cliente fue cancelado",error)
        return None
