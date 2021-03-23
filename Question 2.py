class Time():
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, h):
        if h >= 0 and h <= 23:
            self.__hour = h
        else:
            raise ValueError('hour must be in 0-23')

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, m):
        if m >= 0 and m <= 59:
            self.__minutes = m
        else:
            raise ValueError('minutes must be in 0-59')

    def __str__(self):
        t = str(self.__hour) + ':' + str(self.__minutes)
        return t

    def __lt__(self, other):
        if self.__hour < other.__hour:
            return True
        elif self.__hour == other.__hour:
            if self.__minutes < other.__minutes:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.__hour == other.__hour and self.__minutes == other.__minutes:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__hour > other.__hour:
            return True
        elif self.__hour == other.__hour:
            if self.__minutes > other.__minutes:
                return True
            else:
                return False
        else:
            return False

try:
    t1 = Time(11, 50)
    t2 = Time(23, 50)
    print(t1.hour)
    print(t1.minutes)
    print(t1)
    print(t2)
    if t2 < t1:
        print('t2 is before t1')
    elif t2 == t1:
        print('t2 is the same as t1')
    else:
        print('t2 is after t1')

except ValueError as ret:
    print(ret)






