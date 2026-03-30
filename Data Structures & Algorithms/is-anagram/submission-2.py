class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1,hashmap2 = {}, {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            hashmap1[s[x]] = hashmap1.get(s[x],0) + 1
            hashmap2[t[x]] = hashmap2.get(t[x],0) + 1
        return hashmap1 == hashmap2
        