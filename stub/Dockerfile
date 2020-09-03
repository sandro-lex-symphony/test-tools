FROM ubuntu:18.04
RUN apt-get update && \
 apt-get install -y vim curl wget apache2
RUN sed -i 's/80/8081/g' /etc/apache2/ports.conf && \
 sed -i 's/80/8081/g' /etc/apache2/sites-available/000-default.conf
RUN echo "hello world" > /var/www/html/index.html
CMD ["/usr/sbin/apachectl", "-DFOREGROUND"]


