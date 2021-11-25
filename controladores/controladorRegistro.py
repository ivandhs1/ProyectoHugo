from bd import Obtener_Conexion

def RegistrarCliente(documento, nombre, movil, direccion, saldo):
    conexion = Obtener_Conexion()
    with conexion.cursor() as cursor:
        cursor.execute ("INSERT INTO clientes(documento,nombre,movil,direccion,saldo) VALUES (%s,%s,%s,%s,%s) ",(documento,nombre,movil,direccion,saldo))
    conexion.commit()
    conexion.close()
    