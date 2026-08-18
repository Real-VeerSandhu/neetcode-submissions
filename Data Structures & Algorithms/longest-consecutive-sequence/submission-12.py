class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            if (num - 1) not in num_set:
                cur = num
                while cur in num_set:
                    cur += 1
                res = max(res, cur - num)
        
        return res