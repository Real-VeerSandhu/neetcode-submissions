class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Input: nums = [3,4,5,6,1,2], target = 1

        5,6,1,2,3,4 . . . . target = 2



        nums = [0,1,2] target = 0


        """
        l = 0
        r = len(nums) - 1


        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # check if we are are in left sorted portion!!

            if nums[l] <= nums[m]:
                # we are in the left sorted portion
                # [5,6,7,8,1,2,3,4]
                # [1,2,3,4,5,6,7]

                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
                continue
            else:
                # we are in the right sorted portion
                # [8,9,1,2,3,4,5,6,7]

                if target >= nums[l] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1