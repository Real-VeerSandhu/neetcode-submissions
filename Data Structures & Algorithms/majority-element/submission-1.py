class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        target = 0

        for num in nums:
            if freq == 0:
                target = num
            freq += 1 if target == num else -1
        
        return target
            