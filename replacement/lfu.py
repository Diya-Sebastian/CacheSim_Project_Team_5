class LFUCache:
    def __init__(self, size):
        self.size = size
        self.cache = {}        
        self.order = []        

    def display(self):
        return self.cache
