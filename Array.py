arr = [1,2,3,"四","五",[6,7,8]]
for i in arr:
    print(i)
print('-----------------')
arrName = ['张飞' ,'关羽','刘备']
print(len(arrName))
arrName.append('子龙')
arrName.extend(['刘备','项羽'])
arrName.insert(0,'燕人')
print(len(arrName))
for j in arrName:
    print(j)

print('-----分割线-------')
arrChange = ['项羽','燕人']
# 把项羽和燕人对调

temp = arrChange[0]
arrChange[0]=arrChange[1]
arrChange[1] = temp
# print("对调后的列表为"+ list(arrChange))
for c in arrChange:
    print(c)

member= ['a','b','c','d','e']
member.remove('b')
print(member)
# del member [1]
print(member)
#  返回弹出值 (删除)
# print(member.pop())
# print(member.pop(1))
ele = member.pop()
ele = 'z'
member.append(ele)
print(member)

#列表分片  左闭右开 并影响原列表
print(member[1:3])
# 变形
# member[1:] 从第一个元素到最会一个
# member[:3] 从第0个元素到第3个元素(0.1,2) ,不包含第3个元素
# member[:] 实现列表复制  例:  member2 = member[:]

testList = [1,8,6,4,5,3,5,7,9,9,9,1,1]

print(testList.count(9))
testList.sort()
print(testList)
testList.sort(reverse=True)
print(testList)


