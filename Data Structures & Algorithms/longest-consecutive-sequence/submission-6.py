class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0 #counts consecutive seq
        numSet = set(nums)



        for n in nums:
            if (n - 1) not in numSet:
                length = 0

                while (n + length) in numSet:
                    length += 1
                count = max(count, length)

        return count

            
            




        