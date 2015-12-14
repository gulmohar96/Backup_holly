
class Resources(object):
    def __init__(self,food = 100,sleep = 100,water = 100):
        self.sleep = sleep
        self.water = water
        self.food = food

    def copy(self):
        return Resources(self.food, self.sleep, self.water)

