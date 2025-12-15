

class SetAssociativeCache:
    def __init__(self, cache_size, block_size, associativity):
        self.cache_size = cache_size
        self.block_size = block_size
        self.associativity = associativity

        
        self.num_sets = cache_size // (block_size * associativity)
        self.cache = [[None for _ in range(associativity)] for _ in range(self.num_sets)]
        self.next_replace = [0] * self.num_sets

    def get_set_index(self, address):
        return (address // self.block_size) % self.num_sets

    def get_tag(self, address):
        return (address // self.block_size) // self.num_sets

    def access(self, address):
        set_index = self.get_set_index(address)
        tag = self.get_tag(address)
        cache_set = self.cache[set_index]

        
        if tag in cache_set:
            print(f"Hit: Address {address} found in Set {set_index}")
            return True

       
        print(f"Miss: Address {address} not found in Set {set_index}")

        
        if None in cache_set:
            empty_index = cache_set.index(None)
            cache_set[empty_index] = tag
            print(f"→ Stored in empty block {empty_index} of Set {set_index}")
        else:
            
            replace_index = self.next_replace[set_index]
            cache_set[replace_index] = tag
            print(f"→ Replaced block {replace_index} in Set {set_index}")
            self.next_replace[set_index] = (replace_index + 1) % self.associativity

        return False



cache = SetAssociativeCache(cache_size=16, block_size=2, associativity=2)

addresses = [4, 8, 4, 12, 8, 14, 4]

for addr in addresses:
    cache.access(addr)
