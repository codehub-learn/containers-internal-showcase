FROM debian:bullseye-slim AS builder
RUN apt-get update
RUN apt-get install -y \
    openjdk-11-jdk \
    maven
RUN mkdir /app
COPY src /app/src
COPY pom.xml /app
RUN mvn clean package

FROM debian:bullseye-slim AS staging
RUN apt-get update && apt-get install -y openjdk-11-jdk
COPY --from=builder /app/target/JPrint-1.0-SNAPSHOT.jar /JPrint-1.0-SNAPSHOT.jar
EXPOSE 8900
CMD ["java", "-jar", "/JPrint-1.0-SNAPSHOT.jar"]



