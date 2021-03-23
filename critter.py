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

