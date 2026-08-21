

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        
    def _traverse(self, path, create=False):
        node = self.root

        parts = []
        for p in path.split('/'):
            if p:
                parts.append(p)
        
        for part in parts:
            if part not in node.children:
                if create:
                    node.children[part] = TrieNode()
            node = node.children[part]

        return node

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        if node.is_file:
            return [path.split('/')[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path, create=True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur_node = self._traverse(filePath, True)
        cur_node.is_file = True
        cur_node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self._traverse(filePath).content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
