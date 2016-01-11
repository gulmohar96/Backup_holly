<<<<<<< HEAD
# # NEED PRIORITY GRAPHS 
# import numpy as np
# import matplotlib.pyplot as plt
# # Resource functions 
# x = np.arange(0.0, 1.0, 0.01)
# food_curve = (1 - x**(0.5))
# water_curve = (1 - x**(2))
# sleep_curve = (1 - x**(0.1)) 

graph_cursor = 0.90

# # Plotting teh functions
# #f = plt.plot(x, food_curve)
# #w = plt.plot(x, water_curve)
# #s = plt.plot(x, sleep_curve)
# #plt.show()

# # Graph Cursor is the x value from the main code 
# # Here we find the Y value from the graph corressponding to the x value and 
# # teh main code finds which ou the listed resources has teh aximum utility at that
# # instannt. Thus which resource is to preferenced is decided 


# Y data for respurces using need graphs
food_need = 1 - graph_cursor**0.5
water_need = 1 - graph_cursor**2
sleep_need= 1 - graph_cursor**0.1
need = max(water_need, food_need,sleep_need)

print(food_need, water_need, sleep_need)
print('max need',need)




=======
# NEED PRIORITY GRAPHS 

import matplotlib

# Resource functions 
food_curve = 1 - x^(0.5)
water_curve = 1 - x^(2)
sleep_curve = 1 - x^(0.1) 

# Limiting thse graphs from 0 to 1 
 



# 
>>>>>>> 33ee28c0ac6757c0d1d2939c7461e5bcf4a43697
