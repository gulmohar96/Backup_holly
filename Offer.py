class Offer(object):
<<<<<<< HEAD
    def __init__(self, provider, time, payoff):
        self.provider = provider
        self.time = time
        self.payoff = payoff

    def __str__(self):
        result = str(self.payoff) + " from "
        result += self.provider.name + " over "
        result += str(self.time) + " minutes"
        return result
 
=======
    # Intermediate...Just represents the offers from the provider for easy code usage
    def __init__(self, name, time_consumed, resources):
        self.name = name
        self.time_consumed  = time_consumed
        self.resources = resources
        return(self.name, self.time_consumed, self.resources)
>>>>>>> 33ee28c0ac6757c0d1d2939c7461e5bcf4a43697
