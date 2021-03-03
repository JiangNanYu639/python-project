# TA s = 'give my idea and my work desc, my friend',
# 要求:以函数形式声明，将第二个'my'替换成'your'，并打印

def replaceN(string,old,new,N):
    cnt = 0

    index = string.find(old)
    while index != -1:
        cnt += 1
        if cnt == N:
            front = string[:index]
            end = string[index+len(old):]
            return front + new + end
        index += len(old)
        index = string.find(old,index,len(string))

    return string

str = 'give my idea and my work desc, my friend'

ret = replaceN(str,'my','your',2)
print(ret)





