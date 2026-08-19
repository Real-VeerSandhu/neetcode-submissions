class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_num = float('inf')
        num_set = set()

        for num in nums:
            if num <= 0:
                continue
            min_num = min(min_num, num)
            num_set.add(num)

        if min_num > 1:
            return 1

        while min_num in num_set:
            min_num += 1
        
        return min_num if min_num != float('inf') else 1

"""
seq ->

->0,1,2,3
->4,5,6


nums=[1,2,4,5,6,3,1]


"""