from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.isfile = False
        self.content = ""
        self.children = defaultdict(TrieNode)

# https://leetcode.com/problems/design-in-memory-file-system/
# Tags: Prefix Tree, Trie
# Time: Not timed
class FileSystem:

    def __init__(self):
        self.files = TrieNode()

    def ls(self, path: str) -> List[str]:
        path_lst = path.split("/")
        node = self.files
        for p in path_lst:
            if not p:
                continue
            node = node.children.get(p)
        if node.isfile:
            return [p]
        ans = [i for i in node.children.keys()]
        if not ans:
            return ans
        ans.sort()
        return ans
            
            
    def mkdir(self, path: str) -> None:
        path_lst = path.split("/")
        node = self.files
        for p in path_lst:
            if not p:
                continue
            node = node.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_lst = filePath.split("/")
        node = self.files
        for p in path_lst:
            if not p:
                continue
            node = node.children[p]
        node.content += content
        node.isfile = True
        
    def readContentFromFile(self, filePath: str) -> str:
        path_lst = filePath.split("/")
        node = self.files
        for p in path_lst:
            if not p:
                continue
            node = node.children.get(p)
        return node.content


obj = FileSystem()
obj.mkdir("/dir1/a")
obj.mkdir("/dir1/b")
obj.mkdir("/dir2/c")
param_1 = obj.ls("/")
obj.addContentToFile("/dir1/a/file.txt", "hello world")
param_1 = obj.ls("/dir1/a/file.txt")
param_4 = obj.readContentFromFile("/dir1/a/file.txt")
do = 0