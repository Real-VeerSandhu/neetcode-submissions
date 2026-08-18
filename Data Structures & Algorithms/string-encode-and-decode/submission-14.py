class Solution:

    def encode(self, strs: List[str]) -> str:
        code = []

        for word in strs:
            code.append(str(len(word)))
            code.append('_')
            code.append(word)
        
        return ''.join(code)


    """
    0   1   2   3   4   5
    2   _   a   b   1   _

    """

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] != '_':
                j += 1
            cur_num_length = int(s[i:j])

            j += 1
            res.append(s[j:j+cur_num_length])

            i = j + cur_num_length
        
        return res