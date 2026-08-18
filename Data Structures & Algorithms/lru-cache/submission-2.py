class Node:
    def __init__(self, key = 0, value = 0, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # maps KEY to dll NODE
        self.cap = capacity
        self.left = Node()
        self.right = Node() # front
        self.left.next = self.right
        self.right.prev = self.left

    def _add_to_front(self, key):
        cur_node = self.cache[key]

        old_prev = self.right.prev


        old_prev.next = cur_node
        cur_node.prev = old_prev

        self.right.prev = cur_node
        cur_node.next = self.right
    
    def _delete_node(self, key):
        cur_node = self.cache[key]
        old_prev = cur_node.prev
        old_next = cur_node.next

        old_prev.next = cur_node.next
        old_next.prev = cur_node.prev

        cur_node.next = None
        cur_node.prev = None


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self._delete_node(key)
        self._add_to_front(key)

        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._delete_node(key)
            del self.cache[key]

        self.cache[key] = Node(key, value)

        self._add_to_front(key)

        if len(self.cache) > self.cap:
            key_to_delete = self.left.next.key
            self._delete_node(key_to_delete)
            del self.cache[key_to_delete]
