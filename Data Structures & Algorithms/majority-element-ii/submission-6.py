class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        divisor = 3
        majority_limit = math.floor(len(nums) / divisor)
        res = []
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

            if len(counts) <= 2:
                continue
            
            new_counts = defaultdict(int)
            for n, c in counts.items():
                # c == 1 never added to new_counts
                if c > 1:
                    new_counts[n] = c - 1
            counts = new_counts
        
        for n, c in counts.items():
            if nums.count(n) > majority_limit:
                res.append(n)
        
        return res