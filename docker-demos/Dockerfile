FROM debian:bullseye-slim
USER root
RUN apt-get update && apt-get install -y curl
RUN useradd kostas
USER kostas
CMD ["whoami"]



