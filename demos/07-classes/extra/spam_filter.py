class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return filter(lambda x: x not in self.blocked,
                      sequence)

class SPAMFilter(Filter): # SPAMFilter is a subclass of Filter
    def init(self): # Overrides init method from Filter superclass
        self.blocked = ['SPAM']
