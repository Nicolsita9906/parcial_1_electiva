# parcial1 Nicol Valeria Ocampo Bernal
import mysql.connector

print("Hellor World")

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="parcial_db"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())




