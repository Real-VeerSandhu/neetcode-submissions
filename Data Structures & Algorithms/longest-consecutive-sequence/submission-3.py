class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        finder = set()

        for num in nums:
            finder.add(num)

        seq = 1

        for num in finder:
            if (num - 1) not in finder:
                check = num + 1
                cur = 1
                while (check in finder):
                    cur+=1
                    check+=1
                if cur > seq:
                    seq = cur
           

        return seq
            

                

        
      


        