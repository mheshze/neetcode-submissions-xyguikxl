class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , n = 0, len(s)
        setr = set()
        res = 0
        for r in range(n):
            while s[r] in setr:
                setr.remove(s[l])
                l += 1

            width = (r-l) + 1
            res = max(res,width)
            setr.add(s[r])
        return res
