FROM ubuntu:18.04
LABEL maintainer="UiT The Arctic University of Norway"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 5000
CMD ["runserver.py"]
