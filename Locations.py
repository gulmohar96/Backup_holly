
## _____IGNORE THIS AS OF NOW______##
class Locations(object):

    ## Problems with location recording:
    # don't know how sensors are set up
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