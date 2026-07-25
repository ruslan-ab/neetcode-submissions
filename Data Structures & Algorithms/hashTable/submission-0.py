class HashTable:
    
    def __init__(self, capacity: int):
        self.store = [[] for _ in range(capacity)]
        self.capacity = capacity
        self.used = 0

    def _calculateHash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:    
        h = self._calculateHash(key)
        for pair in self.store[h]:
            if pair[0] == key:
                pair[1] = value
                return

        self.store[h].append([key, value])
        self.used += 1

        if self.used / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        h = self._calculateHash(key)
        for pair in self.store[h]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> bool:
        h = self._calculateHash(key)
        for i, pair in enumerate(self.store[h]):
            if pair[0] == key:
                self.store[h].pop(i)
                self.used -= 1
                return True
        return False

    def getSize(self) -> int:
        return self.used

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_store = self.store
        self.capacity *= 2
        self.store = [[] for _ in range(self.capacity)]
        self.used = 0
        for pair in old_store:
            for key, value in pair:
                self.insert(key, value)