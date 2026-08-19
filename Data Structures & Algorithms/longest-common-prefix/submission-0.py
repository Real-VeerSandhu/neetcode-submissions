class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        res = ''
        min_length = float('inf')

        for word in strs:
            min_length = min(min_length, len(word))
        
        if min_length == 0:
            return res
        
        while i < min_length:
            cur_char = strs[0][i]

            for word in strs:
                if word[i] != cur_char:
                    return res
            
            res += cur_char
            i += 1
        
        return res
                    

            
