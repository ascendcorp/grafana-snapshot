from setuptools import setup, find_packages
import os


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="grafana-snapshot",
    version=read('VERSION'),
    author="Authapon Kongkaew, Nitipat Phiphatprathuang, Panchorn Lertvipada",
    author_email="ohmrefresh@gmail.com, banknitipat@gmail.com, nonpcn@gmail.com",
    description="Task a grafana snapshot",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/ascendcorp/GrafanaSnapshot.git",
    license="MIT",
    packages=find_packages(),
    install_requires=['requests', 'grafana_api'],
    tests_require=['tox', 'coverage', 'wheel', 'requests_mock', 'pytest'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
    ]
)
