# Utiliza una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos requirements.txt y app.py en el contenedor
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY models.py models.py
COPY entrypoint.sh entrypoint.sh
COPY wait_for_postgres.py wait_for_postgres.py

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Da permisos de ejecución al script de entrada
RUN chmod +x entrypoint.sh

# Ejecuta el script de entrada
ENTRYPOINT ["./entrypoint.sh"]
