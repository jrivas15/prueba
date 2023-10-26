from db.conexion import crear_conexion
import pandas
conexion = crear_conexion()
cursor =  conexion.cursor()
cursor.execute("SELECT * FROM productos;")
data = cursor.fetchall()
df = pandas.DataFrame(data)
print(df)
cursor.close()
conexion.close()