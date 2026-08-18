class Solution:
    def two_sum(self, nums, target, init):
        l = 0
        r = len(nums) - 1
        res = []

        while l < r:
            cur = nums[l] + nums[r]
            if cur == target:
                res.append([init, nums[l], nums[r]])
                l += 1
                while l < len(nums) and nums[l] == nums[l - 1]:
                    l += 1
            elif cur < target:
                l += 1
            else:
                r -= 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

            [-4, -2, -1, -1, -1, 0, 1, 1, 2, 2]

            -4, 2, 2
            -1, -1, 2
            -1, 1, 1
            -1, 0, 1



        """
        nums.sort()
        res = []

        # print(nums)

        for i in range(len(nums)):
            num = nums[i]
            if num > 0:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            two_sum_res = self.two_sum(nums[i + 1:], -1 * num, num)
            if not two_sum_res:
                continue
            res.extend(two_sum_res)


        return res