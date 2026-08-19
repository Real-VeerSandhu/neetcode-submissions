class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        min_int = 1

        while min_int in num_set:
            min_int += 1
    
        return min_int

"""
seq ->

->0,1,2,3
->4,5,6


nums=[1,2,4,5,6,3,1]


"""