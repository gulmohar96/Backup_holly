class Resources(object):
    def __init__(self, food, water, sleep):
        self.food = food
        self.water = water
        self.sleep = sleep

    def clamp(self):
        result = self.copy()
        result.food = max(0., min(self.food, 1.))
        result.water = max(0., min(self.water, 1.))
        result.sleep = max(0., min(self.sleep, 1.))
        return result

    def copy(self):
        return Resources(self.food, self.water, self.sleep)

    def add(self, res):
        result = self.copy()
        result.food = self.food + res.food
        result.water = self.water + res.water
        result.sleep = self.sleep + res.sleep
        return result

    def mul(self, scalar):
        result = self.copy()
        result.food = self.food * scalar
        result.water = self.water * scalar
        result.sleep = self.sleep * scalar
        return result

    def __str__(self):
        return "({:.2}, {:.2}, {:.2})".format(self.food, self.water, self.sleep)

