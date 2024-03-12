push: tag
	docker push localhost:5000/webapp:latest

tag: build
	docker tag webapp:latest localhost:5000/webapp:latest

build:
	docker build -t webapp:latest .

clean:
	-docker stack rm webapp
