a,b,c = 0,1,1
n = int(input("请输出一个正整数"))
temp = 0
while c <= n:
    temp += b
    if c == n:
        print(b)
    a, b=b , a+b
    c += 1
print(temp)

n = int(input())
a, b = 0, 1
cn = 1
temp = 0
while cn <= n:
    temp += b
    # print(b,end=",")
    if cn == n:
        print(b)
    a, b = b, a+b
    cn += 1
print()
print("和为%d"% temp)