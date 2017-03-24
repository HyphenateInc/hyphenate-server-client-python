#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hyphenate inc'

import os
import sys

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            # import here, because outside the eggs aren't loaded
            import pytest
            errno = pytest.main(self.test_args)
            sys.exit(errno)

except ImportError:

    from distutils.core import setup

    def PyTest(x): x

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

f = open(os.path.join(os.path.dirname(__file__), 'VERSION'))
_version_ = f.read()
f.close()


setup(
    name='hyphenateserver',
    version=_version_,
    description='Python Client Library for Hyphenate REST API',
    long_description=long_description,
    url='https://github.com/HyphenateInc/hyphenate-server-client-python',
    author='Hyphenate Inc',
    author_email='info@hyphenate.io',
    maintainer='Hyphenate[https://www.hyphenate.io]',
    maintainer_email='support@hyphenate.io',
    license='Apache 2.0',
    keywords=['hyphenate', 'rest', 'api', 'client library', 'im'],
    packages=['hyphenateserver'],
    tests_require=['pytest>=2.7.0'],
    cmdclass={'test': PyTest}
)
