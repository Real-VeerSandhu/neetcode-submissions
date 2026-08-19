class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        quad = [] # current quadruplet is!!

        def k_sum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    k_sum(k - 1, i + 1, target- nums[i])
                    quad.pop()
                return
            
            # two sum II
            l = start
            r = len(nums) - 1
            while l < r:
                cur_sum = nums[l] + nums[r]

                if cur_sum < target:
                    l += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]]) # extend full list
                    l += 1
                    r -= 1 # it works when i remove this??

                    while l < len(nums) and nums[l] == nums[l - 1]: # i can also do l < len(nums)?? why??
                        l += 1
        
        k_sum(4, 0, target)
        return res
