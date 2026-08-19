class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num_freqs = {}

        for num in nums:
            if num not in num_freqs:
                num_freqs[num] = 1
            else:
                num_freqs[num] += 1
        
        for num, freq in num_freqs.items():
            if ( freq > math.floor(n / 2) ):
                return num