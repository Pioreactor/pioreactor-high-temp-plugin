# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="pioreactor_high_temp_plugin",
    version="0.0.3",
    license="MIT",
    description="Do not use this. Using this risks damaging your Pioreactor or harming yourself. All responsibility is on you.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="cam@pioreactor.com",
    author="Cam Davidson Pilon",
    url="https://github.com/Pioreactor/pioreactor-high-temp-plugin",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "pioreactor.plugins": "pioreactor_high_temp_plugin = pioreactor_high_temp_plugin"
    },
)
