from functools import update_wrapper
import time

def trace(func, indent_step=3):
    def wrapped(*args, **kwargs):
        wrapped.level += indent_step
        print
        indent = '|%*s' % (wrapped.level, ' ')
        params = ', '.join([repr(x) for x in args]+['%s=%s' % (k, repr(kwargs[k])) for k in kwargs])
        print '%s%s (%s)' % (indent, func.__name__, params),
        rv = func(*args, **kwargs)
        print '= %s\n%s' % (rv,indent),
        wrapped.level -= indent_step
        return rv
    wrapped.level = 0
    return wrapped

def timestr(t):
    return ( ("%i min %.3f s" % divmod(t, 60)) if t > 60
            else  (("%.3f s" % t) if t > 1
                   else ("%.3f ms" % (t * 1000)) if t > 0.001 else ("%i us" % (t*10**6))
                   )
            )

def timing(func):
    def wrapper(*arg, **kwargs):
        t1 = time.clock()
        e = ''
        try:
            res = func(*arg, **kwargs)
        except Exception as e:
            e = e 
        t2 = time.clock()
        print('\n%s took %s' % (func.__name__, timestr(t2-t1)))
        if e:
            raise
        return res

    return update_wrapper(wrapper, func)

class Memoize(object):
	def __init__ (self, f):
		self.f = f
		self.__name__ = f.__name__
		self.mem = {}
	def __call__ (self, *args, **kwargs):
		if (args, str(kwargs)) in self.mem:
			return self.mem[args, str(kwargs)]
		else:
			tmp = self.f(*args, **kwargs)
			self.mem[args, str(kwargs)] = tmp
			return tmp

@trace
def comb(s, n):
    return [s[:1]+x for x in comb(s[1:], n-1)]+comb(s[1:], n) if len(s) > n > 0 else [s] if len(s) == n else [[]]

@trace
def perm(s):
    return [s[i:i+1]+x for i in range(len(s)) for x in perm(s[:i]+s[i+1:])] if len(s) > 1 else [s]

@trace
def fib(n):
    return fib(n-1)+fib(n-2) if n > 1 else 1

if __name__ == '__main__':
    perm(range(1, 4))
    comb(range(4), 3)
    fib(5)