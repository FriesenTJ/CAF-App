# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in caf/__init__.py
from caf import __version__ as version

setup(
	name="caf",
	version=version,
	description="CAF",
	author="Friesen Tjou Jazernicky",
	author_email="friesen.tjou@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
