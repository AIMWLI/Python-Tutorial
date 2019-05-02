#! /usr/bin/python3



counter = 100
miles = 1000.0
name = 'bob'
print(counter)
print(miles)
print(name)

a,b,c,d= 1,3.14,"many var",4+3j
print(a,b,"\n" + c)
print(type(a),type(b),type(c),type(d))

soul = "sb"
isnum = isinstance(soul, int)
isStr = isinstance(soul, str)
if isnum:
    print("this is num")
elif isStr:
    print("this is a string value")

# 运算逻辑
print(2/4)
print(2//4)
print(17%3)
print(2 ** 5)

t= [1,2,3,4,5,]
subT = t[1:3]
print(subT)
print(t[:4])

list= [ "abcd", 783, 3.14, "pandora",True]
print(list[0:4])
list2 = [True,"apendeList",1234]
print((list + list2)* 2)

list[2:5] = ["re","pla","ce"]
print(list)
list[0:1] = []
print(list)

letters = ['c','h','e','c','k']

letters_ = letters[1:4:2]
print(letters_)


x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('--------')
# print in one line
print(x, end=" ")
print(y, end="")

import sys
print('命令行参数')
for i in sys.argv:
    print(i)
print("\n python path is ",sys.path)

#位置参数
str="{0} love {1} {2}".format("i","python","and Java")
print(str)
#关键字参数
str2="{a} love {b} {c}".format(a="i",b="python",c="and Java")
print(str2)

x = "demo"; sys.stdout.write(x + '\n')
a = x.__sizeof__()
print(a)
