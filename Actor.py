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
