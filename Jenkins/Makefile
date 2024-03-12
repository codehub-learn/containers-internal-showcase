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

run-logstash: network clean-logstash
	docker run \
	-d \
	--network jenkins \
	--name logstash \
	-p 5044:5044 \
	-v $(shell pwd)/logstash.yml:/usr/share/logstash/config/logstash.yml \
	-v $(shell pwd)/logstash.conf:/usr/share/logstash/config/logstash.conf \
	logstash:8.10.2

clean-logstash:
	-docker stop logstash
	-docker rm logstash

run-elasticsearch: network volume-elasticsearch clean-elasticsearch
	docker run \
	-d \
	--network jenkins \
	-p 9200:9200 \
	-p 9300:9300 \
	-e "discovery.type=single-node" \
	-v elasticsearch-vol:/usr/share/elasticsearch \
	--name elasticsearch \
	elasticsearch:8.10.2

volume-elasticsearch:
	-docker volume create elasticsearch-vol

clean-volume-elasticsearch:
	-docker volume rm elasticsearch-vol

clean-elasticsearch:
	-docker stop elasticsearch
	-docker rm elasticsearch

run-kibana: network volume-kibana clean-kibana
	docker run \
	-d \
	--network jenkins \
	-p 5601:5601 \
	-e "elasticsearch.hosts=http://elasticsearch:9200" \
	--name kibana \
	kibana:8.10.2

volume-kibana:
	-docker volume create kibana-vol

clean-volume-kibana:
	-docker volume rm kibana-vol

clean-kibana:
	-docker stop kibana
	-docker rm kibana


run-fluentd: network volume-fluentd clean-fluentd
	docker run \
	-d \
	--network jenkins \
	-p 24224:24224 \
	-p 24224:24224/udp \
	-u fluent \
	-v $(shell pwd)/fluent.conf:/fluentd/etc/fluent.conf \
	--name fluentd \
	fluentd

volume-fluentd:
	-docker volume create fluentd-vol

clean-volume-fluentd:
	-docker volume rm fluentd-vol

clean-fluentd:
	-docker stop fluentd
	-docker rm fluentd

run-loki: network volume-loki clean-loki
	docker run \
	-d \
	--network jenkins \
	-p 3100:3100 \
	-v loki-vol:/loki \
	--name loki \
	grafana/loki

volume-loki:
	-docker volume create loki-vol

clean-volume-loki:
	-docker volume rm loki-vol

clean-loki:
	-docker stop loki
	-docker rm loki

run-promtail: clean-promtail
	docker run \
	-d \
	--network jenkins \
	--name promtail \
	grafana/promtail

clean-promtail:
	-docker stop promtail
	-docker rm promtail

stop-all: 
	-docker stop elasticsearch
	-docker stop kibana
	-docker stop logstash
	-docker stop prometheus
	-docker stop grafana
	-docker stop loki
	-docker stop promtail
	-docker stop $(JENKINS_NAME)
	-docker stop $(JENKINS_NAME)-agent
	-docker stop netdata
start-all: 
	-docker start elasticsearch
	-docker start kibana
	-docker start logstash
	-docker start prometheus
	-docker start grafana
	-docker start loki
	-docker start promtail
	-docker start $(JENKINS_NAME)
	-docker start $(JENKINS_NAME)-agent
	-docker stop netdata
	

run-netdata:
	docker run \
	-d \
	-p 19999:19999 \
	--name=netdata \
	--pid=host \
	--network=host \
	-v netdataconfig:/etc/netdata \
	-v netdatalib:/var/lib/netdata \
	-v netdatacache:/var/cache/netdata  \
	-v /etc/passwd:/host/etc/passwd:ro  \
	-v /etc/group:/host/etc/group:ro \
	-v /proc:/host/proc:ro \
	-v /sys:/host/sys:ro \
	-v /etc/os-release:/host/etc/os-release:ro \
	-v /var/run/docker.sock:/var/run/docker.sock:ro \
	--restart unless-stopped \
	--cap-add SYS_PTRACE \
	--cap-add SYS_ADMIN \
	--security-opt apparmor=unconfined  \
	netdata/netdata

clean-netdata:
	-docker stop netdata
	-docker rm netdata

clean-all: clean-jenkins clean-agent clean-grafana clean-prometheus clean-node-exporter clean-elasticsearch clean-logstash clean-kibana clean-loki clean-promtail clean-fluentd clean-netdata
