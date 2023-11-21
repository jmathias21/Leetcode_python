from collections import defaultdict

# https://leetcode.com/problems/maximum-frequency-stack/
# Tags: Hash Map
# Time: Not timed
class FreqStack:

    # Space Complexity: O(n)
    def __init__(self):
        self.group = defaultdict(list)
        self.frequencies = defaultdict(int)
        self.max_freq = 0
    
        
    # Runtime Complexity: O(1)
    def push(self, val: int) -> None:
        self.frequencies[val] += 1
        self.group[self.frequencies[val]].append(val)
        self.max_freq = max(self.max_freq, self.frequencies[val])
        

    # Runtime Complexity: O(1)
    def pop(self) -> int:
        x = self.group[self.max_freq].pop()
        self.frequencies[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x


obj = FreqStack()
obj.push(1)
obj.push(0)
obj.push(0)
obj.push(1)
obj.push(5)
obj.push(4)
obj.push(1)
obj.push(5)
obj.push(1)
obj.push(6)
p1 = obj.pop()
p1 = obj.pop()
p1 = obj.pop()
p1 = obj.pop()
p1 = obj.pop()
p1 = obj.pop()
p1 = obj.pop()
p1 = obj.pop()
p1 = obj.pop()
do = 0