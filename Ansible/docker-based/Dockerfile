FROM ubuntu:22.04
RUN apt-get update && apt-get install -y \
	openssh-server \
	python3 \
	sudo \
	git \
	iproute2 \
	wget  \
	software-properties-common

RUN apt-add-repository --yes --update ppa:ansible/ansible
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ansible
