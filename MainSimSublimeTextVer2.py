
##_______MAIN SIMULATION_______##
# Initiates the simulation, has the global timer that sets the simulation time
# Has control over all simulation aspects and links all functions & classes

#Importing all linked classes
from resources import Resources
from Provider import Provider
from Offer import Offer
from ProviderFactory import ProviderFactory
from Locations import Locations
from Actor import Actor
#from SystemNoise import SystemNoise 
from NormalLife import NormalLife
from NeedGraphs import NeedGraphs
import random

## _____________ACCIDENT______________ ##
# Probablity control for accidents
## This controls what the odds are of the accident happening
## Probability ranges from 0 to 1 
acc = []
for i in range(0,10):
	prob = random.random() 
    acc.append(prob)
avg_acc = sum(acc)/10

## _____MORNING_____ ##
# Decides the start time of the simulation 
# Actor typically wakes up anywhere between 6am (360th min) to 9am(540th min) which is randomly chosen
awake = random.choice(range(360,540))

## ______NIGHT_____ ##
# Decides when the actor goes to sleep 
# Actor typically sleeps between 7pm (1140th min)to 10pm (1320th min) 
forced_night_sleep = random.choice(range(1140,1320)) 

## ______Forced Sleep cycle______ ##
sleep_cycle = len(range(0,awake))+len(range(forced_night_sleep,1440))

#Random accidents while sleeping 
accident_time = random.choice(range(0,sleep_cycle))

for sleep_time in range(0, sleep_cycle):
    Resources.food -= 1
    Resources.water -= 1     
    Resources.sleep -= 1

	#Sleep Accident
	if avg_acc > 0.5 & sleep_time = accident_time:
		    ProviderFactory.accident()


##_________DAY TIME ROUTINE_________##
delta = range(awake,forced_night_sleep) #works as simulation time for now
for global_time in delta: #Refered to in actor class too
    NormalLife.life() #executes normal life till resource level dips below a certain level
    
    # Resource depletion with every tick 
    # As of now, resource delpletion is uniform 
    Resources.food -= 1
    Resources.water -= 1     
    Resources.sleep -= 1
    #Essentiallly things will start advertising themselves at 20,20,20 resource level 


    #Working on cummulative resources atm, need to figure out scaling/needs later 
    res_total = Resources.food + Resources.water + Resources.sleep
    #this condition should only come into play for teh very forst time the simulation is run 
    if res_total < 80:

    	# Mapping the resource level to graph functions 
    	graph_cursor = Resources.food/100 #all resources are equal at this instant 
    	# graph map gives the x value on the graph
    	# the value was scaled by a factor of 100 as the resources are from a 0-100 scae and the
    	# graph is from 0 to 1 scale 

    	need = max(water_need, food_need,sleep_need)
    	# Here water_need,food_need,sleep_need are the corresponding Y coordinates to graph_cursor
    	if need = water_need:
    		# Sort through list of adverstisors for food in the house to get the max water
    		sort(Provider, lambda provider: Actor.utility(provider.make_offer()))

    	elif need = food_need:


    	elif need = sleep_need: 



	# If resources drop below 0 or get to a negative, get them to zero.
	# Make this and the global time test a method   
    if Resources.food < 0:
    	Resources.food = 0

    if Resources.water < 0:
    	Resources.water = 0

    if Resources.sleep < 0:
    	Resources.sleep =0

    # Time can't be nagative (Add this after time step changes in classes)
    if global_time < 0 
    	global_time = 0

## _______Sleep time________ ##
for night_time = range()
