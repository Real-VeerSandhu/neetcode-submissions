class Solution:
    def _lower_bound(self, nums, target):
        lo = 0
        hi = len(nums)

        while lo < hi:
            m = (lo + hi) // 2

            if nums[m] < target:
                lo = m + 1
            else:
                hi = m
        
        return lo
    def search(self, nums: List[int], target: int) -> int:
        res = self._lower_bound(nums, target)

        if res < len(nums) and nums[res] == target:
            return res
        return -1


        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        
        return -1