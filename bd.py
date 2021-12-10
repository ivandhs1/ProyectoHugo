import pymysql

def Obtener_Conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='bd_proyectohugo')
