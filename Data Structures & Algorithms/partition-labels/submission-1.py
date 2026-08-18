class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}

        for i, c in enumerate(s):
            last_index[c] = i
        
        res = []
        count = 0
        end = 0

        for i, c in enumerate(s):
            count += 1

            end = max(end, last_index[c])

            if i == end:
                # cant extend more
                res.append(count)
                count = 0
        
        return res