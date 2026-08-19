class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []


        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a: # occurs if a != 0, a == 0 when it gets destroyed or equally matched by a +/right asteroid
                stack.append(a)
        
        return stack
        # [X,3,2,1,-4]
        -1
        4