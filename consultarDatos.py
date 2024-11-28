import sqlite3
# Conexión a SQLite
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Consultar datos
cursor.execute('SELECT * FROM productos')
productos = cursor.fetchall()

# Mostrar los datos
for producto in productos:
    print(producto)

# Cerrar conexión
conn.close()
