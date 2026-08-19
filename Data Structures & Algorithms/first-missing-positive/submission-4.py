class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i, num in enumerate(nums):
            
            if num < 0:
                nums[i] = 0
        
        for i, num in enumerate(nums):
            if num == 0 or num == '0':
                continue
            
            num = abs(num)

            if num > len(nums):
                continue
            
            index_to_mark = num - 1
            if nums[index_to_mark] == '0' or nums[index_to_mark] < 0:
                continue

            nums[index_to_mark] = nums[index_to_mark] * -1 if nums[index_to_mark] > 0 else '0'
        
        # print(nums)

        for i, num in enumerate(nums):
            if num == '0' or num < 0:
                continue
            return i + 1

        return len(nums) + 1
        

        

"""
[1, 2, 3, 4] -> 1...5 is answer

[-1, 2, 3, 5, 0]
[-1, -2, 3, 5, 0]
[-1, -2, -3, 5, 0]
[-1, -2, -3, 5, -0]









1   2   3   4   5
1<>Y   1<>Y   4<>Y   2<>Y   N


i=0, num=3

nums[3] = True



"""