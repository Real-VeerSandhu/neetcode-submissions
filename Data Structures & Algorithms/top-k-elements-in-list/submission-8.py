class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freqs = collections.Counter(nums)


        freqs = [[] for _ in (range(len(nums) + 1))]

        for num, freq in num_freqs.items():
            freqs[freq].append(num)
        
        res = []

        for i in range(len(freqs) - 1, -1, -1):
            if not freqs[i]:
                continue
            
            for val in freqs[i]:
                res.append(val)

                if len(res) == k:
                    return res