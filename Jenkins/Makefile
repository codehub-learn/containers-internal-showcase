run: clean volume
	docker run -it -p 8080:8080 -v jenkins-vol:/var/jenkins_home --name jenkins jenkins/jenkins:lts-jdk11

clean:
	-docker stop jenkins
	-docker rm jenkins
volume:
	-docker volume create jenkins-vol

volume_clean:
	-docker volume rm jenkins-vol