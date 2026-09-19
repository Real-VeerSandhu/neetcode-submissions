class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fwd = [1] * n
        bwd = [1] * n


        fwd_product = 1
        for i in range(len(nums)):
            fwd_product *= nums[i]
            fwd[i] = fwd_product


        bwd_product = 1
        for i in range(len(nums) - 1, -1, -1):
            bwd_product *= nums[i]
            bwd[i] = bwd_product
        
        res = [0] * n

        for i in range(len(nums)):
            left = 1
            right = 1
            if i > 0:
                left = fwd[i - 1]
            if i < len(nums) - 1:
                right = bwd[i + 1]
            res[i] = left * right
        
        return res

        # 1 2 8 24




        # 48 48 24 6