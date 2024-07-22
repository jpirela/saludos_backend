#!/bin/sh

# Espera a que PostgreSQL esté disponible
while ! nc -z db 5432; do
  echo "Esperando a que PostgreSQL arranque..."
  sleep 1
done

# Ejecuta la aplicación
python app.py
