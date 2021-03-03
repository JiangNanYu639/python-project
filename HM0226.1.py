# 敲3游戏，打印1-i内，非3的倍数，数字中不包含3

i = input('Pls type an integer greater than 1: ')
i = int(i)

for num in range(1,i + 1):
    if num % 3 != 0:
        containsThree = False
        n = num
        while num != 0:
            remain = num % 10
            if remain == 3:
                containsThree = True
                break
            num //= 10
        if not containsThree:
            print(n,end=' ')
