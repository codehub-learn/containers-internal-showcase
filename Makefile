JENKINS_NAME?=jenkins2
.ONESHELL:

run: clean-jenkins volume-jenkins network
	docker run \
		-d \
		-p 8080:8080 \
		-v $(JENKINS_NAME)-vol:/var/jenkins_home \
		-v /var/run/docker.sock:/var/run/docker.sock  \
		--network jenkins  \
		--name $(JENKINS_NAME) \
		jenkins/jenkins:lts-jdk17

run-agent: clean-agent build-agent network
	docker run \
		-d \
		-p 2022:22 \
		-v /var/run/docker.sock:/var/run/docker.sock \
		--network jenkins \
		--name $(JENKINS_NAME)-agent \
		jenkins-agent

build-agent:
	cd Agents
	docker build -t jenkins-agent .
	
clean-agent:
	-docker stop $(JENKINS_NAME)-agent
	-docker rm $(JENKINS_NAME)-agent

clean-jenkins:
	-docker stop $(JENKINS_NAME)
	-docker rm $(JENKINS_NAME)

network:
	-docker network create jenkins 

clean-network:
	-docker network rm jenkins

volume-jenkins:
	-docker volume create $(JENKINS_NAME)-vol

clean-volume-jenkins:
	-docker volume rm $(JENKINS_NAME)-vol


stop-all: 
	-docker stop $(JENKINS_NAME)
	-docker stop $(JENKINS_NAME)-agent
start-all: 
	-docker start $(JENKINS_NAME)
	-docker start $(JENKINS_NAME)-agent
	

clean-all: clean-jenkins clean-agent 
