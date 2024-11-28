import streamlit as st
import pandas as pd
import sqlite3

# Título de la app
st.title("Visualización de Datos de Productos")

# Conexión a SQLite
conn = sqlite3.connect('mi_base_de_datos.db')

# Leer datos de la tabla "productos"
query = "SELECT * FROM productos"
df = pd.read_sql_query(query, conn)

# Mostrar datos en la app
st.subheader("Datos de la base de datos")
st.dataframe(df)

# Botón para exportar a Excel
if st.button("Exportar a Excel"):
    df.to_excel("productos_streamlit.xlsx", index=False, engine='openpyxl')
    st.success("Archivo exportado como productos_streamlit.xlsx")

# Cerrar conexión
conn.close()
