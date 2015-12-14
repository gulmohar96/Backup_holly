
##_______MAIN SIMULATION_______##
# Initiates the simulation, has teh global timer that sets the simulation time
# Has control over all simulation aspects and links all functions & classes

#Importing all linked classes
from resources import Resources

from Provider import Provider
from Offer import Offer
from ProviderFactory import ProviderFactory
from Locations import Locations
from Actor import Actor

res = Resources(1,1,1)

delta = range(1,14) #works as simulation time for now
for global_time in delta: #Refered to in actor class too
    print(Resources.food)


    print('sim start time in seconds', global_time)


