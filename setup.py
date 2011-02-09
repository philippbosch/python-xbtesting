import os
from setuptools import setup, find_packages

README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read().strip() + "\n\n"
def md2stx(s):
    import re
    s = re.sub(':\n(\s{8,10})', r'::\n\1', s)
    return s
long_description = md2stx(long_description)


setup(
    name = "python-xbtesting",
    version = __import__('xbtesting').__version__,
    author = "Philipp Bosch",
    author_email = "hello@pb.io",
    description = "A Python library to talk to the API provided by CrossBrowserTesting.com",
    long_description=long_description,
    license = "MIT",
    keywords = "python api crossbrowsertesting",
    url = "http://github.com/philippbosch/python-xbtesting/",
    download_url="http://pypi.python.org/pypi/python-xbtesting/",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
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