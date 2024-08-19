import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def close(self):
        if self.conn:
            self.conn.close()

    def read_data(self, query):
        return pd.read_sql(query, self.conn)

class DataAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def compute_statistics(self):
        return self.df.groupby('department').agg({
            'performance_score': ['mean', 'median', 'std'],
            'salary': ['mean', 'median', 'std'],
            'employee_id': 'count'
        }).rename(columns={'employee_id': 'total_employees'})

    def calculate_correlations(self):
        correlation_years_performance = self.df['years_with_company'].corr(self.df['performance_score'])
        correlation_salary_performance = self.df['salary'].corr(self.df['performance_score'])
        return correlation_years_performance, correlation_salary_performance

class DataVisualizer:
    def __init__(self, dataframe):
        self.df = dataframe

    def plot_histogram_by_department(self):
        departments = self.df['department'].unique()
        for department in departments:
            self.df[self.df['department'] == department]['performance_score'].hist(alpha=0.5, label=department)
        plt.title('Histograma del Performance Score por Departamento')
        plt.xlabel('Performance Score')
        plt.ylabel('Frecuencia')
        plt.legend()
        plt.show()

    def plot_scatter(self, x_column, y_column, title, x_label, y_label):
        plt.scatter(self.df[x_column], self.df[y_column])
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

# Ejecución
def main():
    # Configuración de la conexión a la base de datos
    db_connector = DatabaseConnector(
        host="localhost",
        user="root",
        password="",
        database="CompanyData"
    )
    
    db_connector.connect()

    # Leer datos
    query = "SELECT * FROM EmployeePerformance"
    df = db_connector.read_data(query)

    # Análisis de datos
    analyzer = DataAnalyzer(df)
    statistics = analyzer.compute_statistics()
    correlation_years_performance, correlation_salary_performance = analyzer.calculate_correlations()

    # Visualización de datos
    visualizer = DataVisualizer(df)
    visualizer.plot_histogram_by_department()
    visualizer.plot_scatter('years_with_company', 'performance_score', 'Años con la Empresa vs. Performance Score', 'Años con la Empresa', 'Performance Score')
    visualizer.plot_scatter('salary', 'performance_score', 'Salario vs. Performance Score', 'Salario', 'Performance Score')

    # Cerrar la conexión
    db_connector.close()

if __name__ == "__main__":
    main()
