# -*- coding: utf-8 -*-
#列表生成器
L=list(range(1,11))
L2=list(range(10))
print(L)
print(L2)
#切片
print(L[0:3])
print(L[1:5])
print(L[-2:])
print(L[-3:-1])
print(L[::2])
#迭代
for x in L:
    print(x)
for word in 'ABCDE':
    print(word)
#判断是否为课迭代对象
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
