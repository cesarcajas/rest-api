FROM ubuntu:20.04
RUN apt-get update \
&& apt-get -y install python3-dev \
&& apt-get -y install python3-pip
WORKDIR /REST-API
COPY . /REST-API/

RUN apt-get -y install python3-venv
RUN mkdir flask_app && cd flask_app
RUN python3 -m venv venv

RUN pip3 install Flask
RUN python3 -m pip install requests 
CMD [ "python3", "server.py" ]

