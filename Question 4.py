class Critter:

    ATTACK_POUNCE = 0
    ATTACK_ROAR = 1
    ATTACK_SCRATCH = 2
    ATTACK_FORFEIT = 3
    DIRECTION_NORTH = 0
    DIRECTION_SOUTH = 1
    DIRECTION_EAST = 2
    DIRECTION_WEST = 3
    DIRECTION_CENTER = 4



    def eat(self):
        return False

    def fight(self, opponent):
        return Critter.ATTACK_FORFEIT

    def colour(self):
        return "grey"

    def move(self):
        return Critter.DIRECTION_CENTER

    def __str__(self):
        return "I am a Critter."

class Quokka(Critter):

    def __init__(self, ATTACK_POUNCE, DIRECTION_NORTH, DIRECTION_EAST, DIRECTION_WEST, DIRECTION_CENTER, _eaten, _steps, _direction, _slow_counter, _slow_on, i):
        Critter.__init__(ATTACK_POUNCE, DIRECTION_NORTH, DIRECTION_EAST, DIRECTION_WEST, DIRECTION_CENTER)
        self.___eaten = _eaten
        self.___steps = _steps
        self.___direction = _direction
        self.___slow_counter = _slow_counter
        self.___slow_on = _slow_on
        self.__i = i

    def __str__(self):
        if self.___steps == 0:
            return "I am a Critter. Type: Quokka, eaten: %d, steps: %d, current direction: %d"%(self.___eaten, self.___steps, self.___direction)
        else:
            return "I am a Critter. Type: Quokka, eaten: %d, steps: %d, current direction: %d"%(self.___eaten, self.___steps, Quokka.move(self))

    def eat(self):
        self.___eaten += 1
        self.___slow_counter = 3
        self.___slow_on = True
        return True

    def fight(self):
        return Critter.ATTACK_POUNCE

    def move(self):
        li = [Critter.DIRECTION_EAST, Critter.DIRECTION_EAST, Critter.DIRECTION_EAST, Critter.DIRECTION_EAST, Critter.DIRECTION_NORTH, Critter.DIRECTION_WEST, Critter.DIRECTION_WEST, Critter.DIRECTION_WEST, Critter.DIRECTION_WEST, Critter.DIRECTION_NORTH]
        if self.___slow_on == False:
            if self.__i < 10:
                self.___steps += 1
                self.__i += 1
                return li[self.__i - 1]
            else:
                self.__i = 0
                self.___steps += 1
                self.__i += 1
                return li[self.__i - 1]
        else:
            if self.___slow_counter == 3:
                self.___slow_counter -= 1
                return Critter.DIRECTION_CENTER
            elif self.___slow_counter == 2:
                self.___slow_counter -= 1
                if self.__i < 10:
                    self.___steps += 1
                    self.__i += 1
                    return li[self.__i - 1]
                else:
                    self.__i = 0
                    self.___steps += 1
                    self.__i += 1
                    return li[self.__i - 1]
            elif self.___slow_counter == 1:
                self.___slow_counter -= 1
                return Critter.DIRECTION_CENTER
            elif self.___slow_counter == 0:
                self.___slow_counter -= 1
                if self.__i < 10:
                    self.___steps += 1
                    self.__i += 1
                    return li[self.__i - 1]
                else:
                    self.__i = 0
                    self.___steps += 1
                    self.__i += 1
                    return li[self.__i - 1]
            elif self.___slow_counter == -1:
                self.___slow_counter = 0
                self.___slow_on = False
                return Critter.DIRECTION_CENTER

q = Quokka(0, 0, 2, 3, 4, 0, 0, Critter.DIRECTION_EAST, 0, False, 0)
print(q)
print("output of fight: ", q.fight())
print("now move the quokka")
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print("now eat")
q.eat()
print(q.move())
print(q.move())
print("now eat again")
q.eat()
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q.move())
print(q)









