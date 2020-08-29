FROM python:3.7.7

RUN mkdir -p /opt/server
WORKDIR /opt/server

ADD server/requirements.txt /opt/server/requirements.txt
RUN pip3 install -r ./requirements.txt

ADD server /opt/server
CMD ./start.sh
