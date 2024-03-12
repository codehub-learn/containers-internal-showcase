FROM debian:bullseye-slim
RUN groupadd -g 1001 docker
RUN apt-get update && apt-get install -y \
	openssh-server \
	openjdk-11-jdk-headless \
	python3 \
	sudo \
	git \
	iproute2 \
	wget  \
    curl \
	docker.io
EXPOSE 22
COPY start.sh /start.sh
RUN chmod 700 /start.sh
RUN useradd -rm -d /home/andrew -s /bin/bash -g root -G sudo,docker,root -u 2000 andrew
RUN echo "andrew:passw0rd" | chpasswd
RUN echo "Sleeping for 14400 sec"
CMD ["/start.sh"]
