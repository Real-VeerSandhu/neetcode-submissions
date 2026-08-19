class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []


        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue
            
            if not stack:
                stack.append(a)
                continue

            while stack:
                if stack[-1] < 0:
                    break
                
                if stack[-1] < abs(a):
                    stack.pop()
                else:
                    break
                
            if not stack or stack[-1] < 0:
                stack.append(a)
                continue
            if stack[-1] == a * -1:
                stack.pop()
                continue
            if stack[-1] > a * -1:
                continue

        return stack
        
        # [X,3,2,1,-4]
        -1
        4