class Provider(object):
    def __init__(self, name, time, resources):
        self.name = name
        self.time = time
        self.resources = resources

    def offer(self):
        return Offer(self, self.time, self.resources)

    def __str__(self):
        return self.name
