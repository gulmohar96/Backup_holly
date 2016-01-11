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


class Actor(object):
    def __init__(self):
        self.resources = Resources(1.0, 1.0, 1.0)
        #Scaled resource depletion
        self.consumption = Resources(1 / 720.0, 1 / 360.0, 1 / 1440.0)
        self.interaction = None

    def utility(self, resources):
        #NEED GRAPHS
        food_priority = 1 - resources.food ** 0.5
        water_priority = 1 - resources.water ** 2
        sleep_priority = 1- resources.sleep ** 0.1
        #self.priority = Resources(food_priority,water_priority,sleep_priority)        
        res_avg = (food_priority + water_priority + sleep_priority) / 3.0
        #return self.utility(self.priority)
        #res_avg = (resources.food + resources.water + resources.sleep) / 3.0
        b = print('food:',food_priority,"water",water_priority,"sleep",sleep_priority)
        #return res_avg
        return b

    def actor_utility(self):
        return self.utility(self.resources)

    def offer_utility(self, offer):
        new = self.resources.add(offer.payoff).clamp()
        return self.utility(new)

    def normal_life(self):
        print("Living my everyday life getting by and drifting away into oblivion")
        return self

    def set_interaction(self, offer):
        if self.interaction != None:
            print ("Actor already has an interaction")
        else:
            self.resources = self.resources.add(offer.payoff).clamp()
            self.interaction = Interaction(offer.provider, offer.time)

    def interacting_with(self):
        if self.interaction != None:
            return self.interaction.provider
        else:
            return None

    def update(self, delta_min):
        if self.interaction != None:
            self.interaction.update(delta_min)
            if self.interaction.complete():
                self.interaction = None
        else:
            total_consumption = self.consumption.mul(-delta_min)
            self.resources = self.resources.add(total_consumption).clamp()

actor = Actor()
actor.utility()









