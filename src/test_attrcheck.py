# -*- coding:utf-8 -*-

from attrcheck import attrcheck
import unittest

class TestAttrCheck(unittest.TestCase):
    def test1(self):
        @attrcheck(x=['real'], y=['index', 'strip'], z=dir(list))
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
        @attrcheck(y=dir(str))
        def func(x, y=[]): pass

    def test2(self):
        self.assertRaises(AttributeError, self._test2)

    def test3(self):
        @attrcheck(x=['get'])
        def func(x):
            '''Func'''
            pass
        self.assertEqual(func.__name__, 'func')
        self.assertEqual(func.__doc__, 'Func')

if __name__ == '__main__':
    unittest.main()

