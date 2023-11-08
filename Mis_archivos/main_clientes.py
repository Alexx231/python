import crud_clientes

crud_clientes.crear_clientes("Pepe, 12")
crud_clientes.crear_clientes("Gonzalo, 36")


crud_clientes.leer_clientes()


crud_clientes.actualizar_clientes(36,"Angel, 43")


crud_clientes.borrar_clientes("Gonzalo, 36")