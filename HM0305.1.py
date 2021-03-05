# TA
# list1 = [2,2,3,4,5,5,5]
# list2 = [6,3,6,3,6]
# 判断2个list中，出现频率最高的数字，个数是否相同？

def getTheHighestFreq(li):
    if isinstance(li,list):
        Dict = {}
        for x in li:
            if x in Dict:
                Dict[x] += 1
            else:
                Dict[x] = 1

        a = sorted(Dict.items(),key=lambda x:x[1],reverse=True)
        return a[0][1]

def compareEquality(l1,l2):
    if isinstance(l1,list) and isinstance(l2,list):
        if getTheHighestFreq(l1) == getTheHighestFreq(l2):
            return True

    return False

list1 = [2,2,3,4,5,5,5]
list2 = [6,3,6,3,6,6]

print(compareEquality(list1,list2))