class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse_vec = []

        for i, num in enumerate(nums):
            if num != 0:
                self.sparse_vec.append((i, num))


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        p = 0
        q = 0

        while p < len(self.sparse_vec) and q < len(vec.sparse_vec):
            if self.sparse_vec[p][0] == vec.sparse_vec[q][0]:
                res += self.sparse_vec[p][1] * vec.sparse_vec[q][1]
                p += 1
                q += 1
            elif self.sparse_vec[p][0] < vec.sparse_vec[q][0]:
                p += 1
            else:
                q += 1
        
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
