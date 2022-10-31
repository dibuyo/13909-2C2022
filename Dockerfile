ARG  VERSION=2.7
FROM python:${VERSION}

ENV EJERCICIO main

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "start.py $EJERCICIO" ]

ENTRYPOINT ["sh", "-c", "python start.py $EJERCICIO"]