class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:
            num = nums[i]
            if num == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
                continue
            if num == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                continue
            i += 1
        
