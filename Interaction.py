class Interaction(object):
    def __init__(self, provider, time):
        self.provider = provider
        self.time = time

    def update(self, delta_min):
        self.time -= delta_min

    def complete(self):
        return self.time == 0