# TA1 编写递归函数，实现斐波那契数列计算
# F(1)=1, F(2)=1, F(n)=F(n - 1)+F(n - 2) (n >= 3, n属于正整数集)

# n! = n*(n-1)*(n-2)*......*2*1

# n! = n*(n-1)!
# 5! = 5*4!
# 4! = 4*3!
# 3! = 3*2!
# 2! = 2*1!

def F(n):
    if n == 1 or n == 2:
        return 1
    return F(n - 1) + F(n - 2)

num = input('Pls type your number: ')

if num.isdigit():
    num = int(num)
    if num > 0:
        ret = F(num)
        print('The result is %d.'%(ret))
    else:
        print('Number must be larger than 0.')
else:
    print('Sorry not a valid number.')
