from sortedcontainers import SortedDict
import bisect

# Time: started 2:17
class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = SortedDict()

        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        index = self.map[key].bisect_right(timestamp)
        if index == 0:
            return ""

        return self.map[key].peekitem(index - 1)[1]
        

obj = TimeMap()
obj.set('a', 'bar', 1)
obj.set('x', 'b', 3)
p0 = obj.get('b', 3)

obj.set('love', 'high', 20)
obj.set('love', 'low', 10)
p0 = obj.get('love', 5)

obj.set('foo', 'bar', 1)
p1 = obj.get('foo', 1)
p2 = obj.get('foo', 3)
obj.set('foo', 'bar2', 4)
p3 = obj.get('foo', 4)
p4 = obj.get('foo', 5)

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# [null, null, "bar", "bar", null, "bar2", "bar2"]