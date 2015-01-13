#!/usr/bin/env python

from setuptools import setup
from register import __VERSION__

DESCRIPTION = (
    'Library to read registers from XML and write into xls(Excel), '
    'LaTeX, PDF, C header, or Verilog code.'
    )

LONG_DESCRIPTION = """\
"""

CLASSIFIERS = [
    ]

KEYWORDS = (
    'xml register sfr xls tex pdf c_header verilog hardware'
    )

setup(
    name = 'register',
    version = __VERSION__,
    maintainer = 'Eunchan Kim',
    maintainer_email = 'helpbygrace@gmail.com',
    url = 'http://bitbucket.org/eunchan/register/',
    download_url = 'http://bitbucket.org/eunchan/register/',
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    license = 'BSD',
    platforms = 'Platform Independent',
    packages = ['register'],
    keywords = KEYWORDS,
    classifiers = CLASSIFIERS,
    package_data = {
        'register': [
            'examples/*.*',
            ],
        },
    install_requires=['openpyxl'],
    test_suite='register.tests',
    )
