class Solution:

    def encode(self, strs: List[str]) -> str:
        delim = ','
        enc = ''
        for s in strs:
            enc += str(len(s)) + delim
        enc += '#'
        for x in strs:
            enc += x
        return enc
        #4,4,#neetcode

    def decode(self, s: str) -> List[str]:
        i = 0
        delim = ','
        sizes,res = [],[]
        while s[i] != "#":
            cur = ""
            while s[i] != delim:
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for x in range(len(sizes)):
            res.append(s[i:i+sizes[x]])
            i += sizes[x]
        
        return res
            