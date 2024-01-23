# Usamos la imagen oficial de Python desde Docker Hub
FROM python:3.8-slim-buster

# Establecemos un directorio de trabajo
WORKDIR /app

# Actualizamos los paquetes del sistema y instalamos las dependencias necesarias para wkhtmltopdf y RabbitMQ
RUN apt-get update -y && apt-get install -y \
    wget \
    xz-utils \
    libxrender1 \
    fontconfig \
    libxext6 \
    apt-transport-https \
    gnupg


# Copiamos los archivos necesarios al contenedor
COPY . .

# Instalamos Django
RUN pip install Django

EXPOSE 8080

# Ejecutamos el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

