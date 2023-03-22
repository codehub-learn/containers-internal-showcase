# A Small python app
This small python app instantiates a small Flask app, which acts as a simple web server.
It expects to find a Redis instance (denoted by REDIS_HOST env var) and 
then instantiates a connection to it.
In version 2.0 every time someone access the / path in the app, it calls a function to 
increase a key in redis ("hits") and returns the value to the web client.
In version 3.0 of this app, additionally the hostname of the machine/pod running the app is returned also to the
web client


## Docker image creation
Just run 

`docker build -t simpleapp .`

## Local run
Execute

`docker-compose up -d
`


