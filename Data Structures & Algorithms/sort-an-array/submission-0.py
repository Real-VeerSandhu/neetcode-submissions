class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = 0
        r = 0

        while r < len(nums):


            min_right = float('inf')
            min_right_index = r
            i = r
            while i < len(nums):
                if nums[i] < min_right:
                    min_right = nums[i]
                    min_right_index = i
                i += 1
            
            nums[l], nums[min_right_index] = nums[min_right_index], nums[l]
            l += 1
            r += 1
        
        return nums