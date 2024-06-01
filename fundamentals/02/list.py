#! /usr/bin/python3

import random
from cmath import log10
from math import modf

from numpy.core.defchararray import capitalize


def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output


if __name__ == "__main__":
    input = "some one like you"
    rw = reverseWords(input)
    print(rw)

i = max(1, 2, 3, 4, 5, 6, 7)
print(i)
log_ = log10(2)
print(log_)
print(min(1, 2, 3, 4))

modf1 = modf(4.6)
print(modf1)
f = pow(2, 3)
print(f)
round1 = round(3.14, 1)
print(round1)

choice = random.choice(range(10))
print(choice)

uniform = random.uniform(2, 10)
print(uniform)

print("hello world")
var1 = "hello world"
var2 = 'runoob'
print("var1: ---", var1[2:6])
print('h' in var1)
print('\a')

print("我叫 %s 今年 %d 岁!" % ('小明', 10))
a = 'songjin'
n = capitalize(a)
print(n)

b = "  abcdefghabbbb"
print(b * 2)

for x in [1, 2, 3]:
    print(x, end="")
    print("")
L = ["google", "runoob", 'taobao']
print(L[2])

squares = [1, 4, 9, 16]
squares += [2, 3, 5, 6, 7, 8]
# print(sorted(squares))
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x[0][0])
