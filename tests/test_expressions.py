##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import os, sys, unittest

from zope.pagetemplate.engine import Engine

class Data:

    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self): return self.name


def dict(**kw):
    return kw


class ExpressionTests(unittest.TestCase):

    def testCompile(self):
        # Test expression compilation
        context = Data(
            vars = dict(
              x = Data(
                 name = 'xander',
                 y = Data(
                    name = 'yikes',
                    z = Data(name = 'zope')
                    )
                 ),
              y = Data(z = 3),
              b = 'boot',
              B = 2,
              )
            )


        engine = Engine

        expr = engine.compile('x')
        self.assertEqual(expr(context), context.vars['x'])

        expr = engine.compile('x/y')
        self.assertEqual(expr(context), context.vars['x'].y)

        expr = engine.compile('x/y/z')
        self.assertEqual(expr(context), context.vars['x'].y.z)

        expr = engine.compile('path:a|b|c/d/e')
        self.assertEqual(expr(context), 'boot')

        expr = engine.compile('string:Fred')
        self.assertEqual(expr(context), 'Fred')

        expr = engine.compile('string:A$B')
        self.assertEqual(expr(context), 'A2')

        expr = engine.compile('string:a ${x/y} b ${y/z} c')
        self.assertEqual(expr(context), 'a yikes b 3 c')

        expr = engine.compile('python: 2 + 2')
        self.assertEqual(expr(context), 4)

        expr = engine.compile('python: 2 \n+\n 2\n')
        self.assertEqual(expr(context), 4)


def test_suite():
    return unittest.makeSuite(ExpressionTests)


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
