class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        target = 0

        for num in nums:
            if res == 0:
                target = num
            res += 1 if num == target else -1
        
        return target