class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1,hmap2 = {},{}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            hmap1[s[x]] = hmap1.get(s[x],0) + 1
            hmap2[t[x]] = hmap2.get(t[x],0) + 1
        return hmap1 == hmap2