class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqs = []
        for _ in range(n + 1):
            freqs.append([]) # list of lists of length n + 1
        
        num_freqs = Counter(nums)
        
        for num, freq in num_freqs.items():
            freqs[freq].append(num)
        
        res = []
        for i in range(len(freqs) - 1, -1, -1):
            if not freqs[i]:
                continue
            for num in freqs[i]:
                res.append(num)
                k -= 1

                if k == 0:
                    return res

