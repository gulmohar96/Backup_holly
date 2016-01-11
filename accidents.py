import random

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

class Offer(object):
    def __init__(self, provider, time, payoff, location):
        self.provider = provider
        self.time = time
        self.payoff = payoff

    def __str__(self):
        result = str(self.payoff) + " from "
        result += self.provider.name + " over "
        result += str(self.time) + " minutes"
        result += " located at " + self.provider.location 
        return result

class Provider(object):
    def __init__(self, name, time, resources,location):       
        self.name = name
        self.time = time
        self.resources = resources
        self.location = location

    def offer(self):
        return Offer(self, self.time, self.resources, self.location)

    def __str__(self):
        return self.name, self.location

class Interaction(object):
    def __init__(self, provider, time):
        self.provider = provider
        self.time = time

    def update(self, delta_min):
        self.time -= delta_min

    def complete(self):
        return self.time == 0

class Actor(object):
    def __init__(self):
        self.resources = Resources(1.0, 1.0, 1.0)
        #Scaled Resource Depletion
        self.consumption = Resources(1 / 720.0, 1 / 360.0, 1 / 1440.0)
        self.interaction = None

    def utility(self, resources):
        #Desire Graphs
        food_priority = 1 - self.consumption.food ** 0.5
        water_priority = 1 - resources.water ** 2
        sleep_priority = 1- resources.sleep ** 0.1

        # res_avg = (food_priority + water_priority + sleep_priority) / 3.0


        return res_avg

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


class Provider(object):
    def __init__(self, name, time, resources,location):       
        self.name = name
        self.time = time
        self.resources = resources
        self.location = location

    def offer(self):
        return Offer(self, self.time, self.resources, self.location)

    def __str__(self):
        return self.name, self.location

class provider_factory(object):
    def house_providers(self):
        bed = Provider("bed", 480, Resources(-0.25, -0.25, 1.0), "bedroom")
        tap = Provider("tap", 5, Resources(-0.05, 0.15, -0.05), "kitchen")
        food = Provider("food", 30, Resources(0.25, -0.15, -0.1), "kitchen")
        providers = [bed, tap, food]
        return providers

    def accident(self):
        fall = Provider("Bathroom slip", 50, Resources(-0.7, -0.4, -0.5), "bathroom")
        heat_stroke = Provider("Dehydration", 50, Resources(-0.2, -0.9, -0.1), "kitchen")
        accidents = [fall,heat_stroke]
        return accidents


prov_factory_class = provider_factory()

accident_list = prov_factory_class.accident()

accident_choice = random.choice(accident_list)

print(accident_choice)