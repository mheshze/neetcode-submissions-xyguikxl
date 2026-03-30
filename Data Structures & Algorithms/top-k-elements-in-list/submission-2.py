class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for x in range(len(nums)):
            hmap[nums[x]] = hmap.get(nums[x],0) + 1
        return [key for key, val in sorted(hmap.items(), key = lambda x : x[1], reverse = True)[:k]]