class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        res = []

        for key in counter:
            if counter[key] > (len(nums) // 3):
                res.append(key)

        return res