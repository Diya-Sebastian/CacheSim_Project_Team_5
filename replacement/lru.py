# LRU Cache Simulation

class LRUCache:
    def __init__(self, size):
        self.size = size      # Maximum cache size
        self.cache = []       # Cache memory

    def access(self, block):
        # Cache HIT
        if block in self.cache:
            self.cache.remove(block)
            self.cache.append(block)
            print(f"Accessed {block} → HIT  | Cache: {self.cache}")

        # Cache MISS
        else:
            if len(self.cache) >= self.size:
                evicted = self.cache.pop(0)   # Remove LRU block
                print(f"Evicted: {evicted}")

            self.cache.append(block)
            print(f"Accessed {block} → MISS | Cache: {self.cache}")

