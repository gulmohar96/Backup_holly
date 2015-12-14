##_________ NOTES ON OO REPRESENTATION___________##

class Resources:
    def __init__(self, sleep, food, water):
        self.sleep = sleep
        self.food = food
        self.water = water

class Offer:
    def __init__(self, time, resources):
        self.time = time
        self.resources = resources

class Provider:
    def __init__(self, name, time, resources):
        self.name = name
        self.time = time
        self.resources = resources

    def make_offer(self):
        return Offer(self.time, self.resources)

class Actor:
    def __init__(self):
        self.resources = Resources(100, 100, 100)

    @staticmethod
    def update(resources, delta):
        resources.food -= 1 * delta
        resources.water -= 1 * delta
        resources.sleep -= 1 * delta

    def utility(self, offer):
        update(self.resources, offer.time)
        offeredFood = self.resources.food + offer.resources.food
        offeredWater = self.resources.water + offer.resources.water
        offeredSleep = self.resources.sleep + offer.resources.sleep
        return offeredFood * offeredWater * offeredSleep

res = Resources(100, 1, 1, 10)
provider = Provider('tap', res)
provider.make_offer() # res

sort(providers, lambda provider: actor.utility(provider.make_offer()))


#Output format
{
    "house": "house0114",
    "timestamp": "19:30 10/4/16",
    "sensors": [
        "motion_kitchen": "on"
        "motion_bedroom": "on"
    ]
}


microwave = Provider('microwave', 10, Resources(1,1,1))


class ProviderFactory:
    @staticmethod
    def microwave():
        return Provider('microwave', 10, Resources(1,1,1))

    @staticmethod
    def oven():
        return Provider('microwave', 10, Resources(1,1,1))
