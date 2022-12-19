def func(*args,**kwargs):
    def qwer(fu):
        def ins(a,b):
            res = 0
            for i in args:
                res+=i
            return res*fu(a,b)
        return ins
    return qwer

@func(1,2,3,4,a=12,b='qwer')
def kek(a,b):
    return a+b

import itertools as f

word = ['a','b','c']
a = f.accumulate(word)
print( 'a' in a )
