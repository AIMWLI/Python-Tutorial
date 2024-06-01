print("欢迎使用账户管理器")
print()

# 数据存储
accounts = {"qq": "qq123456", "gmail": "gmail123456", "deta": "datapoint"}


def show():
    print()
    print("现有账户列表")
    for a in accounts.keys():
        print(a)
    print("请输入要查询的账户,或按q退出")
    return input()


# 主程序
while (True):
    str = show()
    if (str == "q"):
        break
    elif (str in accounts.keys()):
        print(accounts[str])
    elif(str not in accounts.keys()):
        print("不存在此账户")
    else:
        print("unknow error")