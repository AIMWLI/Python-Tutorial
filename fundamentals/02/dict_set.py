'''
基本数据类型
整数类型
浮点数类型
布尔类型
字符串类型
空类型
'''


'''
this is a multiple
'''
dict = {}
dict["one"] = "1 - first"
dict[2] = "2 - first"
tinydict = {"name":'runoob','code':1,'site':'www.runoob.com'}
print(dict['one'])
print(dict[2])
print(dict)
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

#! /usr/bin/python3
student = {"Tom","jim","mary","Tom","Jack","Rose"}
print(student)
if "Jack" in student:
    print("Jack is in set ")
else:
    print("jack isnot in set")

# set可以进行集合运算
a = set("abcdefg")
b= set("abcefg")
# a 和 b的差集
print(a-b)
# a和b的并集
print(a | b)
# a和b的交集
print(a & b)
# a和b中不同时存在的元素
print(a ^ b)

# touple
#! /usr/bin/python3
tup = ('abcd' ,786, 2.23,'runoob',70.2)
print()
tinytup = ('a',2)
print(tup)
print(tup[2:])
print(tinytup * 2)
print(tup + tinytup)


