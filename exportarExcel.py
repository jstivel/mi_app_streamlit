import sqlite3
import pandas as pd

# Conexión a SQLite
conn = sqlite3.connect('mi_base_de_datos.db')

# Leer datos de la tabla "productos" en un DataFrame
query = "SELECT * FROM productos"
df = pd.read_sql_query(query, conn)

# Exportar los datos a un archivo Excel
df.to_excel('productos.xlsx', index=False, engine='openpyxl')

# Cerrar la conexión
conn.close()

print("Datos exportados exitosamente a productos.xlsx")
