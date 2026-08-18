class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

            1   2   4   6
        
        fwd 1   2   8   48

        bwd 48  48  24   6             

        """

        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        print('prefix:', prefix)

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
    
        return res




            