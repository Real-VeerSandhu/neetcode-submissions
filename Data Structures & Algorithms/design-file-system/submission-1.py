class TrieNode:
    def __init__(self, name):
        self.mp = defaultdict(TrieNode)
        self.name = name
        self.value = -1

class FileSystem:

    def __init__(self):
        self.root = TrieNode('')


    def createPath(self, path: str, value: int) -> bool:
        components = path.split('/') # get array of dirs

        cur = self.root

        for i in range(1, len(components)):
            name = components[i]

            if name not in cur.mp:
                if i == len(components) - 1:
                    cur.mp[name] = TrieNode(name)
                else:
                    return False
            cur = cur.mp[name]

        if cur.value != -1:
            return False
        
        cur.value = value
        return True

    def get(self, path: str) -> int:
        cur = self.root

        components = path.split('/')

        for i in range(1, len(components)):
            name = components[i]

            if name not in cur.mp:
                return -1
            
            cur = cur.mp[name]
        
        return cur.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
