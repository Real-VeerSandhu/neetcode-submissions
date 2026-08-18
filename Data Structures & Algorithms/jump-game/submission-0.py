class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for i, num in enumerate(nums):
            # if max_jump == i:
            print('mj', max_jump, 'i', i)
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + num)
            # else:
        
        return True
        