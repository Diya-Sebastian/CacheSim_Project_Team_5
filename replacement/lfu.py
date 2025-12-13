# LFU Cache Simulator
# Implements Least Frequently Used (LFU) Cache Policy
class LFUCache:
    def __init__(self, size):
        self.size = size            #max cache size
        self.cache = {}             # Stores: block -> frequency
        self.order = []             # Maintains insertion order

    def access(self, block):  
        hit = block in self.cache     # Check if the block already exists in cache

        if hit:
            self.cache[block] += 1     # HIT: Increase frequency of the block
            print(f"Accessed: {block} | HIT  | Freq: {self.cache[block]}")
        else:
            # MISS: Check if cache is full
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
# Insert the new block with frequency = 1
            self.cache[block] = 1
            self.order.append(block)
            print(f"Accessed: {block} | MISS | Cache: {self.cache}")

        return hit
   

    def display(self):
        return self.cache
 
cache_size = int(input("Enter LFU cache size: "))
lfu_cache = LFUCache(cache_size)

ref_input = input("Enter memory references (comma-separated): ")
references = [int(x.strip()) for x in ref_input.split(",")]

hits = 0
misses = 0

for ref in references:
    if lfu_cache.access(ref):
        hits += 1
    else:
        misses += 1


# Display final results
print("\nFinal Cache State:", lfu_cache.display())
print("Total Hits  :", hits)
print("Total Misses:", misses)
print(f"Hit Ratio   : {hits/len(references):.2f}")
