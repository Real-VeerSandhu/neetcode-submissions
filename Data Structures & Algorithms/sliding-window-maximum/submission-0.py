class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            deque is monotonic decreasing, left is big, right is small
             left is always the max, and will be added to res
             we will pop from right whenver adding soemthing that v
             violated the monotonci decreasing property
        """
    
        output = []
        q = deque() # indices
        l = 0
        r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # new val vioalted monotic
                q.pop() # pop from right
            q.append(r) # add to right

            if l > q[0]: # out of bounds
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output