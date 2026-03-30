class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for x in range(len(nums)):
            if nums[x] in hashmap:
                return True
            hashmap[nums[x]] = x
        return False