import boto3
import pandas as pd
import mysql.connector

# Conexión a MySQL
conexion = mysql.connector.connect(
    host="34.199.222.110",
    port=3307,
    user="root",
    password="utec",
    database="db_actividad"
)

# Leer los datos de una tabla
consulta = "SELECT * FROM personas"
df = pd.read_sql(consulta, conexion)
conexion.close()

# Guardar en CSV
ficheroUpload = "data.csv"
df.to_csv(ficheroUpload, index=False)

# Subir a S3
nombreBucket = "act3-output-01"
s3 = boto3.client('s3')
s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada desde MySQL")
