class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1 

        while l < r:
            cur = nums[l] + nums[r]
            if cur < target:
                l += 1
                continue
            if cur > target:
                r -= 1
                continue
            
            return [l + 1, r + 1]