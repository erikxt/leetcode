class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.record = []
        self.cache = {}
        
    # @return an integer
    def get(self, key):
        if self.cache.has_key(key):
            self.record.remove(key)  
            self.record.append(key)
            return self.cache.get(key)
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.cache.has_key(key):
            self.record.remove(key)  
            del self.cache[key]
        if len(self.record) >= self.capacity:
            lru = self.record.pop(0)
            del self.cache[lru]
        self.record.append(key)
        self.cache[key]=value


def main():
    s=LRUCache(10)
    s.set(10,13)
    s.set(3,17)
    s.set(6,11)
    s.set(10,5)
    s.set(9,10)
    s.get(13)
    s.set(2,19)
    s.get(2)
    print s.get(3)
        
    
if __name__  == "__main__":
    main()
