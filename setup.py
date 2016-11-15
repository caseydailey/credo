"""
Credo setup
"""

__author__ = 'Jon Staples'
from setuptools import setup, find_packages
from credo import __version__

setup(
    name='credo',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "gitchangelog",
        "pyaml",
        "pystache"
    ],
    license='',
    author='Jon Staples',
    author_email='jonstaples314@gmail.com',
    description='Belief Management framework.'
)
