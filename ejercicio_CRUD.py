from BDD import *

def anadir_direccion(direccion_a_guardar):
    try:
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "INSERT INTO direccion (direccion) VALUES (%s)"
        valores = direccion_a_guardar
        cursor.execute(query,valores)
        conexion.commit()
        print(f"\nLa direccion fue añadida con exito")
    except FileNotFoundError:
        print(f"\nError")
    cierra_conexion()
        
        
def leer_direccion():
    try:
        conexion= conexion_bdd()
        cursor = conexion.cursor()
        query = "SELECT * FROM direccion"
        cursor.execute(query)
        for (id_direccion,direccion) in cursor:
            print(f"\nLa ID de la direccion es {id_direccion} y el nombre es {direccion}")
        conexion.commit()
    except FileNotFoundError:
        print(f"\nNo hay direcciones añadidas")
    cierra_conexion()


def actualizar_direccion(id_direccion, direccion):
    try:
        conexion= conexion_bdd()
        cursor = conexion.cursor()
        query = "UPDATE direccion SET direccion =%s WHERE id_direccion =%s"
        valores = (id_direccion, direccion)
        cursor.execute(query,valores)
        conexion.commit()
        print(f"\nLa direccion fue actualizada correctamente")
    except FileNotFoundError:
        print(f"\nLa direccion no pudo ser actualizada")
    cierra_conexion()
    

def borrar_direccion(id_direccion):
    try:
        conexion= conexion_bdd()
        cursor = conexion.cursor()
        query = "DELETE FROM direccion =%s WHERE id_direccion =%s"
        valores = (id_direccion)
        cursor.execute(query,valores)
        conexion.commit()
        print(f"\nLa direccion fue borrada con exito")
    except FileNotFoundError:
        print("f\nLa direccion no pudo ser borrada")
    cierra_conexion()
    