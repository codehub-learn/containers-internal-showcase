TAG ?= "latest"
push: build tag
	docker push localhost:5000/indian:$(TAG)
tag:
	docker tag indian:$(TAG) localhost:5000/indian:$(TAG)

build: 
	docker build -t indian:$(TAG) .
