from collections import defaultdict
from typing import List

# 
# Tags: 
# Time: started 8:11
class FreqStack:

    def __init__(self):
        self.frequencies = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.frequencies[val] += 1
        self.group[self.frequencies[val]].append(val)
        self.max_freq = max(self.max_freq, self.frequencies[val])
        

    def pop(self) -> int:
        x = self.group[self.max_freq].pop()
        self.frequencies[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x


obj = FreqStack()
obj.push(1)
obj.push(1)
obj.push(1)
obj.push(2)
obj.push(2)
obj.push(2)
param_2 = obj.pop()
param_2 = obj.pop()
param_2 = obj.pop()
param_2 = obj.pop()