class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = []

        for i, word in enumerate(strs):
            res.append(str(len(word)))
            res.append('_')
            res.append(word)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:

        i = 0
        cur_len = 0
        base = 1

        res = []

        """
        5 _ h e l l o
        0 1 2 3 4 5 6

        i = 1
        i + 1 = 2
        cur_len=5

        i + 1 + cur_len = 7
        """

        while i < len(s):
            if s[i] == '_':
                res.append(s[(i + 1) : (i + 1 + cur_len)])
                i = i + 1 + cur_len
                cur_len = 0
                base = 1
                continue
            else:
                if cur_len:
                    cur_len *= base
                

                cur_len += int(s[i])
                base *= 10
                i += 1


        return res

