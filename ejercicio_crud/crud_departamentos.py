from bdd_empresa import *

def crear_departamentos(departamentos_a_guardar):
    try:
        conexion = conexion_empresa()
        cursor = conexion.cursor()
        query ="INSERT INTO departamentos (nombre_departamento, ubicacion_departamento) VALUES (%s, %s)"
        valores = departamentos_a_guardar
        cursor.execute(query,valores)
        conexion.commit()
        print("El proceso de añadir el departamento fue hecho correctamente")
        conexion.close()
    except mysql.connector.Error as error:
        print("El proceso de añadir el departamento fue cancelado",error)
        return None
    
def ver_departamentos():
    try:
        conexion = conexion_empresa()
        cursor = conexion.cursor()
        query ="SELECT * FROM departamentos"
        cursor.execute(query)
        for(id_departamento,nombre_departamento,ubicacion_departamento) in cursor:
            print("ID:{id_departamento} - Nombre:{nombre_departamento} - Ubicación:{ubicacion_departamento}")
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as error:
        print("No se pudo ver los departamentos",error)
        return None

def actualizar_departamentos(id_departamento,nombre_departamento,ubicacion_departamento):
    try:
        conexion = conexion_empresa()
        cursor = conexion.cursor()
        query ="UPDATE nombre_departamento,ubicacion_departamento SET nombre_departamento,ubicacion_departamento =%s WHERE id_departamento =%s"
        valores = (id_departamento,nombre_departamento,ubicacion_departamento)
        cursor.execute(query,valores)
        conexion.commit()
        print("El proceso de actualizar el departamento fue hecho correctamente")
        conexion.close()
    except mysql.connector.Error as error:
        print("El proceso de actualizar el departammento fue cancelado",error)
        return None

def borrar_departamentos(id_departamentos):
    try:
        conexion = conexion_empresa()
        cursor = conexion.cursor()
        query ="DELETE FROM  nombre_departamento,ubicacion_departamento =%s WHERE id_departamento =%s"
        valores = (id_departamentos)
        cursor.execute(query,valores)
        conexion.commit()
        print("El proceso de borrar el departamento fue hecho correctamente")
        conexion.close()
    except mysql.connector.Error as error:
        print("El proceso de borrar el departamento fue cancelado",error)
        return None