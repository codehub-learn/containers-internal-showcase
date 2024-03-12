FROM debian:bullseye-slim
RUN apt-get update && apt-get install -y python3 iputils-ping curl
COPY app.py /
ENTRYPOINT ["python3", "app.py"]
