line="芝麻开门"
answer=input("请说出密码口令\n")
while True:
    if answer != line:
        answer=input("密码错误,请说出密码口令\n")
    elif answer == line:
        break
print("密码已通过")
