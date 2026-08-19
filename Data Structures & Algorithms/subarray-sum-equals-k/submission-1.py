class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Input: nums = [2,-1,1,2], k = 2




        """
        res = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in prefix_map:
                res += prefix_map[prefix_sum - k]
            
            prefix_map[prefix_sum] += 1
        
        return res