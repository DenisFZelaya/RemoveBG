# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos y instala las dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask
RUN pip install gunicorn
RUN pip install rembg
RUN pip install numba

# Copia el contenido actual del directorio al contenedor en /app
COPY . /app

# Expone el puerto 5000
EXPOSE 5000

# Variable de entorno para habilitar la recarga automática
ENV FLASK_RUN_EXTRA_FILES="templates/"

# Comando para ejecutar la aplicación cuando se inicia el contenedor
# CMD ["python", "app.py"]
CMD ["flask", "run", "--host=0.0.0.0"]
# CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
# CMD ["python", "app.py", "runserver"]
