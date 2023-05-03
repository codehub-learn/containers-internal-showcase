FROM mysql:8
COPY my.cnf /etc/my.cnf
COPY init.sql /docker-entrypoint-initdb.d/01.sql
ENV MYSQL_RANDOM_ROOT_PASSWORD true
ENV MYSQL_DATABASE snm
ENV MYSQL_USER snm
ENV MYSQL_PASSWORD snm1234
EXPOSE 3306