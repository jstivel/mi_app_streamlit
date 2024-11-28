import sqlite3

# Conexión a SQLite
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Datos de ejemplo
productos = [
    ("Laptop", 1200.50, 10),
    ("Mouse", 25.00, 50),
    ("Teclado", 45.99, 30),
    ("Monitor", 300.00, 20)
]

# Insertar datos en la tabla
cursor.executemany('''
INSERT INTO productos (nombre, precio, cantidad)
VALUES (?, ?, ?)
''', productos)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos insertados exitosamente.")
