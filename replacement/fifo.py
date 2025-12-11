class FIFOCache:
    def __init__(self, size):
        self.size = size
        self.cache = []

    def access(self, block):
        hit = block in self.cache
        if hit:
            print(f"Accessed: {block} | HIT  | Cache: {self.cache}")
        else:
            if len(self.cache) >= self.size:
                evicted = self.cache.pop(0)
                print(f"Evicted: {evicted}")
            self.cache.append(block)
            print(f"Accessed: {block} | MISS | Cache: {self.cache}")
        return hit
          
    def display(self):
        return self.cache
    
