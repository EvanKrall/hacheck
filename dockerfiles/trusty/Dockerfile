FROM docker-dev.yelpcorp.com/trusty_yelp
MAINTAINER John Billings <billings@yelp.com>

RUN rm -f /etc/apt/sources.list.d/proposed.list
RUN apt-get update

RUN apt-get -y install dpkg-dev python-tox python-setuptools dh-virtualenv
RUN apt-get -y install python-dev debhelper libyaml-dev

WORKDIR /work
