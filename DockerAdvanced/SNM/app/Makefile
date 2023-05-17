docker: clean image network
	docker run --name app \
		-p 6000:6000 \
		--net appnet \
		-e APP_PORT=6000 \
		-d app


run: venv
	. venv/bin/activate; cd src; python3 -m flask run 

venv:
	virtualenv venv
	. venv/bin/activate; cd src; pip install -Ur requirements.txt

network:
	-docker network create -d bridge appnet

image: 
	docker build -t app .

clean:
	-deactivate
	rm -rvf venv
	-docker stop app
	-docker rm -f app
	-docker network rm appnet
