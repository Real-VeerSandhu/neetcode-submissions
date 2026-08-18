class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, speed) for pos, speed in zip(position, speed)]
        stack = []
        pairs = sorted(pairs, key=lambda x:x[0], reverse=True)



        for pos, speed in pairs:
            cur_time = (target - pos) / speed
            
            if not stack:
                stack.append(cur_time)
            elif cur_time > stack[-1]:
                stack.append(cur_time)

        return len(stack)