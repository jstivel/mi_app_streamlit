import sqlite3

# Conexión a SQLite (crea el archivo si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL
)
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos y tabla creada exitosamente.")
