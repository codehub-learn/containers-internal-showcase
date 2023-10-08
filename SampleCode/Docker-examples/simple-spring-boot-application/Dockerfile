FROM debian:bullseye-slim
RUN apt-get update && apt-get install -y openjdk-11-jdk maven
#COPY simple-spring-boot-application / 
RUN ["mvn", "clean", "package"]
ENTRYPOINT ["java", "-jar", "/target/simple-project-0.0.1-SNAPSHOT.jar"]
