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

    def search(self, nums: List[int], target: int) -> int:
        
        res = self._lower_bound(nums, target)

        return res if res < len(nums) and nums[res] == target else -1