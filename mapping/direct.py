# direct.py
# Simple implementation of Direct Mapping Cache

class DirectMappingCache:
    def __init__(self, cache_lines):
        self.cache_lines = cache_lines
        self.cache = [None] * cache_lines
    
    def access_memory(self, block_number):
        # Direct mapping formula
        line = block_number % self.cache_lines