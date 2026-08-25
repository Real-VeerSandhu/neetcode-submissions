class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse_vec = {}

        for i, num in enumerate(nums):
            if num != 0:
                self.sparse_vec[i] = num


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0

        for idx in self.sparse_vec:
            if idx in vec.sparse_vec:
                res += vec.sparse_vec[idx] * self.sparse_vec[idx]
        
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
