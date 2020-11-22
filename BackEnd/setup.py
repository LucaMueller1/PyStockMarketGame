# coding: utf-8
"""
desc: Setup is used to package and build the project through setuptools
date: 2020-11-07
"""

from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="PyBroker",
    author_email="",
    url="",
    keywords=["Swagger", "PyBroker"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Absolute legendary PyBroker BackEnd API
    """
)

