FROM debian:bullseye-slim
RUN apt-get update
RUN apt-get install -y \
    openjdk-11-jdk
ADD target/JPrint-1.0-SNAPSHOT.jar /JPrint-1.0-SNAPSHOT.jar
CMD ["java", "-jar", "/JPrint-1.0-SNAPSHOT.jar"]
