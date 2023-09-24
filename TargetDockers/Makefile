NUMBER?=01
.ONESHELL:

run: build run_debian run_fedora

clean: clean_debian clean_fedora

build: build_debian build_fedora

build_debian:
	docker build -t debian-server -f Dockerfile_debian .

run_debian: clean_debian build_debian
	docker run -d -p 1$(NUMBER)22:22 -p 1$(NUMBER)80:80 --name debian-$(NUMBER) debian-server; 

clean_debian:
	-docker stop debian-$(NUMBER)
	-docker rm debian-$(NUMBER)

build_fedora:
	docker build -t fedora-server -f Dockerfile_fedora .

run_fedora: clean_debian build_debian
	docker run -d -p 2$(NUMBER)22:22 -p 2$(NUMBER)80:80 --name fedora-$(NUMBER) fedora-server

clean_fedora:
	-docker stop fedora-$(NUMBER)
	-docker rm fedora-$(NUMBER)



