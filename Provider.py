class Provider(object):
<<<<<<< HEAD
    def __init__(self, name, time, resources):
        self.name = name
        self.time = time
        self.resources = resources

    def offer(self):
        return Offer(self, self.time, self.resources)

    def __str__(self):
        return self.name
=======
    # The provider provides different offers from all the possible resources in the house
    def __init__(self,name,time_consumed,resources):
        self.name = name
        self.time_consumed = time_consumed
        self.resources = resources # Gives the status of the resources at after the usage of a particular object
                                   # that is making a offer

    def make_offer(self):
        return(self.name, self.time_consumed, self.resources)

>>>>>>> 33ee28c0ac6757c0d1d2939c7461e5bcf4a43697
