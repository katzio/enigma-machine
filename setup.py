# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='enigma-machine',
    version='0.1.0',
    description='Enigma Machine Simpulator',
    long_description=readme,
    author='Aryeh Katz',
    url='https://github.com/katzio/enigma-machine.git',
    license=license,
    packages=find_packages(exclude=('tests'))
)

