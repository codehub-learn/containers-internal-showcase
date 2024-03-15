## Jenkins instructions
This repository is a demo of a CI pipeline with testing

### Start Jenkins
`cd Jenkins`
`make run`

### Start Jenkins-agent
`cd Jenkins`
`make run-agent`

### Change /var/run/docker in agent
`docker exec -it jenkins-agent bash`
`chmod 666 /var/run/docker.sock`

Press Ctrl-D to exit

*This hack is needed for Jenkins to run the pipeline*


### Login to Jenkins
- When Jenkins container starts it prints a password. Copy that.
- Open a browser in http://localhost:8080
- Press accept and put your password when prompted
- Wait till Jenkins setup is finished


### Add plugins to Jenkins
You will need to install the following plugins
- Locale
- github
- github-pipeline
- maven-integration
- pipeline-maven
- docker
- docker-pipeline
- docker-build and publish

### Add credentials to Jenkins
You need to add some credentials to Jenkins.
You need credentials from:
- github
- dockerhub
- jenkins-agent

The github and dockerhub tokens can be created by following the guides here:

https://docs.docker.com/security/for-developers/access-tokens/

https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

* Note:
Name the credentials for docker: *dockercredentials* and the credentials for github: *github*

For Jenkins Agent add a username/password credentials set with values:
username: andrew
password: passw0rd

### Add Jenkins Agent to Jenkins as node
- Open Jenkins
- Go to Dashboard -> Manage Jenkins -> Nodes -> New Node
- Select Permanent Agent and give a name
- On the next page add the following:
    - Number of executors: 3
    - Remote root directory: /var/jenkins
    - Labels: docker
    - Launch method: Launch Agents via SSH
    - Host: jenkins-agent
    - Credentials: The jenkins-agent credentials created above
    - Host Key Verification Strategy: Non verifying Verification Strategy
- Press Save

### Create your first job
- Create a new Pipeline Jon
- Select Pipeline Script from SCM
- Put this repository as Repository URL
- Select github credentials

### Run the Pipeline
Well, if you made it congrats. You can run the pipeline now.

