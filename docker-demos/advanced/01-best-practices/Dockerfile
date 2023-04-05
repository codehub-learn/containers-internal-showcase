FROM debian:bullseye-slim
RUN apt-get update && apt-get install apache2 -y \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/www/html
RUN echo "<h1>Hello</h1>" > /var/www/html/index.html
VOLUME /var/www/html
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
EXPOSE 80/tcp
