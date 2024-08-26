# Actividad de repaso + POO

Este proyecto realiza un análisis del rendimiento de los empleados de una empresa utilizando Python, pandas para el análisis de datos, y matplotlib para la visualización. Los datos se almacenan en una base de datos MySQL y se accede a ellos utilizando `mysql-connector-python`.

## Descripción del Proyecto

El proyecto consta de tres módulos principales:

1. **DatabaseConnector**: Módulo para conectar y desconectar de una base de datos MySQL, y para leer datos de la base de datos utilizando consultas SQL.
2. **DataAnalyzer**: Módulo para realizar análisis estadísticos sobre el rendimiento de los empleados.
3. **DataVisualizer**: Módulo para generar visualizaciones de los datos, incluyendo histogramas y gráficos de dispersión.

## Estructura de Archivos

```
.
├── database.py                  # Módulo para la conexión a la base de datos
├── employeeperformance.sql      # Archivo SQL para la inserción de datos
├── main.py                      # Script principal para la ejecución del proyecto
├── README.md                    # Este archivo
```

## Requisitos

- Python 3.x
- MySQL Server
- Paquetes de Python:
  - pandas
  - mysql-connector-python
  - matplotlib

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/tu_usuario/tu_proyecto.git
   cd tu_proyecto
   ```

2. **Configurar la base de datos MySQL**

   Asegúrate de tener una instancia de MySQL en ejecución y crear una base de datos llamada `CompanyData`.

   ```sql
   CREATE DATABASE CompanyData;
   USE CompanyData;
   ```

   Luego, inserta los datos del archivo `employeeperformance.sql`:

   ```sql
   source employeeperformance.sql;
   ```

3. **Instalar las dependencias de Python**

   Utiliza `pip` para instalar las dependencias necesarias:

   ```bash
   pip install pandas mysql-connector-python matplotlib
   ```

## Uso

1. **Ejecutar el script principal**

   Modifica el archivo `main.py` si es necesario para cambiar la configuración de la base de datos, y luego ejecuta el script:

   ```bash
   python main.py
   ```

2. **Resultados esperados**

   - **Análisis de datos**: Estadísticas calculadas para cada departamento, incluyendo la media, mediana y desviación estándar de `performance_score` y `salary`.
   - **Visualización de datos**: Se generarán histogramas del rendimiento de los empleados por departamento y gráficos de dispersión que muestran la relación entre años con la empresa y rendimiento, y entre salario y rendimiento.

## Ejemplos de Ejecución

### Análisis Estadístico de Datos

El análisis incluye cálculos como la media, la mediana, y la desviación estándar del rendimiento (`performance_score`) y del salario (`salary`) de los empleados por departamento.

### Visualización de Datos

1. **Histograma de Rendimiento por Departamento**

   Muestra la distribución de los puntajes de rendimiento por cada departamento.

2. **Gráfico de Dispersión de Años con la Empresa vs. Rendimiento**

   Visualiza la relación entre los años que un empleado ha estado con la empresa y su rendimiento.

3. **Gráfico de Dispersión de Salario vs. Rendimiento**

   Muestra cómo el salario de un empleado puede correlacionarse con su rendimiento.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un _issue_ o envía un _pull request_ para cualquier mejora o corrección.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
