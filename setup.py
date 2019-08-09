from subprocess import check_output
from setuptools import setup, find_packages


def get_version():
    try:
        tag = check_output(
            ["git", "describe", "--tags", "--abbrev=0", "--match=[0-9]*"]
        )
        return tag.decode("utf-8").strip("\n")
    except Exception:
        raise RuntimeError(
            "The version number cannot be extracted from git tag in this source "
            "distribution; please either download the source from PyPI, or check out "
            "from GitHub and make sure that the git CLI is available."
        )


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="grafana-snapshot",
    version=get_version(),
    author="Authapon Kongkaew, Panchorn Lertvipada",
    author_email="ohmrefresh@gmail.com, nonpcn@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ascendcorp/GrafanaSnapshot.git",
    license="MIT",
    packages=find_packages(),
    install_requires=['requests', 'grafana_api'],
    tests_require=['tox', 'coverage', 'wheel', 'requests_mock', 'xmlrunner', 'pytest', 'unittest-xml-reporting'],
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
