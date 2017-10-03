FROM ubuntu:15.10
RUN apt-get -y  update && apt-get -y upgrade
RUN apt-get -y install build-essential
RUN apt-get -y install wget
RUN echo "mysql-server mysql-server/root_password password SeC-0n4b" | debconf-set-selections && \
    echo "mysql-server mysql-server/root_password_again password SeC-0n4b" | debconf-set-selections && \
    apt-get -y install mysql-server
RUN apt-get -y install apache2 php5 php5-mysql
RUN bash -c "echo \"[mysqld]\nsecure-file-priv = '/usr/local/sqli/pub/'> /etc/my.cnf\";mkdir -p /usr/local/sqli/pub"
RUN bash -c "chown www-data:www-data /usr/local/sqli -R"
RUN bash -c "mysql_install_db --datadir=/var/lib/mysql --user=mysql"

ADD ./apache2.conf /etc/apache2/apache2.conf
ADD ./000-default.conf /etc/apache2/sites-enabled/000-default.conf
ADD ./sql.sql /tmp/sql.sql
ADD ./index.php /usr/local/sqli/pub/index.php



CMD ["bash", "-c", "export APACHE_LOG_DIR=/tmp/; /usr/bin/mysqld_safe & sleep 3 | /usr/bin/mysqladmin -u root password 'SeC-0n4b' & /usr/sbin/apache2 -D FOREGROUND"]
EXPOSE 80


