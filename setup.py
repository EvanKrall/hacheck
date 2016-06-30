#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="hacheck",
    version="0.9.0",
    author="James Brown",
    author_email="jbrown@uber.com",
    url="https://github.com/uber/hacheck",
    license="MIT",
    packages=find_packages(exclude=['tests']),
    keywords=["monitoring", "load-balancing", "networking"],
    description="HAProxy health-check proxying service",
    install_requires=[
        'tornado>=4.1,<=4.3',
        'PyYAML>=3.0',
        'six>=1.4.0',
    ],
    test_suite="nose.collector",
    entry_points={
        'console_scripts': [
            'haup = hacheck.haupdown:up',
            'hadown = hacheck.haupdown:down',
            'hashowdowned = hacheck.haupdown:status_downed',
            'hastatus = hacheck.haupdown:status',
            'halist = hacheck.haupdown:halist',
            'hacheck = hacheck.main:main',
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Monitoring",
    ]
)
