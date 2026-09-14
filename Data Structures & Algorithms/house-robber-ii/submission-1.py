class Solution:
    def house_robber_one(self, nums):
        rob1 = 0
        rob2 = 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.house_robber_one(nums[1:]), self.house_robber_one(nums[:(len(nums)-1)]))