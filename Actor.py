<<<<<<< HEAD
class Actor(object):
    def __init__(self):
        self.resources = Resources(1.0, 1.0, 1.0)
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
=======
from Resources import Resources
from Provider import Provider
from Offer import Offer

class Actor(object):
    def __init__(self):
        self.resources = Resources(100, 100, 100) # internal level of resources in the actor initially
        self.interacting_provider = None

    @staticmethod
    #Delta time step is the current nth minute(or second) of teh simulation
    def update(resources, delta):
        resources.food -= 1 * delta
        resources.water -= 1 * delta
        resources.sleep -= 1 * delta

    def update(self, delta):
        #interactng_provider will be defined later to make the actor interact with the objects in the house
        #Interaction is dependant on time and will continue for a certain time after which the actor takes up next task
        if  self.interacting_provider != None:
            self.interacting_provider.time_left -= delta
            if self.interacting_provider.time_left == 0:
                self.interacting_provider = None

    def utility(self, Offer): #shouldn't this import from offer class?
        newResources = self.resources.copy()
        update(newResources, Offer.time_consumed)
        offeredFood = newResources.food + Offer.resources.food
        offeredWater = newResources.water + Offer.resources.water
        offeredSleep = newResources.sleep + Offer.resources.sleep
        return offeredFood * offeredWater * offeredSleep

   ## sort(Provider, lambda provider: Actor.utility(provider.make_offer()))
>>>>>>> 33ee28c0ac6757c0d1d2939c7461e5bcf4a43697
