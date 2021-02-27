# 大乐透游戏，给你的6位数，中奖码是958 (9 5 8可以在6位数中任意位置，都存在) ，如何判断自己中奖？

num = input('Pls type your number: ')

num = int(num)
num1 = num
num2 = num
cnt = 0

while num != 0:
    remain = num % 10
    if remain == 9:
        cnt += 1
        break
    else:
        num //= 10

while num1 != 0:
    remain1 = num1 % 10
    if remain1 == 5:
        cnt += 1
        break
    else:
        num1 //= 10

while num2 != 0:
    remain2 = num2 % 10
    if remain2 == 8:
        cnt += 1
        break
    else:
        num2 //= 10

if cnt == 3:
    print('You win!')
else:
    print('Sorry.')


