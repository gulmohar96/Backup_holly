#LOCATION TRACKING ADDED TO OLD SIMULATION CORE

#from __future__ import division
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
    #def __init__(self, name, time, resources):        
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
        self.consumption = Resources(1 / 720.0, 1 / 360.0, 1 / 1440.0)
        self.interaction = None

    def utility(self, resources):
        res_avg = (resources.food + resources.water + resources.sleep) / 3.0
        return res_avg

    def actor_utility(self):

        return self.utility(self.resources)

    def offer_utility(self, offer):
        new = self.resources.add(offer.payoff).clamp()
        return self.utility(new)

    def normal_life(self):
        return("Living my everyday life getting by and drifting away into oblivion")

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

##ROOM CODES
# bedroom = 0, kitchen = 1, bathroom = 2 
# bed = Provider("bed", 480, Resources(-0.25, -0.25, 1.0),0)
# tap = Provider("tap", 5, Resources(-0.05, 0.15, -0.05),1)
# food = Provider("food", 30, Resources(0.25, -0.15, -0.1),1)
# accident = Provider("Accident", 50, Resources(-0.7, -0.4, -0.5),2)

bed = Provider("bed", 480, Resources(-0.25, -0.25, 1.0), "bedroom")
tap = Provider("tap", 5, Resources(-0.05, 0.15, -0.05), "kitchen")
food = Provider("food", 30, Resources(0.25, -0.15, -0.1), "kitchen")
accident = Provider("Accident", 50, Resources(-0.7, -0.4, -0.5), "bathroom")

providers = [ bed, tap, food] #,accident]
offers = list((map(lambda x: x.offer(), providers)))

## _______________MAIN SIMULATION_________________ ##
import random

#Introducing Accidents 
acc = []
for i in range(0,10):
    prob = random.random() 
    acc.append(prob)
avg_acc = sum(acc)/10
accident_time = random.choice(range(0,600)) 

print("Starting simulation...")
for global_time in range(0,1440,1):
    if avg_acc > 0.5 and global_time == accident_time:
        print('Accident happened at', global_time,'minutes') #Add the accident provider to resources 
        break

    if actor.interacting_with() == None:

        if actor.actor_utility() < 0.5:
            print ("\nThe time is {}".format(global_time))
            print ("\tActor resources: {}".format(str(actor.resources)))

            print ("\tOffers:")
            for x in offers:
                print ("\t\t", x, "(utility: {})".format(actor.offer_utility(x)))
            # print(offers)    
            winning_offer = sorted(offers, key= lambda offer: actor.offer_utility(offer))[0]

            print ("\tActor chooses: {}".format(winning_offer))
            actor.set_interaction(winning_offer)
        elif actor.actor_utility() > 0.8:
                print('Living my everyday life at', global_time, 'minutes')            
    actor.update(1)

