# direct.py
# Simple implementation of Direct Mapping Cache

class DirectMappingCache:
    def __init__(self, cache_lines):
        self.cache_lines = cache_lines
        self.cache = [None] * cache_lines
    
    def access_memory(self, block_number):
        # Direct mapping formula
        line = block_number % self.cache_lines
        
         # Check for hit or miss
        if self.cache[line] == block_number:
            return f"Cache HIT: Block {block_number} found in line {line}"
        else:
            self.cache[line] = block_number
            return f"Cache MISS: Block {block_number} loaded into line {line}"