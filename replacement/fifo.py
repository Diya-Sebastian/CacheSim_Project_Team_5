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
    if __name__ == "__main__":
        while True:
            try:
                cache_size = int(input("Enter cache size (positive integer): "))
                if cache_size <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Enter a positive integer.")

        while True:
            try:
                refs = input("Enter memory references (comma-separated): ")
                references = [int(x.strip()) for x in refs.split(",") if x.strip()]
                if not references:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Enter comma-separated integers.")
    
