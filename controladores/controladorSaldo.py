from bd import Obtener_Conexion
def CambiarDeuda(deudaActual, documento):
    conexion = Obtener_Conexion()

    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET deuda = %s WHERE documento = %s ",(deudaActual,documento))
    conexion.commit()
    conexion.close()
    
def CambiarAFavor(aFavor, documento):
    conexion = Obtener_Conexion()

    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET aFavor = %s WHERE documento = %s ",(aFavor,documento))
    conexion.commit()
    conexion.close()
    
    
def Deuda(documento):
    conexion = Obtener_Conexion()
    deuda=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT deuda FROM clientes Where documento = %s",(documento))
        deuda=cursor.fetchone()
    conexion.close()
    return deuda

def aFavor(documento):
    conexion = Obtener_Conexion()
    aFavor=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT aFavor FROM clientes Where documento = %s",(documento))
        aFavor=cursor.fetchone()
    conexion.close()
    return aFavor

