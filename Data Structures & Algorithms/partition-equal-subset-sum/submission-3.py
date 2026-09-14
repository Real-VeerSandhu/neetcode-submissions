class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        hash_set = set()
        hash_set.add(0)

        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) / 2

        for i in range(len(nums) - 1, -1, -1):
            new_set = set()
            for item in hash_set:
                new_set.add(item + nums[i])
            
            hash_set = hash_set.union(new_set)
        
        return target in hash_set
