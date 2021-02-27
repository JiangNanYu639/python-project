# 敲3游戏，打印1-100内，非3的倍数，数字中不包含3

num = 1
while num < 101:
    remain = num % 10
    quotient = num // 10
    if remain != 3 and quotient != 3 and num%3 != 0:
        print(num,end=' ')
        num += 1
    else:
        num += 1
