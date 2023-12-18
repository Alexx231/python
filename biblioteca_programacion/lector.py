"""  
Ver un listado de los libros prestados en el que aparezca el nombre del libro, el nombre del lector y la fecha de préstamo. 
"""
class Lector:
    
def __init__(self, id_lector, nombre, apellidos, fecha_alta, fecha_baja):
        self.id_lector = id_lector
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_alta = fecha_alta    
        self.fecha_baja = fecha_baja