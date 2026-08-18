class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newNum = [0] * len(nums) #array of 0's

        total = 1
        zeroCount = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1

            total *= nums[i] #total product of all

        if zeroCount > 1:
            return newNum

        total_two = 1
        zero_idx = 0

        if zeroCount == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    total_two *= nums[i] #product of all expct 0
                        
                if nums[i] == 0:
                    zero_idx = i
            newNum[zero_idx] = total_two
            return newNum


        for j in range(len(nums)):
                        
            newVal = total // nums[j]
            newNum[j] = newVal

        return newNum
        

        

        
