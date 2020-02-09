from setuptools import setup, find_packages
import re

# Read version from file without loading the module
with open('GrafanaSnapshot/version.py', 'r') as version_file:
    version_match = re.search(r"^VERSION ?= ?['\"]([^'\"]*)['\"]",
                              version_file.read(), re.M)

with open("README.md", "r") as fh:
    long_description = fh.read()

if version_match:
    VERSION = version_match.group(1)
else:
    VERSION = '0.1'  #

setup(
    name="grafana-snapshot",
    version=VERSION,
    author="Authapon Kongkaew, Nitipat Phiphatprathuang, Panchorn Lertvipada",
    author_email="ohmrefresh@gmail.com, banknitipat@gmail.com, nonpcn@gmail.com",
    description="Task a grafana snapshot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ascendcorp/grafana-snapshot.git",
    license="MIT",
    packages=find_packages(),
    install_requires=['requests', 'grafana_api==0.9.0'],
    tests_require=['tox', 'coverage', 'wheel', 'requests_mock', 'pytest'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
    ]
)
