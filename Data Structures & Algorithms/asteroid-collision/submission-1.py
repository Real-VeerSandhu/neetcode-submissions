class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if abs(a) > abs(stack[-1]):  # current asteroid is bigger
                    stack.pop()
                    continue
                elif abs(a) == abs(stack[-1]):  # both destroy each other
                    stack.pop()
                # in both equal or smaller cases, current asteroid is gone
                a = 0
                break
            
            if a:
                stack.append(a)

        return stack