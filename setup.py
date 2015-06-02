##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.pagetemplate package
"""
import os
import sys
from setuptools import setup, find_packages

PY3 = sys.version_info[0] >= 3


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

def _modname(path, base, name=''):
    if path == base:
        return name
    dirname, basename = os.path.split(path)
    return _modname(dirname, base, basename + '.' + name)

def alltests():
    import logging
    import pkg_resources
    import unittest

    class NullHandler(logging.Handler):
        level = 50

        def emit(self, record):
            pass

    logging.getLogger().addHandler(NullHandler())

    suite = unittest.TestSuite()
    base = pkg_resources.working_set.find(
        pkg_resources.Requirement.parse('zope.pagetemplate')).location
    for dirpath, dirnames, filenames in os.walk(base):
        if os.path.basename(dirpath) == 'tests':
            for filename in filenames:
                if ( filename.endswith('.py') and
                     filename.startswith('test') ):
                    mod = __import__(
                        _modname(dirpath, base, os.path.splitext(filename)[0]),
                        {}, {}, ['*'])
                    suite.addTest(mod.test_suite())
    return suite

TESTS_REQUIRE = [
    'zope.testing',
    'zope.proxy',
    'zope.security',
] + (['zope.untrustedpython'] if not PY3 else [])


setup(name='zope.pagetemplate',
      version='4.2.1.dev0',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      description='Zope Page Templates',
      long_description=(
          read('README.rst')
          + '\n\n' +
          'Detailed Documentation\n' +
          '----------------------'
          + '\n\n' +
          read('src', 'zope', 'pagetemplate', 'architecture.txt')
          + '\n\n' +
          read('src', 'zope', 'pagetemplate', 'readme.txt')
          + '\n\n' +
          read('CHANGES.rst')),
      keywords="zope3 page template",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3'],
      url='http://pypi.python.org/pypi/zope.pagetemplate',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope'],
      extras_require=dict(
          test=TESTS_REQUIRE,
          untrusted=['zope.untrustedpython'] if not PY3 else [],
      ),
      install_requires=['setuptools',
                        'six',
                        'zope.interface',
                        'zope.component',
                        'zope.tales',
                        'zope.tal',
                        'zope.i18n',
                        'zope.i18nmessageid',
                        'zope.traversing',
                       ],
      include_package_data=True,
      zip_safe=False,
      tests_require=TESTS_REQUIRE,
      test_suite='__main__.alltests',
      )
