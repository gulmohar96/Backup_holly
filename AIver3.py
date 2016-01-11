## _____________OOP Representation____________ ##
class Resources(object):
    def __init__(self,food = 100,sleep = 100,water = 100):
        self.sleep = sleep
        self.water = water
        self.food = food

    def copy(self):
        return Resources(self.food, self.sleep, self.water)

## _____IGNORE THIS AS OF NOW______##
class Locations(object):

    ## Problems with location recording:
    # dont know how sensors are set up
    # Especially where a single room satisfies multiple needs such as the kitchen supplies food and water
    # Also how to have a global empty data structure like location = [] be a global empty variable to store
    # different locations through different methods under a class
    # How to link to things that are kept in different rooms

    # 0 - bedroom , 1- bathroom, 2- Living Room , 3- Kitchen
    location = []
    def __init__(self,bedroom,bathroom,livingRoom,kitchen,location):
        self.bedroom = bedroom
        self.bathroom = bathroom
        self.livingRoom = livingRoom
        self.kitchen = kitchen
        self.location = location

    def bedroom(self):
        if sleep #sensor activated
            location.append(0)
    
    def bathroom(self):
        if water #sensor activated
            location.append(1)
    
    def livingRoom(self):
        if sleep #later recreational stuff/entertainment etc activated 
            location.append(2)

    def kitchen(self):
        if water #sensor activated
            location.append(3)
            elif food #sensor activated
                location.append(3)


class Provider(object):
    # The provider provides different offers from all the possible resources in the house
    def __init__(self,name,time_consumed,resources):
        self.name = name
        self.time_consumed = time_consumed
        self.resources = resources # Gives the status of teh resources at after the usage of a particular object
                                   # that is making a offer

    def make_offer(self):
        return(self.name, self.time_consumed, self.resources) # SEE WHAAATTTT

class Offer(object):
    # Intermediate...Just represents the offers from the provider for easy code usage
    def __init__(self, name, time_consumed, resources):
        self.name = name
        self.time_consumed  = time_consumed
        self.resources = resources
        return(self.name, self.time_consumed, self.resources)

## _____Objects in the house______##
    # Put this in class provider factory later
#FOOD
microwave = Provider('Microwave', 10, Resources(5, -0.009 , -0.0.4) ) #confirm resource depletion design
# 10 minutes consumed, 5 food point provided causing 0.1 and 0.12 depletion in water and food over a simulated time
oven = Provider('Oven', 30, Resources(10, -0.003 , -0.012) )
toaster = Provider('toaster', 8, Resources(7, -0.001 , -0.08) )

#WATER
kitchen_tap = Provider('Kitchen Tap', 2, Resources(6, -0.005,-0.02))
bathroom_tap = Provider('Kitchen Tap', 3, Resources(4, -0.003,-0.04))

#SLEEP
bed = Provider('Bed', 2, Resources(6, -0.005,-0.02))
couch = Provider('Kitchen Tap', 2, Resources(6, -0.005,-0.02))

class Actor(object):
    def __init__(self):
        self.resources = Resources(100, 100, 100) # internal level
        self.interacting_provider = None

    @staticmethod
    def update(resources, delta):
        resources.food -= 1 * delta
        resources.water -= 1 * delta
        resources.sleep -= 1 * delta

    def update(self, delta):
        if  self.interacting_provider != None:
            self.interacting_provider.time_left -= delta
            if self.interacting_provider.time_left == 0:
                self.interacting_provider = None

    def utility(self, offer):
        newResources = self.resources.copy()
        update(newResources, offer.time_consumed)
        offeredFood = newResources.food + offer.resources.food
        offeredWater = newResources.water + offer.resources.water
        offeredSleep = newResources.sleep + offer.resources.sleep
        return offeredFood * offeredWater * offeredSleep

sort(providers, lambda provider: actor.utility(provider.make_offer()))




