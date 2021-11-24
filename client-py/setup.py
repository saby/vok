import os
import pathlib

from setuptools import setup


setup(
    name='sabyvok',
    version='1.0.0',
    description='Saby Vok API client',
    packages=['sabyvok'],
    install_requires=['requests'],
    author_email='mail@veseloff.net',
    zip_safe=False,
)
