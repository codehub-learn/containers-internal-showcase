FROM debian:bullseye-slim
RUN apt-get update
RUN apt-get install -y curl \
    python3
ADD app.py /
CMD ["python3", "-u", "/app.py", "0.0.0.0", "8000"]
