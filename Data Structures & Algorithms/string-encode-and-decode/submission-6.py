class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(f"{str(len(word))}_")
            res.append(word)
        return (''.join(res))

    def decode(self, s: str) -> List[str]:
        res = []

        print(s)
        i=0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '_':
                j+=1
            # print('->', i,j)
            cur_len = int(s[i:j])
            # print(s[j+1:j+1+cur_len])
            res.append(s[j+1:j+1+cur_len])
            i = j+1+cur_len

        return res
