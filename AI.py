##__________Initialising Global Timer___________##
# Global time ticks and causes uniform decrease in Food, water,sleep levels

# import numpy as np # Figure out how range would work with float to give a time slice in minutes

# Initial Fuel Levels
food = 100
water = 100
sleep = 100

nap_hours = [] #Stors Forced Nap Hours

# Time steps of the day, also controls the  speed of the simulation
#Time initiation for forced routine maps
day_time = range(1, 8600);  # FIX WITH TIME STEPS IN NUMPY
for global_time in day_time:
    print('current time', global_time)
    food -= 1
    water -= 1
    sleep -= 1

##_________FORCED ROUTINE_________##



##_________Resource Depletion and fuel refilling________##


## ____________KITCHEN___________##
    # Make oven & toaster objects later
    # Make kitchen the method or class
    # oven gives 10 food points looses 60 minutes and causes other resources to go down by 5
    # toaster gives 6 food points and looses 10 minutes, it causes other resources to go down by 3
    # microwave gives 7 food points, looses 5 minutes, causes other resources to go down by 2

    # Happens in 1 time-step
    if food < 80 & (sleep + water) < 40 :
        print('food after condition check',food, 'water',water, 'sleep', sleep)

        toaster = (food + 6) + (water - 3) + (sleep - 3)
        oven = (food + 10) + (water - 5) + (sleep - 5)
        microwave = (food + 7) + (water - 2) + (sleep - 2)

        if oven is max(toaster, oven, microwave):
            print('oven used',oven)
            # Fuel depletion and gain due to oven use
            food += 10
            sleep -= 5
            water -= 5

            # If fuel is more than needed, extra fuel is wasted and we go back to 100% energy level
            if food > 100:
                food = 100

            print('f', food, 'w', water, 's', sleep)
            new_global_time = global_time + 60  # time increment due to oven
            print('new_global_time', new_global_time)
            break  # stop after recharge and resume normal timer

        elif toaster is max(toaster, oven, microwave):
            print('toaster used',toaster)
            # Fuel depletion and gain due to toaster use
            food += 6
            sleep -= 3
            water -= 3

             # If fuel is more than needed, extra fuel is wasted and we go back to 100% energy level
            if food > 100:
                food = 100
            print('f', food, 'w', water, 's', sleep)
            new_global_time = global_time + 10  # time increment due to oven
            print('new_global_time', new_global_time)
            break  # stop after recharge and resume normal timer

        elif microwave is max(toaster, oven, microwave):
            print('microwave used',microwave)
            # Fuel depletion and gain due to toaster use
            food += 7
            sleep -= 2
            water -= 2

             # If fuel is more than needed, extra fuel is wasted and we go back to 100% energy level
            if food > 100:
                food = 100
            print('f', food, 'w', water, 's', sleep)
            new_global_time = global_time + 5  # time increment due to oven
            print('new_global_time', new_global_time)
            break  # stop after recharge and resume normal timer

print('f', food, 'w', water, 's', sleep)
print('current time', new_global_time)
# Global timer resumes after oven debacle with a new value
for global_time in range(new_global_time , 8600):
    print('new timer', global_time)  # overwriting global timer variable cuz we need to duh

##____________BEDROOM____________##
    # Make bed an object later
    # Make bedroom the method or class
    # bed gives 1/6 more sleep per min, -1/480 food per minute and -1/320 water points

    # Happens in 1 time-step and repeats till he is not sleepy
    if sleep < 80 & (water + food) < 40:
        sleep += 1/6
        food -= 1/480
        water -= 1/320
        #NO need for time taken increment since we only go by per minute wastage
        #print('sleep after condition check',sleep, 'water',water, 'food', food)
    elif sleep > 80:
        break

    print('sleep after recharge', sleep, 'food', food, 'water', water)
    print('current time', global_time)

##__________Water needs__________##

    if water < 80 & (food + sleep) < 40:
        sleep -= 1/10
        food -= 1/12
        water -= 5
    elif water > 80:
        break
    print('water after recharge', water, 'food', food, 'sleep', sleep)
    print('current time', global_time)


class Resources(object):
    def __init__(self,food = 100,sleep = 100,water = 100):
        self.sleep = sleep
        self.water = water
        self.food = food

    def food(self):
        food -= 1 #link this depletion to the graphs later
        return food
    def water(self):
        water -= 1
    def sleep(self):
        sleep -= 1

class locations:
    def __init__(self,bedroom,bathroom,livingRoom,kitchen):
        self.bedroom = bedroom
        self.bathroom = bathroom
        self.livingRoom = livingRoom
        self.kitchen = kitchen

    def bedroom(self):






# ##_________ NOTES ON OO REPRESENTATION___________##
#
# class Resources:
#     def __init__(self, sleep, food, water):
#         self.sleep = sleep
#         self.food = food
#         self.water = water
#
# class Offer:
#     def __init__(self, time, resources):
#         self.time = time
#         self.resources = resources
#
# class Provider:
#     def __init__(self, name, time, resources):
#         self.name = name
#         self.resources = resources
#
#     def make_offer(self):
#         return Offer(self.time, self.resources)
#
# class Actor:
#     def __init__(self):
#         self.resources = Resources(100, 100, 100)
#
#     @staticmethod
#     def update(resources, delta):
#         resources.food -= 1 * delta
#         resources.water -= 1 * delta
#         resources.sleep -= 1 * delta
#
#     def utility(self, offer):
#         update(self.resources, offer.time)
#         offeredFood = self.resources.food + offer.resources.food
#         offeredWater = self.resources.water + offer.resources.water
#         offeredSleep = self.resources.sleep + offer.resources.sleep
#         return offeredFood * offeredWater * offeredSleep
#
# res = Resources(100, 1, 1, 10)
# provider = Provider('tap', res)
# provider.make_offer() # res
#
# sort(providers, lambda provider: actor.utility(provider.make_offer()))
#
#
# #Output format
# {
#     "house": "house0114",
#     "timestamp": "19:30 10/4/16",
#     "sensors": [
#         "motion_kitchen": "on"
#         "motion_bedroom": "on"
#     ]
# }
