# 大乐透游戏，给你的6位数，中奖码是958 (9 5 8可以在6位数中任意位置，都存在) ，如何判断自己中奖？

n = input('Pls type your number: ')
a = '9'
b = '5'
c = '8'

if n.isdigit():
    if n.find(a) != -1 and n.find(b) != -1 and n.find(c) != -1:
        print('You win!')
    else:
        print('Sorry.')
else:
    print('Not a valid number.')






