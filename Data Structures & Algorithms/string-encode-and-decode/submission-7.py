class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # part = f"{len(s)} # + {s}"
            part = str(len(s))+'#'+s
            res+=part
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            s_len = int(s[i:j])
            
            part = s[j + 1 : j + 1 + s_len]
            res.append(part)
   
            i = j + 1 + s_len
            
        return res