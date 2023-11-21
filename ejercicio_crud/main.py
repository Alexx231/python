import crud_departamentos
import crud_empleados

crud_departamentos.crear_departamentos("Ventas")
crud_departamentos.crear_departamentos("Marketing")

crud_departamentos.ver_departamentos()

crud_departamentos.actualizar_departamentos("Marketing","Marketing y Publicidad")

crud_departamentos.borrar_departamentos("Ventas")


crud_empleados.crear_empleados("Pepe, 12, 1")
crud_empleados.crear_empleados("Gonzalo, 36, 2")

crud_empleados.ver_empleados()

crud_empleados.actualizar_empleados(36,"Angel, 43, 2")

crud_empleados.borrar_empleados("Gonzalo, 36, 2")