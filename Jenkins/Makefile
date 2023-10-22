JENKINS_NAME?=jenkins
.ONESHELL:

run: clean volume network
	docker run -it -p 8080:8080 -v $(JENKINS_NAME)-vol:/var/jenkins_home --network jenkins  --name $(JENKINS_NAME) jenkins/jenkins:lts-jdk11

run-agent: clean-agent build-agent network
	docker run -it -p 2022:22 -v /var/run/docker.sock:/var/run/docker.sock --network jenkins --name $(JENKINS_NAME)-agent jenkins-agent

build-agent:
	cd Agents
	docker build -t jenkins-agent .
	
clean-agent:
	-docker stop $(JENKINS_NAME)-agent
	-docker rm $(JENKINS_NAME)-agent

clean:
	-docker stop $(JENKINS_NAME)
	-docker rm $(JENKINS_NAME)
volume:
	-docker volume create $(JENKINS_NAME)-vol

clean-volume:
	-docker volume rm $(JENKINS_NAME)-vol

network:
	-docker network create jenkins 

clean-network:
	-docker network rm jenkins

prometheus: network clean-prometheus
	docker run \
    -p 9090:9090 \
	--network jenkins \
	--name prometheus \
	-v /var/run/docker.sock:/var/run/docker.sock \
    -v $(shell pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus

clean-prometheus:
	-docker stop prometheus
	-docker rm prometheus
