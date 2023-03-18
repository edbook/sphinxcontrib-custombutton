#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = """
A custom button for Sphinx
"""

requires = ["Sphinx>=0.6", "setuptools"]


setup(
    name="sphinxcontrib-custombutton",
    version="2.0",
    description="Sphinx custom button",
    author="Unknow",
    maintainer="Benedikt Magnusson",
    maintainer_email="bsm@hi.is",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["sphinxcontrib"],
)
