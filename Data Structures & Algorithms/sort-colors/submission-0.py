class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        number_colour_map = ['red', 'white', 'blue']
        colour_count = {'red': 0, 'white': 0, 'blue': 0}

        for num in nums:
            colour_count[number_colour_map[num]] += 1
        
        i = 0
        while i < len(nums) and colour_count['red']:
            nums[i] = 0
            colour_count['red'] -= 1
            i += 1
        
        while i < len(nums) and colour_count['white']:
            nums[i] = 1
            colour_count['white'] -= 1
            i += 1
        
        while i < len(nums) and colour_count['blue']:
            nums[i] = 2
            colour_count['blue'] -= 1
            i += 1
        
        return nums
