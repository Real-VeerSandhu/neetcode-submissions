class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.q = deque()

        for index, vector in enumerate(self.vectors):
            if len(vector) > 0:
                # tuple == (index_of_vector, 
                #           index_of_element_in_vector_to_output)

                self.q.append((index, 0))

    def next(self) -> int:
        if self.q:
            vec_index, ele_index = self.q.popleft() # this HOLDS next as in RIGHT NOW TO OUTPUT

            next_ele_index = ele_index + 1

            if next_ele_index < len(self.vectors[vec_index]):
                self.q.append((vec_index, next_ele_index))
            
            return self.vectors[vec_index][ele_index]
        

    def hasNext(self) -> bool:
        return len(self.q) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
