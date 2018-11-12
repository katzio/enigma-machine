# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='enigma-machine',
    version='1.0.0',
    description='Enigma Machine Simpulator',
    author='Aryeh Katz',
    url='https://github.com/katzio/enigma-machine.git',
    packages=find_packages(exclude=('tests'))
)

