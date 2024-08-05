import pandas as pd
import mysql.connector

# Conectar a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="CompanyData"
)

# Leer los datos de la tabla EmployeePerformance
query = "SELECT * FROM EmployeePerformance"
df = pd.read_sql(query, conn)

# Cerrar la conexión
conn.close()

