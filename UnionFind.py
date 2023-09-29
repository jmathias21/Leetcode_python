# Resources: https://leetcode.com/explore/featured/card/graph/618/disjoint-set/3881/

# Space Complexity: O(n)
class QuickFind:

    # Runtime Complexity: O(n)
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # Runtime Complexity: O(1) (average and worst-case)
    def find(self, x):
        # in quick find, the root node is always stored in the array,
        # so we can just return it immediately
        return self.root[x]

    # Runtime Complexity: O(n)
    def union(self, x, y):
        root_x = self.root[x]
        root_y = self.root[y]

        # if the roots of both nodes are the same, they are already unioned
        if root_x != root_y:
            # update the old root of all nodes to point to the new root
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x

    # Runtime Complexity: O(1) (average and worst-case)
    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Space Complexity: O(n)
class QuickUnion:

    # Runtime Complexity: O(n)
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # Runtime Complexity: O(log n)
    def find(self, x):
        if self.root[x] == x:
            return x
        
        return self.find(self.root[x])

    # Runtime Complexity: O(log n)
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    # Runtime Complexity: O(log n)
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    

# Space Complexity: O(n)
class QuickUnionWithUnionByRank:

    # Runtime Complexity: O(n)
    def __init__(self, size):
        self.root = [i for i in range(size)]

        # starting off, each node is its own root, so we can initially set all of their
        # ranks to 1
        self.rank = [1] * size

    # Runtime Complexity: O(log n)
    def find(self, x):
        if self.root[x] == x:
            return x
        
        return self.find(self.root[x])

    # Runtime Complexity: O(log n)
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # if the x tree is taller, then we want to attach the root of the y
            # tree to the root of the x tree because it will increase the height
            # of the tree by the least amount
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            
            # if the y tree is taller, we perform the reverse operation of the above
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y

            # if the trees are the same height we pick an arbitrary new root and then
            # add one depth, because unioning two trees of the same height will always
            # increase the height by 1
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    # Runtime Complexity: O(log n)
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    

# Space Complexity: O(n)
class QuickUnionWithUnionByRankAndPathCompression:

    # Runtime Complexity: O(n)
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    # Runtime Complexity: O(log n)
    def find(self, x):
        if self.root[x] == x:
            return x
        
        # This is the only change for path compression. As the recursion unfolds and we
        # return back up the stack, each node encountered is updated to directly point
        # to the root of the component, effectively compressing the path for future operations
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # Runtime Complexity: O(log n)
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    # Runtime Complexity: O(log n)
    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = QuickUnionWithUnionByRankAndPathCompression(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
uf.find(5)
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true