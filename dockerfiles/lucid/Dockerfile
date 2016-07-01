FROM docker-dev.yelpcorp.com/lucid_yelp
MAINTAINER John Billings <billings@yelp.com>

RUN apt-get update

RUN apt-get -y install dpkg-dev python-tox python-setuptools
RUN apt-get -y install python-dev debhelper libyaml-dev
RUN apt-get -y install dh-virtualenv python-pip

WORKDIR /work
