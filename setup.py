#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import setuptools

# Read version from file without loading the module
with open('GrafanaSnapshot/version.py', 'r') as version_file:
    version_match = re.search(r"^VERSION ?= ?['\"]([^'\"]*)['\"]",
                              version_file.read(), re.M)
with open("README.md", "r") as fh:
    long_description = fh.read()


if version_match:
    VERSION=version_match.group(1)
else:
    VERSION='0.1' #

requirements = [
    'python-dotenv',
    'setuptools',
    'requests',
    'grafana_api'
]

test_requirements = [
    'tox',
    'coverage',
    'wheel',
    'pytest'
]

setuptools.setup(
    name="grafana-snapshot",
    version=VERSION,
    author="Authapon Kongkaew",
    author_email="ohmrefresh@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ohmrefresh/GrafanaSnapshot.git",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='tests',
    tests_require=test_requirements
)