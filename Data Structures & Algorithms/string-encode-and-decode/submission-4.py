class Solution:
    spacer = '#'

    def encode(self, strs: List[str]) -> str:
        msg = ''
        for string in strs:
            msg += str(len(string)) + "#" + string
        
        return msg
    def decode(self, s: str) -> List[str]:
        returnArr = []

        curWordLen = ''
        
        i = 0
        while (i < len(s)):
            if s[i].isdigit():
                curWordLen = curWordLen + (s[i])
                i+=1
            elif s[i] == "#":
                returnArr.append(s[i+1:i+1+int(curWordLen)])
                i += int(curWordLen) + 1
                curWordLen = ''
        
        return returnArr

            

            

