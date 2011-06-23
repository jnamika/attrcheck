# -*- coding:utf-8 -*-

import attrcheck
import unittest

class TestFoo(unittest.TestCase):
    def test1(self):
        @attrcheck.attrcheck(x=['real'], y=['index', 'strip'], z=dir(list))
        def func(x, y, z=[]): pass
        func(0, 'y')
        func(1, 'y', [])
        self.assertRaises(AttributeError, func, '0', 'y')
        self.assertRaises(AttributeError, func, x='0', y='y')
        self.assertRaises(AttributeError, func, 0, 1)
        self.assertRaises(AttributeError, func, x=0, y=1)
        self.assertRaises(AttributeError, func, 0, 'y', 3)
        self.assertRaises(AttributeError, func, x=1, y='y', z=3)

    def _test2(self):
        @attrcheck.attrcheck(y=dir(str))
        def func(x, y=[]): pass

    def test2(self):
        self.assertRaises(AttributeError, self._test2)

if __name__ == '__main__':
    unittest.main()

