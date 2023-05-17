build:
	docker build -t db  - < Dockerfile


run: clean build
	docker run --name=db \
		--mount type=bind,src=$(shell pwd)/my.cnf,dst=/etc/my.cnf \
		--mount type=bind,src=$(shell pwd)/data,dst=/var/lib/mysql \
		--mount type=bind,src=$(shell pwd)/init.sql,dst=/docker-entrypoint-initdb.d/01.sql \
		-p 3306:3306 \
		-d db

clean: 
	-docker rm -f db
	
