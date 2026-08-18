class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}

        for i, num in enumerate(nums):
            if (target - num) in target_map:
                return [target_map[target - num], i]
            
            target_map[num] = i
        