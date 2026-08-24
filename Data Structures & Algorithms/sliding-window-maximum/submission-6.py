class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # monotinic decreasing Q from left->right
        # left/front = maximum

        l = 0
        r = 0

        while r < len(nums):


            # new element nums[r] makes every element SMALLER THAN IT obselete
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output

