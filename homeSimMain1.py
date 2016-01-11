__author__ = 'gulmohar'




## _________ Parameters and Assumptions_________ ##
# Every house will contain a Kitchen, bedroom, living room, bathroom






## _________Random Theory________##

#-----Determine next random occurrence given by LAMBDA----#
#random.expovariate(lmbda) #lmbda will be modelled from the poisson process also 'lambda' is an inbuilt func, hence using lmbda
##_____ Mathematical formula_________##(INSTEAD OF USING random.expovariate)
# import math
# import random
#
# def nextTime(rateParameter):
#     return -math.log(1.0 - random.random()) / rateParameter
##call
##nextTime(Lmda.0)
# Reference: http://preshing.com/20111007/how-to-generate-random-timings-for-a-poisson-process/





##________RecursiveFunc-Home________##
### simulate n number of test homes





##_______________GENERATING RANDOM WALKING PATHS_______________##


##_________Walker1: Elderly_______##
# Specify probability distributions for time spent in the  living, bath, kitchen, bedrooms according to elderly needs
# Poisson Modelling
# Reference: http://preshing.com/20111007/how-to-generate-random-timings-for-a-poisson-process/

# LIVING ROOM
living_1 = random.expovariate(1/10) # change lambda value as per actual mathematical calc later

# BEDROOM
bed_1 = random.expovariate(1/20) # change lambda value as per actual mathematical calc later

# BATHROOM
bath_1 = bed = random.expovariate(1/6) # change lambda value as per actual mathematical calc later


##________Walker2: Unspecified_______##

# LIVING ROOM
living_2 = random.expovariate(1/11) # change lambda value as per actual mathematical calc later

# BEDROOM
bed_2 = random.expovariate(1/30) # change lambda value as per actual mathematical calc later

# BATHROOM
bath_2 = bed = random.expovariate(1/7) # change lambda value as per actual mathematical calc later



##_________Test Home__________##

# house_map = [(1,0),(0,1),(0,2),(2,0),(2,3),(3,2)]

# dictionary for house maps
graph = {"0" : ["1","2"],
          "1":["0"],
          "2":["0","3"],
          "3":["2"]
          }

# Generating list of all edges in the house graph
def generate_edges(graph):
     edges = []
     for node in graph:
         for neighbour in graph[node]:
             edges.append((node,neighbour))
     return edges

print(generate_edges(graph))

# ___________Generating random walker path__________ #


import random

sim_time = 10 # Specifies the number of rooms th walker will visit in the path, should be sped up with a smaller time
              # step for the final simulation

walker_path = []
tot_rooms = len(graph)
for i in range(1,sim_time):
    walker_path = randm.randint(0,tot_rooms)
    walker_path
    walker_path += 1

# Remove irrational paths
# Staying in 1 room ex: walker_path = [1,1,1]
if walker_path =


## __________Finding and tracing Walker path_________##

# Method to find the path from teh start vertex to the end vertex in house map
def find_path(self, start_vertex, end_vertex, path=[]):
        """ find a path from start_vertex to end_vertex
            in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

# Method find_all_paths finds all paths between a start vertex and end vertex

def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths




