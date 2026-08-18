class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """"
        1   2   3   4
        
        pre-fwd
        1   2   4   24


        post-bwd
        48   48   12   4

        """
        n = len(nums)

        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i] # product of all elements to the left
        postfix = 1

        for i in range(n - 1, -1, -1):
            res[i] *= postfix # product of all elements to the right
            postfix *= nums[i]
        
        return res