class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [6,1,2,3,4,5]

        l ... r

        if l <= r:
            in sorted position!
        if l > r:
            it will be in right half
            l = m + 1
        """
        l = 0
        r = len(nums) - 1
        res = float('inf')

        while l <= r:
            m = (l + r) // 2

            if nums[m] <= nums[r]:
                res = min(res, nums[m])
                r = m - 1
            elif nums[m] > nums[r]:
                l = m + 1
        
        return res
            



