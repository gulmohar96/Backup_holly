from __future__ import division

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
    def __init__(self, provider, time, payoff):
        self.provider = provider
        self.time = time
        self.payoff = payoff

    def __str__(self):
        result = str(self.payoff) + " from "
        result += self.provider.name + " over "
        result += str(self.time) + " minutes"
        return result

class Provider(object):
    def __init__(self, name, time, resources):
        self.name = name
        self.time = time
        self.resources = resources

    def offer(self):
        return Offer(self, self.time, self.resources)

    def __str__(self):
        return self.name

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
        self.resources = Resources(1.0, 1.0, 0.0)
        self.consumption = Resources(1 / 720.0, 1 / 360.0, 1 / 1440.0)
        self.interaction = None

    def utility(self, resources):
        return (resources.food + resources.water + resources.sleep) / 3.0

    def actor_utility(self):
        return self.utility(self.resources)

    def offer_utility(self, offer):
        new = self.resources.add(offer.payoff).clamp()
        return self.utility(new)

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
bed = Provider("bed", 480, Resources(-0.25, -0.25, 1.0))
tap = Provider("tap", 5, Resources(-0.05, 0.15, -0.05))
food = Provider("food", 30, Resources(0.25, -0.15, -0.1))

providers = [ bed, tap, food ]
offers = map(lambda x: x.offer(), providers)

print("Starting simulation...")
for i in range(0,600,1):
    
    if actor.interacting_with() == None:

        if actor.actor_utility() < 0.8:
            print("\nThe time is {}".format(i))
            print ("\tActor resources: {}".format(str(actor.resources)))

            print ("\tOffers:")
            for x in offers:
                print ("\t\t", x, "(utility: {})".format(actor.offer_utility(x)))
            winning_offer = sorted(offers, key= lambda x: -actor.offer_utility(x))[0]
            print ("\tActor chooses: {}".format(winning_offer))
            actor.set_interaction(winning_offer)

    actor.update(1)
