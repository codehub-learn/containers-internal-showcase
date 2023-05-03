

docker: image
	docker run -d -p 3306:3306 --name db db

image: 
	docker build -t db .

clean:
	-docker stop db
	-docker rm -f db
