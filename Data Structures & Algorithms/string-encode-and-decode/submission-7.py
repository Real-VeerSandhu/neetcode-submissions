class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i, word in enumerate(strs):
            res.append(f"!{len(word)}!")
            res.append(word)
        
        print(''.join(res))
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            i+=1
            num_start = i
            while s[i] != "!":
                i+=1
            length = int(s[num_start:i])
            # print('range',length)
            # print('word', s[i+1:i+1+length])
            res.append(s[i+1:i+1+length])
            i = i + 1 + length
        
        return res
