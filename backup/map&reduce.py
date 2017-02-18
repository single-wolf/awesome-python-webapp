# -*- coding: utf-8 -*-
#高阶函数map
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
#得到的r为Iterator
print(list(r))


def normalize(name):
    return name[:1].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#高阶函数reduce
from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


#综合测试

m=input('请输入字符串形式的数字：')
def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))
    num=len(s)-s.rfind('.')-1
    s=s.replace('.','')
    return str2int(s)/(10**num)
print('str2float('+m+')=',str2float(m))