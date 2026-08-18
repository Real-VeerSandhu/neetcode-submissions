class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_index = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal_index:
                goal_index = i # goal i smaller cuz we could reach prev one
        
        return goal_index == 0
        