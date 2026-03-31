class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force greedy
        numSet = set(nums)
        res = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                cur = num
                while cur + 1 in numSet:
                    length += 1
                    cur += 1
                res = max(length,res)
        return res