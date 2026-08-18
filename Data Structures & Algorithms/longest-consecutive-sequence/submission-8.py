class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        res = 0

        """
            Input: nums = [2,20,4,10,3,4,5]

            Output: 4

            2,20,4,10,3,4,5


        """
        res = 0

        for num in nums_set:
            if ((num - 1) not in nums_set):
                # print(f"---({num}) is start of seq---")

                p = num
                while p in nums_set:
                    p += 1
                
                res = max(res, p - num)
        
        return res





