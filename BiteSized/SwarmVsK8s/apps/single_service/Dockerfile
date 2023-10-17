FROM debian:bullseye-slim
RUN apt-get update
RUN apt-get install -y \
    apache2 \
    curl \
    iproute2 \
    net-tools \
    php
COPY index.php /var/www/html/index.php
COPY dir.conf /etc/apache2/mods-available/dir.conf
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]