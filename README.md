## 13909-2C2022 - Introducción a la programación: Software libre

### Pre-requisites

* [Docker for OSX or Docker for Windows](https://www.docker.com/products/docker)Docker for OSX or Docker for Windows

Ejecutar el siguiente comando en la carpeta raiz para crear la imagen.

docker build -t python -f Dockerfile .

Ejecutar el siguiente comando en la carpeta raiz para ejecutar la imagen.

docker run \
-it \
-e EJERCICIO=ejercicio-a \
--name python \
--mount type=bind,source="$PWD"/src,target=/usr/src/app/src \
--rm \
python