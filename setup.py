

from setuptools import setup, find_packages

setup(
    name='yourappname',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'yourappname=yourappname:main',
        ],
    },
)