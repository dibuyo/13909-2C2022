## 13909-2C2022 - Introducción a la programación: Software libre

### Pre-requisites

* [Docker for OSX or Docker for Windows](https://www.docker.com/products/docker)Docker for OSX or Docker for Windows

### Ejecutar el siguiente comando en la carpeta raiz para crear la imagen.

```console
docker build -t python -f Dockerfile .
```

### Ejecutar el siguiente comando en la carpeta raiz para ejecutar la imagen.

```console
docker run \
-it \
--name python \
--mount type=bind,source="$PWD"/src,target=/usr/src/app/src \
--rm \
-e EJERCICIO=ejercicio-a \
python
```