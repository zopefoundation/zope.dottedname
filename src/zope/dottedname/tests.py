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

README = os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.txt'))
FLAGS = doctest.REPORT_NDIFF | doctest.ELLIPSIS

def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite(README, optionflags=FLAGS, module_relative=False),
    ))
