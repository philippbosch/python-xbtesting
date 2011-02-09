import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-xbtesting",
    version = __import__('xbtesting').__version__,
    author = "Philipp Bosch",
    author_email = "hello@pb.io",
    description = "A Python library to talk to the API provided by CrossBrowserTesting.com",
    license = "MIT",
    keywords = "python api crossbrowsertesting",
    url = "http://github.com/philippbosch/python-xbtesting/",
    packages=find_packages(),
    package_data={
        'xbtesting': [],
    },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'simplejson',
    ],
)