FROM ubuntu:18.04
LABEL maintainer="UiT The Arctic University of Norway"
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
RUN echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential mongodb-org
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 5000
CMD ["mongod","runserver.py"]
