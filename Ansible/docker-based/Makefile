NUMBER?=01
.ONESHELL:
ANSIBLE_DOCKER_NAME?=docker-ansible

run: clean build
	docker run -it -v $(shell pwd)/../chapter-$(NUMBER):/root/chapter-$(NUMBER) --name $(ANSIBLE_DOCKER_NAME) $(ANSIBLE_DOCKER_NAME) /bin/bash

build:
	docker build -t $(ANSIBLE_DOCKER_NAME) -f Dockerfile .

clean:
	-docker stop $(ANSIBLE_DOCKER_NAME)
	-docker rm $(ANSIBLE_DOCKER_NAME)
