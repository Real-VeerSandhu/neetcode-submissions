class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        prefix_sum = 0


        for i, num in enumerate(nums):
            prefix_sum += num

            if (prefix_sum - k) in prefix_map:
                res += prefix_map[prefix_sum - k]
            
            prefix_map[prefix_sum] += 1
        
        return res