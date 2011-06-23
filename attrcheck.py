# -*- coding:utf-8 -*-

import inspect

def attrcheck(*arguments, **keywords):
    errmsg = "Error checking argument %r of function %r with hasattr(%r, '%s')"
    def _(f):
        spec = inspect.getargspec(f)
        def __(*args, **kw):
            def check(k):
                if k in keywords:
                    for n in keywords[k]:
                        if not hasattr(v, n):
                            raise AttributeError(errmsg % (k, f.__name__, v, n))
            for i,v in enumerate(args):
                k = spec.args[i]
                check(k)
            for k,v in kw.iteritems():
                check(k)
            return f(*args, **kw)
        return __
    return _

