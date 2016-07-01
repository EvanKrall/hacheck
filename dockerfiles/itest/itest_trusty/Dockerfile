FROM docker-dev.yelpcorp.com/trusty_yelp
MAINTAINER John Billings <billings@yelp.com>

RUN apt-get update && apt-get -y install python-dev

ADD itest.sh /itest.sh

RUN chmod +x /itest.sh

CMD /itest.sh
