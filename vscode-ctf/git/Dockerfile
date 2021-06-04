FROM httpd:2.4.48-alpine

RUN a2enmod cgi alias env && \
    mkdir -p /srv/git && \
    chgrp -R www-data /srv/git && \
    htpasswd -c /srv/git/.htpasswd
