class Provider(object):
    # The provider provides different offers from all the possible resources in the house
    def __init__(self,name,time_consumed,resources):
        self.name = name
        self.time_consumed = time_consumed
        self.resources = resources # Gives the status of the resources at after the usage of a particular object
                                   # that is making a offer

    def make_offer(self):
        return(self.name, self.time_consumed, self.resources)

