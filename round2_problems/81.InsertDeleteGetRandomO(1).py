import random

# Time: 16:00
class RandomizedSet:

    def __init__(self):
        self.set = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.set.append(val)
            self.map[val] = len(self.set) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.map:
            self.set[self.map[val]] = self.set[-1]
            self.map[self.set[-1]] = self.map[val]
            del self.map[val]
            self.set.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        return self.set[random.randint(0, len(self.set) - 1)]


obj = RandomizedSet()
p1 = obj.insert(1)
p1 = obj.insert(2)
p1 = obj.insert(2)
p1 = obj.insert(3)
p1 = obj.remove(2)
p1 = obj.remove(2)
p1 = obj.getRandom()
do = 0