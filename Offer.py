class Offer(object):
    # Intermediate...Just represents the offers from the provider for easy code usage
    def __init__(self, name, time_consumed, resources):
        self.name = name
        self.time_consumed  = time_consumed
        self.resources = resources
        return(self.name, self.time_consumed, self.resources)
