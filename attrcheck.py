# -*- coding:utf-8 -*-

import inspect

def attrcheck(*arguments, **keywords):
    errmsg = "Error checking argument %r of function %r with hasattr(%r, '%s')"
    def _(f):
        def check(k, v):
            if k in keywords:
                for n in keywords[k]:
                    if not hasattr(v, n):
                        raise AttributeError(errmsg % (k, f.__name__, v, n))
        spec = inspect.getargspec(f)
        if spec.defaults != None:
            n = len(spec.args) - len(spec.defaults)
            for i,v in enumerate(spec.defaults):
                check(spec.args[n+i], v)
        def __(*args, **kw):
            for i,v in enumerate(args):
                k = spec.args[i]
                check(k, v)
            for k,v in kw.iteritems():
                check(k, v)
            return f(*args, **kw)
        return __
    return _

