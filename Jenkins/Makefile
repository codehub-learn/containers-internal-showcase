.ONESHELL:

run: clean volume
	docker run -it -p 8080:8080 -v jenkins-vol:/var/jenkins_home  --name jenkins jenkins/jenkins:lts-jdk11

run-agent: clean-agent build-agent
	docker run -it -p 2022:22 -v /var/run/docker.sock:/var/run/docker.sock --name jenkins-agent jenkins-agent

build-agent:
	cd Agents
	docker build -t jenkins-agent .
	
clean-agent:
	-docker stop jenkins-agent
	-docker rm jenkins-agent

clean:
	-docker stop jenkins
	-docker rm jenkins
volume:
	-docker volume create jenkins-vol

volume_clean:
	-docker volume rm jenkins-vol
