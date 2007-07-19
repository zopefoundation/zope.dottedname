##############################################################################
#
# Copyright (c) 2007 Zope Corporation and Contributors.
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
"""Setup for zope.documenttemplate package

$Id$
"""

import os.path

from setuptools import setup, find_packages


here = os.path.dirname(os.path.abspath(__file__))
resolve_txt = os.path.join(here, "src", "zope", "dottedname", "resolve.txt")

setup(
    name="zope.dottedname",
    version = '3.4.1',
    url='http://svn.zope.org/zope.dottedname',
    license='ZPL 2.1',
    description='Resolver for Python dotted names.',
    long_description=open(resolve_txt).read().rstrip(),
    author='Zope Corporation and Contributors',
    author_email='zope3-dev@zope.org',

    packages=find_packages('src'),
    package_dir={'':'src'},
    namespace_packages=['zope'],
    include_package_data=True,
    install_requires = ['setuptools'],
    zip_safe = False
    )

