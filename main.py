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


# Análisis de datos
statistics = df.groupby('department').agg({
    'performance_score': ['mean', 'median', 'std'],
    'salary': ['mean', 'median', 'std'],
    'employee_id': 'count'
}).rename(columns={'employee_id': 'total_employees'})

correlation_years_performance = df['years_with_company'].corr(df['performance_score'])
correlation_salary_performance = df['salary'].corr(df['performance_score'])