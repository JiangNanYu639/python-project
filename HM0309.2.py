# TA2 一辆汽车中有4个轮胎，轮胎有属性 (品牌: GoodYear，....，生产日期，价格，使用年限)，通过汽车对象，打印轮胎
# 生产日期在2007年之后的轮胎
import datetime

class Wheel:
    def __init__(self,brand,MFG,price,years):
        self.__brand = brand
        self.__MFG = MFG
        self.__price = price
        self.__years = years

    def show(self):
        print(self.__brand)
        print(self.__MFG)
        print(self.__price)
        print(self.__years)

    def getMFG(self):
        return self.__MFG

class Car:
    __wheels = []
    def __init__(self,wheelsList,color,speed):
        self.__wheels.extend(wheelsList)
        self.__color = color
        self.__speed = speed

    def addWheel(self,wheel):
        if wheel not in self.__wheels:
            self.__wheels.append(wheel)

    def changeWheel(self,old,new):
        if old in self.__wheels:
            self.__wheels.remove(old)
            self.__wheels.append(new)

    def checkMFG(self,date):
        for w in self.__wheels:
            if w.getMFG() >= date:
                w.show()


w1 = Wheel('GoodYear',datetime.date(2010,10,23),123,2)
w2 = Wheel('DL',datetime.date(2000,10,23),120,2)
w3 = Wheel('CA',datetime.date(2005,10,23),223,2)
w4 = Wheel('SY',datetime.date(2008,10,23),323,2)
car = Car([w1,w2,w3,w4],'red',150)

wDate = datetime.date(2007,1,1)
car.checkMFG(wDate)

