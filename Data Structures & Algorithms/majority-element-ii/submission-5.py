class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        old = Counter(nums)

        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for key in count:
                if count[key] > 1:
                    new_count[key] = count[key] - 1
            count = new_count
        
        res = []
        for key in count:
            if nums.count(key) > (len(nums)//3):
                res.append(key)
        return res
        

