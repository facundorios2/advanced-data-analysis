import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt


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




# Análisis de datos
statistics = df.groupby('department').agg({
    'performance_score': ['mean', 'median', 'std'],
    'salary': ['mean', 'median', 'std'],
    'employee_id': 'count'
}).rename(columns={'employee_id': 'total_employees'})

correlation_years_performance = df['years_with_company'].corr(df['performance_score'])
correlation_salary_performance = df['salary'].corr(df['performance_score'])

# Histograma del performance_score para cada departamento
departments = df['department'].unique()
for department in departments:
    df[df['department'] == department]['performance_score'].hist(alpha=0.5, label=department)

plt.title('Histograma del Performance Score por Departamento')
plt.xlabel('Performance Score')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Gráfico de dispersión de years_with_company vs. performance_score
plt.scatter(df['years_with_company'], df['performance_score'])
plt.title('Años con la Empresa vs. Performance Score')
plt.xlabel('Años con la Empresa')
plt.ylabel('Performance Score')
plt.show()

# Gráfico de dispersión de salary vs. performance_score
plt.scatter(df['salary'], df['performance_score'])
plt.title('Salario vs. Performance Score')
plt.xlabel('Salario')
plt.ylabel('Performance Score')
plt.show()


# Cerrar la conexión
conn.close()