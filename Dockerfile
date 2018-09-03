# Stage 0: Build the webserver
FROM ubuntu:18.04
LABEL maintainer="UiT The Arctic University of Norway"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential redis-server
COPY . /app
WORKDIR /app
RUN pip3 install pip --upgrade --no-cache-dir
RUN pip3 install setuptools --upgrade --no-cache-dir
RUN pip3 install -r requirements.txt
COPY conf/redis.conf /etc/redis/
ENTRYPOINT ["python3"]
EXPOSE 5000
CMD ["runserver.py"]
