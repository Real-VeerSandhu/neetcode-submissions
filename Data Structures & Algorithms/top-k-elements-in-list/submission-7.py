class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        freqs = []
        for _ in range(len(nums) + 1):
            freqs.append([])

        for num, freq in freq_map.items():
            freqs[freq].append(num)
        
        # print(freqs)

        i = len(freqs) - 1
        res = []

        while i >= 0:
            if not freqs[i]:
                i -= 1
                continue
            
            for val in freqs[i]:
                res.append(val)

                k -= 1

                if not k:
                    return res
            
            i -= 1

