# -*- coding: utf-8 -*-
def is_palindrome(n):
    if str(n)[0]==str(n)[-1]:
        return n
output = filter(is_palindrome, range(1, 1000))
print(list(output))
