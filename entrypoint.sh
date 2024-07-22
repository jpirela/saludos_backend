#!/bin/sh

# Espera a que PostgreSQL esté disponible ejecutando el script de Python
python wait_for_postgres.py

# Ejecuta la aplicación
python app.py
