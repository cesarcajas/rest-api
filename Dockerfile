FROM alpine:3.10

RUN apk add --no-cache python3-dev\
    && pip3 install --upgrade pip

WORKDIR /server

COPY . /server/

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "sourcecode/server.py"]
