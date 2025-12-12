class LFUCache:
    def __init__(self, size):
        self.size = size
        self.cache = {}        
        self.order = []     

    def access(self, block):
        def access(self, block):
    hit = block in self.cache

    if hit:
        self.cache[block] += 1
        print(f"Accessed: {block} | HIT  | Freq: {self.cache[block]}")
    else:
        if len(self.cache) >= self.size:
            min_freq = min(self.cache.values())
            candidates = [b for b in self.cache if self.cache[b] == min_freq]

            for b in self.order:
                if b in candidates:
                    evict = b
                    break

            print(f"Evicted: {evict}")
            self.cache.pop(evict)
            self.order.remove(evict)

        self.cache[block] = 1
        self.order.append(block)
        print(f"Accessed: {block} | MISS | Cache: {self.cache}")

    return hit
   

    def display(self):
        return self.cache
