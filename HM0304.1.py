# TA1 A(4,5) B(5,6) C(7,10) 计算哪条边最长，对应的端点信息；计算哪条边最短，对应的端点信息？

# AC ['A',4,5,'C',5,6,1.3]
# CB
# BA

pointA = ['A',4,5]
pointB = ['B',5,6]
pointC = ['C',7,10]

def createElements(x,y):
    length = ((x[1]-y[1])**2+(x[2]-y[2])**2)**0.5
    element = [length]
    element.append(x)
    element.append(y)
    return element

li = [createElements(pointA,pointB),createElements(pointB,pointC),createElements(pointC,pointA)]

sorted(li,key=lambda x:x[0])

longest = li[2]
shortest = li[0]

print('The longest is %.2f, points are %c and %c.'%(longest[0],longest[1][0],longest[2][0]))
print('The shortest is %.2f,points are %c and %c.'%(shortest[0],shortest[1][0],shortest[2][0]))





