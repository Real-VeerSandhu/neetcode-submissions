class Solution:
    def _lower_bound(self, nums, a):
        lo = 0
        hi = len(nums)

        while lo < hi:
            m = (lo + hi) // 2
            if nums[m] < a:
                lo = m + 1
            else:
                hi = m

        return lo
    
    def _upper_bound(self, nums, a):
        lo = 0
        hi = len(nums)

        while lo < hi:
            m = (lo + hi) // 2
            if nums[m] <= a:
                lo = m + 1
            else:
                hi = m
        return lo

    def search(self, nums: List[int], target: int) -> int:
        
        res = self._upper_bound(nums, target) - 1

        return res if res >= 0 and nums[res] == target else -1