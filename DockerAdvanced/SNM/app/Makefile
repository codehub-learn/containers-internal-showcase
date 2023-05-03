run: venv
	. venv/bin/activate; python3 -m flask run 

venv:
	virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt

image: 
	docker build -t app .

docker: image
	docker run -d -p 5000:5000 --name app app 

clean:
	-deactivate
	rm -rvf venv
	-docker stop app
	-docker rm -f app
