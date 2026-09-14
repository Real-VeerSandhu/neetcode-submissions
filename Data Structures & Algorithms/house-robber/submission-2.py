class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [nums[0], max(nums[0], nums[1])]
        res = max(dp)

        for i in range(2, len(nums)):
            tmp_dp1 = dp[1]
            dp[1] = max(dp[1], dp[0] + nums[i])
            dp[0] = tmp_dp1
            res = max(res, max(dp))
        
        return res
