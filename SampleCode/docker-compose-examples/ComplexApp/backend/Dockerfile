FROM debian:bullseye-slim
RUN apt-get update && apt-get install -y python3 iputils-ping curl
COPY backend.py /
ENTRYPOINT ["python3", "backend.py"]
