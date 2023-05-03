FROM debian:bullseye-slim
RUN apt-get update && \
    apt-get install -y \
    python3 \
    curl \
    python3-pip
COPY requirements.txt /
RUN pip3 install -r requirements.txt
RUN mkdir /app
COPY *.py /app/
WORKDIR /app
CMD [ "flask", "run" , "-h", "0.0.0.0" ]
