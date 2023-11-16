from db.conexion import crear_conexion



def consultar_alumnos():
    conexion = None
    sql = 'SELECT * FROM asistencia;'
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        print('ERROR CONSULTANDO ALUMNOS')
        return []
    finally:
        if conexion:
            cursor.close()
            conexion.close()


def buscar_alumno(apellido:str):
    sql = F'SELECT * FROM asistencia WHERE apellido LIKE "%{apellido}%"; '
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(f'ERROR BUSCANDO ALUMNOS: {e}')
        return []
    finally:
        if conexion:
            cursor.close()
            conexion.close()