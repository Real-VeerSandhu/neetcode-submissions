class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                new_num = num + 1
                while new_num in nums_set:
                    new_num += 1
                res = max(res, new_num - num)

        return res