class User:
    __user_name = "abc"

    def __init__(self):
        print(User.__user_name)
        pass


user = User()
print(user._User__user_name)  # 私有属性, 可以通过"实例名.类名__xxx"方式访问
print(user._user_name)  # 私有属性不能通过实例名访问, 出错
