## 13909-2C2022 - Introducción a la programación: Software libre

### Pre-requisites

* [Docker for OSX or Docker for Windows](https://www.docker.com/products/docker)Docker for OSX or Docker for Windows

### Ejecutar el siguiente comando en la carpeta raiz para crear la imagen.

```console
docker build -t python -f Dockerfile . --build-arg VERSION=3.8
```

### Ejecutar el siguiente comando en la carpeta raiz para ejecutar la imagen.

La variable de entorno EJERCICIO puede ser modificada por el nombre del archivo a ejecutar. En el siguiente ejemplo se ejecuta el ejercicio-a.

```console
docker run \
-it \
--name python \
--mount type=bind,source="$PWD"/src,target=/usr/src/app/src \
--mount type=bind,source="$PWD"/data,target=/usr/src/app/data \
--rm \
-e EJERCICIO=trabajo-practico-labs \
python
```