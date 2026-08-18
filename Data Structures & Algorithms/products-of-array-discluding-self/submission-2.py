class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

            1   2   4   6
        
        fwd 1   2   8   48

        bwd 48  48  24   6             

        """

        fwd = [1] * len(nums)
        fwd_p = 1

        for i, num in enumerate(nums):
            if i == 0:
                fwd[i] = num
                continue
            fwd[i] = fwd[i - 1] * num
        
        bwd = [1] * len(nums)
        bwd_p = 1

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]

            if i == (len(nums) - 1):
                bwd[i] = num
                continue
            bwd[i] = bwd[i + 1] * num

        res = [1] * len(nums)

        for i in range(len(res)):
            L, R = 1, 1
            if i != 0:
                L = fwd[i - 1]
            
            if i != len(res) - 1:
                R = bwd[i + 1]
            
            res[i] = L * R




        return res