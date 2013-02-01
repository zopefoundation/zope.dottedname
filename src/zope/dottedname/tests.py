##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
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
"""test resolution of dotted names
"""
import unittest
import doctest
import os
import re

from zope.testing.renormalizing import RENormalizing

README = os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.txt'))
FLAGS = doctest.REPORT_NDIFF | doctest.ELLIPSIS

def test_suite():
    checker = RENormalizing([
        # datetime is a class in Python 3, but a type in Python 2
        (re.compile("<class 'datetime\.datetime'>"),
         "<type 'datetime.datetime'>"),
        # Python 3.2 adds quotes around the module name
        (re.compile("ImportError: No module named '([^']*)'"),
         r"ImportError: No module named \1"),
        # and improves the message in other ways too
        (re.compile(r"ImportError: No module named datetime\.foo;"
                    " datetime is not a package"),
         "ImportError: No module named foo"),
        # PyPy 1.9 has some different error messages and reprs
        (re.compile(r"ImportError: No module named datetime\.foo"),
         "ImportError: No module named foo"),
        (re.compile(r"<bound method type\.now of <type 'datetime\.datetime'>>"),
         "<built-in method now of type object at ...>"),
    ])
    return unittest.TestSuite((
        doctest.DocFileSuite(README,
                             checker=checker,
                             optionflags=FLAGS,
                             module_relative=False),
    ))
