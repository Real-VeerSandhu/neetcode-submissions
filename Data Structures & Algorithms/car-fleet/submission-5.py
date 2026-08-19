class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
            Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]


        [(0, 1), (1, 2), (4, 2), (7, 1)]




        """

        n = len(position)
        cars = []
        stack = []
        res = 0

        for i in range(n):
            time_to_target = (target - position[i]) / speed[i]
            cars.append((position[i], speed[i], time_to_target))
        
        cars.sort(key = lambda x : x[0], reverse=True)
        

        for pos, v, t in cars:
            if not stack:
                stack.append(t)
                res += 1
                continue
            
            if stack[-1] >= t:
                old_t = stack.pop()
                stack.append(old_t)
            else:
                stack.append(t)
                res += 1
        
        return res
            

                
            

