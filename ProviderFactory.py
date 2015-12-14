from Provider import Provider
from resources import Resources

# Different items in the house advertise themselves to the actor
# Also Includes accidents
class ProviderFactory(object):

    @staticmethod
    ## ________FOOD_______ ##
    def microwave():
        return Provider('Microwave', 10, Resources(5, -2, -3) ) #confirm resource depletion design
        # 10 minutes consumed, 5 food point provided causing 0.1 and 0.12
        # depletion in water and food respectively over a simulated time

    def oven():
        return Provider('Oven', 30, Resources(10, -3 , -3) )

    def toaster():
        return Provider('toaster', 8, Resources(7, -2 , -3) )

    ##__________WATER_________ ##
    def kitchen_tap():
        return Provider('Kitchen Tap', 2, Resources(-2, -4, 6))

    def bathroom_tap():
        return Provider('Kitchen Tap', 3, Resources(-2, -3, 4))

    ## __________SLEEP__________ ##
    def bed():
        return Provider('Bed', 2, Resources(-3, 5, -2))

    def couch():
        return Provider('Kitchen Tap', 2, Resources(-2, 6,-3))

    ## __________ACCIDENTS__________##
    def accident():

        return Provider('Accident', 30, (Resources(-10, -20, -30))

		# DOES THIS SETS THE RESOURCES TO A CERTAIN LEVEL OR DECREASE THEM BY THIS?

	# Wont need death as 0 resources would mean death and similarly dehydration
    # These give more control to see sudden changes if needed
	def death():
        return Provider('Death', -1400 , Resources(-100, -100, -100))

	def dehydration():
        return Provider('Death', 0 ,Resources(0, 0, -100)