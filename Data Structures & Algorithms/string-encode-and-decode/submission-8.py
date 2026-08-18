class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(str(len(word)))
            res.append('_')
            res.append(word)

        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        # start at length
        # obtain full length by reading until the underscore
        # read n chars, and repreat

        # 4_neet3_try
        # 012345
        i = 0
        res = []
        while i < len(s):
            cur_len = ''
            while s[i] != '_':
                cur_len += s[i]
                i += 1
            cur_len = int(cur_len)
            res.append(s[ (i+1):(i+1+cur_len) ])
            i += (cur_len) + 1
        return res
