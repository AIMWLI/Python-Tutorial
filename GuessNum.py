# 1-10 猜数字游戏
import random

num = random.randint(1,10)
print("--------")
print(num)
print("--------")
temp = input("请输入1-10之间一个数字\n")
guess = 0
while guess != num:
    temp = input("猜错了,请重新输入\n")
    guess = int(temp)
    if guess > num:
        print("数字太大了\n")
    else:
        if guess < num:
            print("数字太小了\n")
if guess == num:
    print("恭喜你猜中了")
    print("游戏结束")
