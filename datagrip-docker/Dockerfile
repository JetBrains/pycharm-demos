FROM postgres:12

ADD conf /etc/postgresql-common/ssl.conf

ADD cert /var/ssl/
ADD cert /var/ssl/

# Add the ssl config setup script
COPY conf /usr/share/postgresql/12/pg_hba.conf.sample
COPY conf /usr/share/postgresql/12/postgresql.conf.sample
COPY cert ./cert/server.key /var/ssl/
RUN chown postgres.postgres /usr/share/postgresql/12/pg_hba.conf.sample \
                            /usr/share/postgresql/12/postgresql.conf.sample \
                            /var/ssl/server.key \
                            /var/ssl/server.crt && \
    chmod 600 /var/ssl/server.key &&\
    chgrp postgres /var/ssl/server.key &&\
    chown postgres /var/ssl/server.key

ENV LOCALE_CONFIG /etc/locale.gen
RUN sed -ri 's/#\ fr_FR.UTF-8\ UTF-8/fr_FR.UTF-8\ UTF-8/' ${LOCALE_CONFIG}
RUN sed -ri 's/#\ en_US.UTF-8\ UTF-8/en_US.UTF-8\ UTF-8/' ${LOCALE_CONFIG}
RUN cd /usr/sbin/ && ./locale-gen
