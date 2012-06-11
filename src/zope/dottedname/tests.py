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

$Id$
"""
import os,unittest
from zope.testing.doctest import DocFileSuite,REPORT_NDIFF,ELLIPSIS

def test_suite():
    return unittest.TestSuite((
        DocFileSuite(
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.txt')),
            optionflags=REPORT_NDIFF|ELLIPSIS,
            module_relative=False,
            ),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

