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
		jenkins/jenkins:lts-jdk11

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


run-prometheus: network clean-prometheus
	docker run \
	-d \
    -p 9090:9090 \
	--network jenkins \
	--name prometheus \
    -v $(shell pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus

clean-prometheus:
	-docker stop prometheus
	-docker rm prometheus

volume-grafana:
	-docker volume create grafana-vol

clean-volume-grafana:
	-docker volume rm grafana-vol

run-grafana: network clean-grafana
	docker run \
	-d \
    -p 3000:3000 \
	-v grafana-vol:/var/lib/grafana \
	--network jenkins \
	--name grafana \
    grafana/grafana

clean-grafana:
	-docker stop grafana
	-docker rm grafana

run-node-exporter: network clean-node-exporter
	docker run \
	-d \
    -p 9100:9100 \
	--network jenkins \
	--name node-exporter \
    bitnami/node-exporter

clean-node-exporter:
	-docker stop node-exporter
	-docker rm node-exporter

clean: clean-jenkins clean-agent clean-grafana clean-prometheus clean-node-exporter

