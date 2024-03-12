create: clean 
	docker stack deploy --compose-file docker-compose.yaml appstack

clean:
	-docker stack rm appstack
