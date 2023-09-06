build:
	docker build -t debian-server .

run: clean build
	docker run -d -p 2022:22 --name debian-server debian-server

clean:
	docker stop debian-server
	docker rm debian-server

