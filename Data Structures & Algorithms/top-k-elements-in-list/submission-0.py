class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = []

        for _ in range(len(nums) + 1):
            freqs.append([])


        # print(freqs)



        nums_counter = collections.Counter(nums)

        # print(nums_counter)

        for num in nums_counter:
            freqs[nums_counter[num]].append(num)

        # print(freqs)
        
        res = []
        for i in range(len(freqs) - 1, -1, -1):
            for j in range(len(freqs[i]) -1, -1, -1):
                res.append(freqs[i][j])

                k -= 1
                if k == 0:
                    return res


