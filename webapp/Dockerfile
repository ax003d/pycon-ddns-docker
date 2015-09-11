FROM python:2.7

MAINTAINER Robert Zheng <rzheng@xtremeprog.com>

RUN mkdir -p /root/.pip
COPY pip.conf /root/.pip/
RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD webapp.py webapp.py
COPY docker-entrypoint.sh /usr/local/bin/

EXPOSE 80
ENTRYPOINT ["docker-entrypoint.sh"]
CMD [""]