from bdd_empresa import *

def crear_empleados(empleados_a_guardar): #Esta función intenta crear un nuevo empleado en la base de datos.
    try:
        conexion = conexion_empresa()
        cursor = conexion.cursor()
        query ="INSERT INTO empleados (nombre_empleado) VALUES (%s)"
        valores = empleados_a_guardar
        cursor.execute(query,valores)
        conexion.commit()
        print("El proceso de añadir un empleado fue hecho correctamente")
        conexion.close()
    except mysql.connector.Error as error:
        print("El proceso de añadir un empleado fue cancelado",error)
        return None
    
def ver_empleados(): #Esta función intenta ver los empleados de la base de datos.
    try:
        conexion = conexion_empresa()
        cursor = conexion.cursor()
        query ="SELECT * FROM empleados"
        cursor.execute(query)
        for(id_empleado,nombre_empleado) in cursor:
            print("ID:{id_empleado} - Nombre:{nombre_empleado}")
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as error:
        print("No se pudo ver los empleados",error)
        return None

def actualizar_empleados(id_empleado,nombre_empleado): #Esta función intenta actualizar los empleados de la base de datos.
    try:
        conexion = conexion_empresa()
        cursor = conexion.cursor()
        query ="UPDATE nombre_empleado SET nombre_empleado =%s WHERE id_empleado =%s"
        valores = (id_empleado,nombre_empleado)
        cursor.execute(query,valores)
        conexion.commit()
        print("El proceso de actualizar un empleado fue hecho correctamente")
        conexion.close()
    except mysql.connector.Error as error:
        print("El proceso de actualizar un empleado fue cancelado",error)
        return None

def borrar_empleados(id_empleado): #Esta función intenta borrar los empleados de la base de datos.
    try:
        conexion = conexion_empresa()
        cursor = conexion.cursor()
        query ="DELETE FROM  nombre_empleado =%s WHERE id_empleado =%s"
        valores = (id_empleado)
        cursor.execute(query,valores)
        conexion.commit()
        print("El proceso de borrar un empleado fue hecho correctamente")
        conexion.close()
    except mysql.connector.Error as error:
        print("El proceso de borrar un empleado fue cancelado",error)
        return None