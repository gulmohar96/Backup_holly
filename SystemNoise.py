from Actor import Actor 
from resources import Resources 
from Provider import Provider

#HAS TO BE LINKED WITH LOCATION PROBS
class SystemNoise(object):
	@staticmethod
	
	def accident():
		return Provider('Accident', 30, (Resources(-10, -20, -30))

		# DOES THIS SETS THE RESOURCES TO A CERTAIN LEVEL OR DECREASE THEM BY THIS?
	def death():
		return Provider('Death', -1400 , Resources(-100, -100, -100))

	def dehydration():
		return Provider('Death', 0 ,Resources(0, 0, -100)


