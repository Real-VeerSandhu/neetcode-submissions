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

        pre_fwd = [1] * n
        pre = 1
        for i in range(len(nums)):
            pre *= nums[i]
            pre_fwd[i] *= pre
        
        post_bwd = [1] * n
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            post *= nums[i]
            post_bwd[i] *= post
        
        res = [1] * n

        for i in range(len(res)):
            left = 1 if i == 0 else pre_fwd[i - 1]
            right = 1 if i == n - 1 else post_bwd[i + 1]

            res[i] = left * right
        
        return res