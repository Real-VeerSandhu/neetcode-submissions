class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        prefix = 0

        for num in nums:
            prefix += num

            if (prefix - k) in prefix_map:
                res += prefix_map[prefix - k]
            
            prefix_map[prefix] += 1
        
        return res
